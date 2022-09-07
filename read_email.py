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

# select INBOX mailbox
status, messages = imap.select("INBOX")

# to see available mailboxes
# imap.list()

# determine number of top emails to fetch
N = 3

# total number of emails
messages = int(messages[0])

# loop over each email message
for i in range(messages, messages-N, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse the bytes email into an email object
            msg = email.message_from_bytes(response[1])

            # decode the email subject
            subject, encoding = decode_header(msg['Subject'])[0]

            if isinstance(subject, bytes):
                # if bytes decode to str
                subject = subject.decode(encoding)

            # decode email sender
            From, encoding = decode_header(msg.get("From"))[0]

            print(subject, From)
