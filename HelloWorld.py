from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route("/")
def hello_world():
	return "hello world vishwanath manvi"

try:
	@app.route("/hello/<search_query>")

	def hello(search_query):
		return search_query

	@app.route("/test/<int:value>")

	def intRoute(value):
		print(value + 1)
		return "correct",200


except(Exception):
	print("Exception occured")
	print (Exception.with_traceback())

app.run()

