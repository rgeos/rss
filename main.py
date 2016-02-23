#!/usr/bin/env python
# _*_coding: utf-8 _*_

import classRSS as feed
import classSave as sav

rss = feed.classRSS()
save = sav.classSave()

# string with URLs separated by space
# urls = "http://tech.uzabase.com/rss"

urls = "http://tech.uzabase.com/rss " \
       "http://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml " \
       "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml " \
       "http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml " \
       "http://rss.nytimes.com/services/xml/rss/nyt/Science.xml"


# setting up the URLs
rss.setURLs(urls)

# dictionary of feeds
# {0:{feed0}, 1:{feed1}}
# rss.getFeeds()

# the whole data
data = [rss.getFeedData(i, u) for i in xrange(rss.getFeedsLen()) for u in xrange(rss.getFeedLen(i))]

# print data

# feed index 0, news index 2, summary
# data = rss.getFeedData(0, 2)[1]

# save the data to file
save.getFile(data=data)
