

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from celery.schedules import crontab
from pymongo import MongoClient
from celery import Celery
import smtplib


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




app = Flask(__name__)

# MongoDB bağlantısı
client = MongoClient('mongodb://localhost:27017/')
db = client['usersFlask']  # MongoDB veritabanı adı

# JWT ayarları
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # JWT için gizli anahtar
jwt = JWTManager(app)

# Örnek veri modeli
class UserModel:
    def __init__(self, name, email):
        self.name = name
        self.email = email

app.config['CELERY_BROKER_URL'] = 'amqp://guest:guest@localhost:5672//'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])

celery.conf.beat_schedule = {
    'send-email-every-minute': {
        'task': 'send_email_task', # Fonksiyon adı düzeltildi
        'schedule': crontab(minute="*/1"),
    },
}


# Kullanıcı girişi endpoint'i
@app.route('/login', methods=['POST'])
def login():
    name = request.json.get('name', None)
    email = request.json.get('email', None)

    # JWT oluştur ve geri dön
    access_token = create_access_token(identity=name)
    return jsonify(access_token=access_token), 200

# Yeni kullanıcı ekleme endpoint'i
@app.route('/api/add', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if name and email:
        new_user = UserModel(name, email).__dict__
        db.users.insert_one(new_user)
        return jsonify({'message': 'Kullanıcı eklendi'}), 201
    else:
        return jsonify({'message': 'Geçersiz istek'}), 400

# Kullanıcıyı silen endpoint
@app.route('/api/delete/<name>', methods=['DELETE'])
def delete_user(name):
    db.users.delete_one({'name': name})
    return jsonify({'message': 'Kullanıcı silindi'}), 200

# Tüm kullanıcıları getiren endpoint
@app.route('/api/all', methods=['GET'])
def get_all_users():
    
    users = []
    for user in db.users.find():
        users.append({'_id': str(user['_id']), 'name': user['name'], 'email': user['email']})
    return jsonify(users), 200

# Arka plan görevi: Her 1 dakikada bir e-posta atan fonksiyon
@celery.task(name='send_email_task')  # Fonksiyon adı düzeltildi
def send_email_task():
    users = db.users.find()

    for user in users :
        print(user['email'], "subject", "şimdiki mesaj" )
        send_email(user['email'], 'Subject', 'Message')

    return 'send_email_task() Mail gönderildi'




def send_email(email, subject, message):

    sender_email = 'Your Mail Address'
    password = 'Password'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, email, text)
        print(f"E-posta gönderildi: {email}, Konu: {subject}, İçerik: {message}")
    except Exception as e:
        print(f"E-posta gönderilirken hata oluştu: {e}")
    finally:
        server.quit()


# def send_Message( message):
#     # Telegram botunuzun API anahtarını buraya girin
#     telegram_api =  "Your Telegram api "
#     chat_id =  "-Your Chat İD"
    
#     requests.post(url=telegram_api,data={"chat_id":chat_id,"text":str(message),"parse_mode": "HTML"}).json()

#     print(f"send_email() mesaj gönderildi: {message}")



if __name__ == "__main__":
    app.run(debug=True)
