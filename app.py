from flask import Flask, render_template, request
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/day/<int:num>')
def project(num):
  return render_template("/days/1.html")

if __name__ == '__main__':
    app.run()
