from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import pymongo
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

ATLAS_URI = os.getenv("ATLAS_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = pymongo.MongoClient(ATLAS_URI, tls=True,
                             tlsAllowInvalidCertificates=True)
db = client.test
collection = db[COLLECTION_NAME]

from app import routes