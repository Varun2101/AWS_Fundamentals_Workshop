from flask import Flask, render_template, request
application = Flask(__name__)
defText = "Input will be truncated to 100 characters..."

@application.route("/", methods=['GET'])
def home():
	return render_template("home.html", occurrences=0, defText=defText, defKey=defText)

@application.route("/", methods=['GET', 'POST'])
def countOccurrences():
	text = request.form["text"]
	key = request.form["key"]
	text = text[:100]
	key = key[:100]
	if text == "" or key == "":
		occ = 0
	else:
		occ = text.count(key)
	return render_template("home.html", occurrences=occ, defText=text, defKey=key)

if __name__ == '__main__':
	application.run(debug=True)
