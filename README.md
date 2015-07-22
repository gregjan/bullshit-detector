Bullshit Detector
=================

Bullshit detector is a service that matches news shared via social media with current issues investigated by fact checking sites. It is intended to help individuals respond to false and misleading stories that tend to "go viral" all too often.

Features
--------

The service monitors the news feeds of major fact checking web sites. This data is matched with social media data to support fast responses to friends and family who post misleading stories.

* Bullshit Detected Page - Page displays all posts visible to the user that cite misleading articles, in the main body or comments. Posts might eventually be grouped by issue.

* "Call Bullshit" Button - Big button that facilitates a rapid response to the friends and family that have posted misleading stories. A template message will be provided that cites the fact check URL.

* Bullshit Artists - A page that shows the top offenders that have been detected so far. These are your social media connections who have posted the most bullshit.

* Rumor Mills - Page shows the sites that are notorious sources of bullshit. Perhaps the sources most often cited by friends?

* Stats - How many times have people called out some bullshit today on Facebook. Honor roll of friends who have called out the most bullshit and where you rank among them.

Components
----------

* Mirror of rumor mills - Collected headlines and descriptions from fact checking sites in MongoDB.

* Cache of matched URLs - A lookup table of URLs that the Bullshit Detector has already been matched with misleading stories.

* Matching Algorithm - OpenNLP plagiarism schemes should work, for one thing.

Fact Check Sites
-----------------
* Snopes - http://www.snopes.com/info/whatsnew.xml
* Truth or Fiction - http://truthorfiction.com/feed/
* PolitiFact - http://politifact.org/feeds/statements/truth-o-meter/
* Fact Check - http://www.factcheck.org/feed/
