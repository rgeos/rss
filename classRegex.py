#!/usr/bin/env python
# _*_coding: utf-8 _*_

import re


class classRegex(object):
	"""
	Regular expressions
	"""

	def __init__(self):
		self.string = ""
		self.reg = "NewsPicks"  # by default we will set the regex


	def setString(self, newString):
		"""
		Set a string to apply regex on
		:param newString:   String
		:return:            String
		"""
		self.string = newString


	def setRegex(self, newRegex):
		"""
		Set a regular expression, other than the one above
		:param newRegex:    String
		:return:            String
		"""
		self.reg = newRegex


	def getString(self):
		"""
		Retrieve the string
		:return:    String
		"""
		return self.string

	def getRegex(self, string):
		"""
		This function will return a string with each occurrence of the regex removed
		:param string:  String
		:return:        String
		"""
		regex = re.compile(self.reg)
		return regex.sub("", string)
