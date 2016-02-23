#!/usr/bin/env python
# _*_coding: utf-8 _*_

import simplejson as js

class classSave(object):
	"""
	Saving data in
	"""

	def __init__(self):
		self.filename = "rss.txt"


	def setName(self, newName):
		"""

		:param newName:
		:return:
		"""
		self.filename = newName

	def getName(self):
		"""

		:return:
		"""
		return self.filename

	def getFile(self, data):
		"""

		:rtype: object
		:param data:
		:return:
		"""
		with open(self.getName(), "w") as f:
			js.dump(data, f)