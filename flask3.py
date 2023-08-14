# # importing libraries
# from flask import Flask
# from flask_mail import Mail, Message

# app = Flask(__name__)
# mail = Mail(app) # instantiate the mail class

# # configuration of mail
# app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
# app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT'))
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
# app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', False) in ['True', 'true', '1']
# app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL', False) in ['True', 'true', '1']




# mail = Mail(app)

# # message object mapped to a particular URL ‘/’
# @app.route("/")
# def index():
#     msg = Message(
#                     'Hello',
#                     sender ='rosepear9@gmail.com',
#                     recipients = ['sijanthpa@gmail.com']
#                 )
#     msg.body = 'Hello Flask message sent from Flask-Mail'
#     mail.send(msg)
#     return 'Sent'

# if __name__ == '__main__':
#     app.run(debug = True)
