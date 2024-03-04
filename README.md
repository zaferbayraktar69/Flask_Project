
# Start rabbitMq
## sudo rabbitmq-server
<img width="1097" alt="Ekran Resmi 2024-03-01 17 07 06" src="https://github.com/PISAGOOR/Flask_Project/assets/60022825/4f0bf8aa-f0ff-4553-bc3e-3d3dff4fa607">

# 1 Terminal
## python main.py
<img width="1680" alt="Ekran Resmi 2024-03-01 17 01 40" src="https://github.com/PISAGOOR/Flask_Project/assets/60022825/989e4516-a506-4764-99e3-880298d9b38d">
-------------------

# 2 Terminal
## celery -A main.celery worker --loglevel=info
<img width="1680" alt="Ekran Resmi 2024-03-01 17 02 48" src="https://github.com/PISAGOOR/Flask_Project/assets/60022825/f14c0e36-c4b9-4db0-8d7f-5ae7d18e8071">
-------------------

# 3 Terminal
## celery -A main.celery beat --loglevel=info
<img width="1680" alt="Ekran Resmi 2024-03-01 17 03 32" src="https://github.com/PISAGOOR/Flask_Project/assets/60022825/0e66ac0f-491c-4296-951b-a7a6f315d926">
-------------------



