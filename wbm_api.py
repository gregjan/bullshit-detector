import requests
import os
import errno
import wget
import untangle
import glob
import logging
from readability import Document
import json
import hashlib


DEFAULT_SAVE_PATH = 'feed_archives'


def get_history_links(url):
    request_url = "http://web.archive.org/cdx/search/xd?url="
    request_url += url
    request_url += "&fl=timestamp,original&collapse=digest&gzip=false&filter=statuscode:200"

    resp = requests.get(request_url)
    resp.raise_for_status()
    return generate_links(resp.text)


def generate_links(text):
    for line in text.splitlines():
        (timestamp, url) = line.split()
        yield (timestamp, "http://web.archive.org/web/{0}/{1}".format(timestamp, url))


def download_feed_history(name, url, only_count=False, total=-1):
    savefolder = os.path.join(DEFAULT_SAVE_PATH, name, 'rss_archive')
    mkdir_p(savefolder)
    count = 0
    for (timestamp, link) in get_history_links(url):
        if only_count:
            count += 1
            continue
        f = os.path.join(savefolder, timestamp+'.xml')
        if os.path.exists(f):
            continue
        print('Saving {0} from {1} at {2}'.format(name, timestamp, f))
        wget.download(link, f)
    return count


def download_article_html(name, only_count=False, total=-1):
    rss_archive = os.path.join(DEFAULT_SAVE_PATH, name, 'rss_archive')
    article_archive = os.path.join(DEFAULT_SAVE_PATH, name, 'raw_articles')
    mkdir_p(article_archive)
    count = 0
    for rss in glob.glob(rss_archive+'/*.xml'):
        obj = untangle.parse(rss)
        if count > 1:
            break
        for item in obj.rss.channel.item:
            guid = item.guid.cdata
            title = item.title.cdata
            try:
                orig_link = item.feedburner_origLink
            except IndexError as e:
                logging.error(e)
                break
            link = "http://web.archive.org/web/{0}".format(orig_link)
            h = hashlib.sha224(guid).hexdigest()
            f = os.path.join(article_archive, h+'.html')
            if os.path.exists(f):
                continue
            count += 1
            if only_count:
                continue
            print(u'Downloading {0}/{1}: {2}'.format(count, total, title))
            resp = requests.get(link)
            if resp.status_code == 200:
                with open(f, 'w') as fp:
                    fp.write(resp.text)
    return count


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def extract_content_texts(name):
    article_archive = os.path.join(DEFAULT_SAVE_PATH, name, 'raw_articles')
    json_archive = os.path.join(DEFAULT_SAVE_PATH, name, 'json_articles')
    mkdir_p(json_archive)
    for html in glob.glob(article_archive+'/*.html'):
        fname = os.path.basename(html)+'.json'
        savepath = os.path.join(json_archive, fname)
        if os.path.exists(savepath):
            logging.info('Skipping existing json data: {0}'.format(savepath))
            continue
        data = {}
        with open(html, 'r') as myfile:
            doc = Document(myfile.read())
            data['title'] = doc.title()
            data['content'] = doc.content()
            data['summary'] = doc.summary()
            with open(savepath, 'w') as saving:
                json.dump(data, saving)


def get_historical_feed(name='breitbart', rss_url='http://feeds.feedburner.com/breitbart'):
    count_rss = download_feed_history(name, rss_url, only_count=True)
    print('{0} RSS feed archives to download for {1}'.format(count_rss, name))
    download_feed_history(name, rss_url, total=count_rss, only_count=True)
    count_articles = download_article_html(name, only_count=True)
    print('{0} articles to download for {1}'.format(count_articles, name))
    download_article_html(name, total=count_articles)
    extract_content_texts(name)


def main():
    get_historical_feed()

main()
