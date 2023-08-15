# importing libraries
import os
from flask import Flask ,render_template,request, redirect
from flask_mail import Mail, Message
from app import app, mail

app = Flask(__name__)
mail = Mail(app) # instantiate the mail class

#configuration of mail
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', False) in ['True', 'true', '1']
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', False) in ['True', 'true', '1']








mail = Mail(app)

# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/send_email',methods=['GET','POST'])
def send_email():
    if request.method=='POST':
        recipient_email = 'tesewa9275@v1zw.com'
        recipient_name = 'Recipient Name'
        data = request.form
        name = data.get('name')
        email = data.get('email')
        subject = 'Your Subject Here'
        sender_email = app.config('MAIL_USERNAME')

        message = Message(subject, sender=sender_email, recipients=[recipient_email])
        message.html = render_template('email_template.html', cust_name=name,cust_email=email,message=message)

        try:
            mail.send(message)
            return 'Email sent successfully!'
        except Exception as e:
            return str(e)
    else:
        return render_template('index.html')
    
@app.route("/send",methods=['GET','POST'])   
def send():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        email = data.get('email')
        message=data.get('message')
        # Do something with the received data
        print(f"Received data: Name={name}, Email={email},Message={message}")
        # msg = Message(
        #                 'Response Got',
        #                 sender ='rosepear9@gmail.com',
        #                 recipients = ['tesewa9275@v1zw.com']
        #             )
        # msg.body = 'Hello Flask message sent from Flask-Mail'
        # mail.send(msg)
        return 'Sent'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
