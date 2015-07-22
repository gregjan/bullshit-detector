Bullshit Detector
=================

Bullshit detector is a service that matches news shared via social media with current issues investigated by fact checking sites. It is intended to help individuals respond to false and misleading stories that tend to "go viral" all too often. Let's call out bullshit when we see it and refocus debate on goals and evidence.

Features
--------

The service monitors the news feeds of major fact checking web sites. This data is matched with social media data to support fast responses to friends and family who post misleading stories.

* Bullshit Detected Page - Page displays all posts visible to the user that cite misleading articles, in the main body or comments. Posts might eventually be grouped by issue. Will be limited to a certain number of posts or a certain time range. (We cannot process all the posts, all the time.)

* Smells Like Some Bullshit - These are stories or posts that are likely to be bullshit, based on some identifiable traits. The most likely indicator is the original news site that produced the story. These rumor mills come up with misleading stories every day. Page will facilitate the submission of the story to a fact checking site.

* "Call Bullshit" Button - Big button that facilitates a rapid response to the friends and family that have posted misleading stories. A template message will be provided that cites the fact check URL.

* Bullshit Artists - A page that shows the top offenders that have been detected so far. These are your social media connections who have posted the most bullshit.

* Rumor Mills - Page shows the sites that are notorious sources of bullshit. Perhaps the sources most often cited by your friends?

* Leaderboard and Gamification - Honor roll of friends who have called out the most bullshit and where you rank among them. Badges for various things: streaks of responding to all friends bullshit for a day, a week, a month, number of times called bullshit, first time calling bullshit, first time writing your own response, posting a follow up response, etc..

* Making a Difference - Stats on how well the detector is working. How many times have people called out some bullshit today on Facebook and other social media sites? What are the trends? Are people making a difference that we can measure?

Components
----------

* Mirror of rumor mills - Routinely collected headlines, URLs, results and descriptions from fact checking sites. Extract keywords and store all of it in MongoDB.

* Cache of matched URLs - A lookup table of URLs that the Bullshit Detector has already matched with identified falsehoods. Includes the URL of the misleading article, URL of investigation,

* Matching Engine - OpenNLP plagiarism schemes should work, for one thing. Takes a post/story and tries to match it with known false or misleading stories. Uses cache first, then NLP approaches. If it finds a match, the post id and relevant data points are recorded.

* Facebook Integrations
 * Basic application code
 * the pages above
 * API code to retrieve feed
 * Badges, etc..

Fact Check Sites
-----------------
* Snopes - http://www.snopes.com/info/whatsnew.xml
* Truth or Fiction - http://truthorfiction.com/feed/
* PolitiFact - http://politifact.org/feeds/statements/truth-o-meter/
* Fact Check - http://www.factcheck.org/feed/

Suggestions?
------------

Have a great idea? Want to help? Email me at gregory dot jansen at gmail dot com.
