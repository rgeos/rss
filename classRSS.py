#!/usr/bin/env python
# _*_coding: utf-8 _*_

import feedparser as rss
import classRegex as reg


class classRSS(object):
	"""
	Retrieving some of the elements of an RSS feed
	"""

	def __init__(self):
		self.urls = ""                  # the URLs will be in a string
		self.feed = {}                  # a dictionary of feeds
		self.remove = reg.classRegex()  # regex to remove from string

	def setURLs(self, newURLs):
		"""
		This function will set the RSS URLs in the
		form of a string delimited by space
		:param newURLs: String
		:return:        String
		"""
		self.urls = newURLs


	def getURLs(self):
		"""
		A list of URLs formed by splitting a string on spaces
		:return:    List
		"""
		return [x.strip() for x in self.urls.split(" ")]


	def getFeeds(self):
		"""
		This function will return a dictionary of RSS feeds
		:return:    Dictionary
		"""
		for i in range(len(self.getURLs())):
			self.feed[i] = rss.parse(self.getURLs()[i])

		return self.feed


	def getFeed(self, feedId):
		"""
		Providing an ID, retrieve a feed with that ID
		:param feedId:  Integer
		:return:        String
		"""
		try:
			return self.getFeeds()[feedId]
		except Exception:
			return "The ID %r doesn't exist." % feedId


	def getFeedTitle(self, feedId):
		"""
		Providing an ID, retrieve the title of a feed with that ID
		:param feedId:  Integer
		:return:        String
		"""
		try:
			return self.remove.getRegex(self.getFeed(feedId=feedId).feed.title)
		except Exception:
			return "The ID %r doesn't exist." % feedId


	def getFeedLink(self, feedId):
		"""
		Providing an ID, retrieve the link of a feed with that ID
		:param feedId:  Integer
		:return:        String
		"""
		try:
			return self.getFeed(feedId=feedId).feed.link
		except Exception:
			return "The ID %r doesn't exist." % feedId


	def getFeedSubtitle(self, feedId):
		"""
		Providing an ID, retrieve the subtitle of a feed with that ID
		:param feedId:  Integer
		:return:        String
		"""
		try:
			return self.remove.getRegex(self.getFeed(feedId=feedId).feed.subtitle)
		except Exception:
			return "The ID %r doesn't exist." % feedId


	def getFeedLen(self, feedId):
		"""
		Providing an ID, retireve the length of a feed with that ID
		:param feedId:  Integer
		:return:        String
		"""
		try:
			return len(self.getFeed(feedId=feedId).entries)
		except Exception:
			return "The ID %r doesn't exist." % feedId

	def getFeedDatas(self, feedId):
		"""
		Retrieve all entries in a feed
		:param feedId:  Integer
		:return:        String
		"""
		try:
			return self.getFeed(feedId=feedId).entries
		except Exception:
			return "The ID %r doesn't exist." % feedId

	def getFeedData(self, feedId, entryId):
		"""
		This will return the summary and the title of a feed
		At the same time it will remove the regex from the contets
		:param feedId:  Integer
		:param entryId: Integer
		:return:        List
		"""
		try:
			title   = self.remove.getRegex(self.getFeedDatas(feedId=feedId)[entryId].title)
			summary = self.remove.getRegex(self.getFeedDatas(feedId=feedId)[entryId].summary)
			return [title, summary]
		except Exception:
			return "The ID %r, %r doesn't exist." % (feedId, entryId)



