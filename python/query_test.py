from tkinter.filedialog import askopenfilename
import sqlite3
from sqlite3 import Error
import sys
from python import database_creator as dbc
from twilio.rest import Client
conn = dbc.return_conn()
#dbc.delete_all_tasks(conn)
#user = ('Aidan', 'aidanhill61@gmail.com', '4123289513')
#dbc.insert_test(conn, user)

phone = dbc.select_phone_users(conn)
print(phone)


# account_sid = "ACc6043bec84ced717253f054fc93af5ec"
# # Your Auth Token from twilio.com/console
# auth_token = "c274a27ddb3b13a9d6cb1dc80ccd3d9a"
#
# client = Client(account_sid, auth_token)
# phone = dbc.select_phone_users(conn)
# phone = ''.join(str(phone))
# phone = phone.strip('(')
# phone = phone.strip(')')
# phone = phone.strip(',')
# print(phone)
# message = client.messages.create(
#     to=phone,
#     from_="+15595138433",
#     body="Unknown user is in feed, check computer for image.")
#
# print(message.sid)
sys.exit()
#filename = askopenfilename()
