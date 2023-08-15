# importing libraries
import os
from flask import Flask ,render_template,request, redirect
from flask_mail import Mail, Message

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
        recipient_email =  os.getenv('RECIPIENT_USERNAME')
        
        data = request.form
        name = data.get('name')
        email = data.get('email')
        cust_message=data.get('cust_message')
        subject = 'Response from ContactUs Page'
        sender_email = os.getenv('MAIL_USERNAME')

        message = Message(subject, sender=sender_email, recipients=[recipient_email])
        message.html = render_template('email_template.html', cust_name=name,cust_email=email,cust_message=cust_message)

        try:
            mail.send(message)
            return 'Email sent successfully!'
        except Exception as e:
            return str(e)
    else:
        return render_template('index.html')
    


if __name__ == '__main__':
    app.run(debug = True)
