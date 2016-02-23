#!/usr/bin/env python
# _*_coding: utf-8 _*_


class classSave(object):
	"""
	Saving data to file
	"""

	def __init__(self):
		self.filename = "rss.txt"   # by default the filename


	def setName(self, newName):
		"""
		Set the name of the file
		:param newName: String
		:return:        String
		"""
		self.filename = newName

	def getName(self):
		"""
		Retrieve the name of the file
		:return:    String
		"""
		return self.filename

	def getFile(self, data):
		"""
		Write the data to file
		:param data:    String
		:return:        Object
		"""
		with open(self.getName(), "w") as f:
			f.write(data.encode('utf-8'))