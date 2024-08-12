python app.py

# Production 에서는 Gunicorn으로 실행시킬 수 있어요.
# gunicorn -w 4 -b 0.0.0.0:5000 app:app