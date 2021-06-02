from flask import Flask
from db import db_session, init_db
from model import TestTable

init_db()