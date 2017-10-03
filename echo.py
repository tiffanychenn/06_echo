from flask import Flask, render_template, request

jinjas_in_the_night = Flask(__name__)

@jinjas_in_the_night.route("/", methods = ["GET", "POST"])
def root():
	return render_template("base.html")

@jinjas_in_the_night.route("/echoed", methods = ["GET", "POST"])
def echoed():
	return render_template("echoed.html", user = request.form["user"], method = request.method, message = request.form["message"])
	
if __name__ == "__main__":
	jinjas_in_the_night.debug = True
	jinjas_in_the_night.run()