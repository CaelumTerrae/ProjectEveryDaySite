from flask import Flask, render_template, request
application = Flask(__name__)
numPages = 3 #update this daily, and change this to be a request to database when that is set up

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
  return render_template("/days/" + str(num) + ".html",num=num,numPages=numPages)

if __name__ == '__main__':
    application.run()
