
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import random
import string

app = Flask(__name__)

# Cấu hình server email
app.config['MAIL_SERVER'] = 'smtp.yourdomain.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@yourdomain.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

mail = Mail(app)

# Tạo email tạm thời
@app.route('/create_email', methods=['POST'])
def create_email():
    domain = request.json.get('domain')
    if not domain:
        return jsonify({'error': 'Domain is required'}), 400

    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email = f"{local_part}@{domain}"
    return jsonify({'email': email})

# Gửi email
@app.route('/send_email', methods=['POST'])
def send_email():
    to_email = request.json.get('to_email')
    subject = request.json.get('subject')
    body = request.json.get('body')

    if not to_email or not subject or not body:
        return jsonify({'error': 'to_email, subject, and body are required'}), 400

    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[to_email])
    msg.body = body
    mail.send(msg)
    return jsonify({'message': 'Email sent successfully'})

if __name__ == '__main__':
    app.run(port=5000)
