from flask import Flask, render_template, request
from secrets import emailsecret
from flask_mail import Message, Mail

mail = Mail()

application = Flask(__name__)

application.config["MAIL_SERVER"] = "smtp.gmail.com"
application.config["MAIL_PORT"] = 465
application.config["MAIL_USE_SSL"] = True
application.config["MAIL_USERNAME"] = emailsecret["username"]
application.config["MAIL_PASSWORD"] = emailsecret["password"]

mail.init_app(application)

numPages = 6 #update this daily, and change this to be a request to database when that is set up

# Ensure responses aren't cached
@application.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@application.route('/',methods=['POST','GET'])
def hello_world():
  if request.method =='GET':
    return render_template("index.html")
  else:
    contact = {
      "name": request.form["name"],
      "email": request.form["email"],
      "subject": request.form["subject"],
      "message": request.form["message"]
    }
    if contact["name"] and contact["email"] and contact["subject"] and contact["message"]:
      subject = "New Project Every Day: " + contact["subject"]
      msg = Message(subject, sender=emailsecret["username"], recipients=[emailsecret["username"]])
      msg.body = """
      Message from New Project Every Day!
      From: %s <%s>
      %s
      """ % (contact["name"], contact["email"], contact["message"])
      mail.send(msg)
      return render_template("index.html",success=True,returnAddress="contact")
    else:
      messages = ["Missing fields!"]
      return render_template("index.html", messages=messages, returnAddress="contact")

@application.route('/day/<int:num>')
def project(num):
  return render_template("/days/" + str(num) + ".html",num=num,numPages=numPages)

if __name__ == '__main__':
    application.run()
