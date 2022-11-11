from decouple import config

#https://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python

print('DB_HOST : {HOST}, DB_NAME : {DB_NAME}, DB_USER : {DB_USER}, DB_PASSWORD : {PASSWORD}.'.format(
      HOST = config('DB_HOST'),
      DB_NAME = config('DB_NAME'),
      DB_USER = config('DB_USERNAME'),
      PASSWORD = config('DB_PASSWORD')
    )
)



