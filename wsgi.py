# sudo apt-get update && sudo apt-get install libgl1
# pip freeze > requirements.txt
# pip install -r requirements.txt
# gunicorn --bind 0.0.0.0:5000 wsgi:app
# python wsgi.py
# python -m flask run

from app import app

if __name__ == "__main__":
    app.run()