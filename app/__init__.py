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
@app.route("/send",methods=['POST'])   
def send():
    if request.method == 'POST':
        msg = Message(
                        'Response Got',
                        sender ='rosepear9@gmail.com',
                        recipients = ['sijanthpa@gmail.com']
                    )
        msg.body = 'Hello Flask message sent from Flask-Mail'
        mail.send(msg)
        return 'Sent'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
