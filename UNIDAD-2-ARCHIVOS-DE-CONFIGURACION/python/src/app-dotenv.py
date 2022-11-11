import os
from dotenv import load_dotenv, find_dotenv
load_dotenv (find_dotenv())

#https://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python

print('DB_HOST : {HOST}, DB_NAME : {DB_NAME}, DB_USER : {DB_USER}, DB_PASSWORD : {PASSWORD}.'.format(
      HOST = os.getenv('DB_HOST'),
      DB_NAME = os.getenv('DB_NAME'),
      DB_USER = os.getenv('DB_USERNAME'),
      PASSWORD = os.getenv('DB_PASSWORD')
    )
)



