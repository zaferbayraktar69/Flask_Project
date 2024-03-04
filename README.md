
# Start rabbitMq
## sudo rabbitmq-server
<img width="1097" alt="Ekran Resmi 2024-03-04 09 59 40" src="https://github.com/zaferbayraktar69/Flask_Project/assets/60022825/6781d388-fd8a-4b76-baba-93aaae49dd15">


# 1 Terminal
## python main.py
<img width="968" alt="Ekran Resmi 2024-03-04 10 01 29" src="https://github.com/zaferbayraktar69/Flask_Project/assets/60022825/0a6ceeb5-419c-4f4d-a500-a0dfe51977b3">



# 2 Terminal
## celery -A main.celery worker --loglevel=info
<img width="1185" alt="Ekran Resmi 2024-03-04 10 02 37" src="https://github.com/zaferbayraktar69/Flask_Project/assets/60022825/5292d055-127e-443e-bcfb-5870e471dede">



# 3 Terminal
## celery -A main.celery beat --loglevel=info
<img width="1185" alt="Ekran Resmi 2024-03-04 10 03 06" src="https://github.com/zaferbayraktar69/Flask_Project/assets/60022825/b99cf1e9-ca44-41ea-8c14-7527a281cbae">


# RabbitMq Admin Panel
## http://localhost:15672/#/
<img width="1555" alt="Ekran Resmi 2024-03-04 10 04 12" src="https://github.com/zaferbayraktar69/Flask_Project/assets/60022825/5507df8a-28a2-446d-8dd5-e87ca33461af">
