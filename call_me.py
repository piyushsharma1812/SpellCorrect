from flask import Flask,redirect, url_for, request,jsonify
app=Flask(__name__)
import GrammerChecker,Missspelled
import json

@app.route("/")
def hello():
	return "Hello"

@app.route("/spellCorrect")
def spellcheck():
	word = request.args.get('word')
	#d = GrammerChecker.proper_word(word)
	d=Missspelled.regexTester(word)
	return jsonify(d)

if __name__ == '__main__':
	app.run(debug=True)
