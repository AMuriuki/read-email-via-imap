import imaplib
import email
from email.header import decode_header
import webbrowser
import os
from decouple import config

# account credentials
username = config('username')
password = config('password')

# outlook IMAP server
imap_server = "outlook.office365.com"

# create an IMAP4 CLASS with SSL
imap = imaplib.IMAP4_SSL(imap_server)

# authenticate
imap.login(username, password)

status, messages = imap.select("INBOX")

print(status, messages)
