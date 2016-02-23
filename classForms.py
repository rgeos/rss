#!/usr/bin/env python

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import Form


class RssValidation(Form):
	"""
	GUI forms
	Part of the Flask framework
	"""

	rss     = StringField('RSS feeds', validators=[DataRequired("Please enter at least one RSS address")])
	regex   = StringField('Regex')
	submit  = SubmitField('Run')
