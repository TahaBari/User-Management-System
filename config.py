import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    # Explicitly use PyMySQL
    db_url = os.environ.get('DATABASE_URL')
    if db_url and 'mysql:' in db_url and 'pymysql' not in db_url:
        db_url = db_url.replace('mysql:', 'mysql+pymysql:')
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False 