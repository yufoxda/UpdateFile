from database.schema import Book,Song,Lyricist,SongWriter,Arranger
from database.schema import SongLyricistAssociation,SongWriterAssociation,SongArrangerAssociation

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the app
app = Flask(__name__, template_folder="../page/template",static_folder="../page/static")
import os
db_path = os.path.join(os.getcwd(), 'Database/ompooscores.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

per_page = 30

import api.roote