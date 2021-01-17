from flask import Flask, render_template, request

# Note: for deploying to Elastic Beanstalk, Flask app must be named "application"
application = Flask(__name__)

defText1 = "Input will be truncated to 1000 characters..."
defText2 = "Input will be truncated to 100 characters..."

# Initial display when no text has been typed.
# Get request so that default text can be displayed
@application.route("/", methods=['GET'])
def home():
	return render_template("home.html", occurrences=0, defText=defText1, defKey=defText2)

# Switches to this route when a post request is made
# Get request still needed to display results and keep the input text unchanged on reload
@application.route("/", methods=['GET', 'POST'])
def countOccurrences():
	text = request.form["text"]
	key = request.form["key"]
	# truncating inputs to prevent maliciously long inputs that require large amounts of computation
	text = text[:1000]
	key = key[:100]
	if text == "" or key == "":
		occ = 0
	else:
		occ = text.count(key)
	return render_template("home.html", occurrences=occ, defText=text, defKey=key)

# Note: the .py file containing the main function (and entrypoint to the app) must be called "application.py"
if __name__ == '__main__':
	application.debug = True  # remember to comment this out before deploying on production server
	application.run()
