#!/usr/bin/env python

from flask import Flask, request, render_template, redirect, url_for, flash

from classForms import RssValidation as rv

app = Flask(__name__)


@app.route("/")
def index():
	"""
	Welcoming page
	:return:    page template
	"""
	return render_template("index.html")

@app.route("/service")
def service():
	form = rv(csrf_enabled=False)

	if request.method == "POST" and form.validate():
		flash("It works")
		return render_template("index.html", form=form)

	return render_template("index.html", form=form)


@app.route("/about_en")
def about_en():
	"""
	Details about the project - English page
	:return:    page template
	"""
	return render_template("about_en.html")


@app.route("/about_jp")
def about_jp():
	"""
	Details about the project - Japanese page
	:return:    page template
	"""
	return render_template("about_jp.html")

if __name__ == "__main__":
	app.run(debug=True, port=9999)
