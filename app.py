from flask import Flask, render_template, request
application = Flask(__name__)

# Ensure responses aren't cached
@application.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@application.route('/')
def hello_world():
    return render_template("index.html")

@application.route('/day/<int:num>')
def project(num):
  return render_template("/days/" + str(num) + ".html")

if __name__ == '__main__':
    application.run()
