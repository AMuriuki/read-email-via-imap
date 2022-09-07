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
imap_server = config('imap_server')

# create an IMAP4 CLASS with SSL
imap = imaplib.IMAP4_SSL(imap_server)

# authenticate
imap.login(username, password)

# select INBOX mailbox
status, messages = imap.select("INBOX")

# to see available mailboxes
# imap.list()

# determine number of top emails to fetch
N = 10

# total number of emails
messages = int(messages[0])


def clean(text):
    # create folder name from subject without spaces
    return "".join(c if c.isalnum() else "_" for c in text)


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

            if isinstance(From, bytes):
                From = From.decode(encoding)

            print("Subject", subject)
            print("From", From)

            # if msg is multipart
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # print text/plain emails and skip attachments
                        print(body)
                    elif "attachment" in content_disposition:
                        # download attachment
                        filename = part.get_filename()
                        if filename:
                            folder_name = clean(subject)
                            if not os.path.isdir(folder_name):
                                # make a folder for this email (named from subject)
                                os.mkdir(folder_name)
                            filepath = os.path.join(folder_name, filename)

                            # download attachment and save it
                            open(filepath, 'wb').write(
                                part.get_payload(decode=True))
                    else:
                        # extract content type of email
                        content_type = msg.get_content_type()
                        # get email body
                        body = msg.get_payload(decode=True)

                        if content_type == "text/plain":
                            # print text email
                            print(body)
                    if content_type == "text/html":
                        # create HTML file and open in browser
                        folder_name = clean(subject)
                        if not os.path.isdir(folder_name):
                            os.mkdir(folder_name)
                        filename = "index.html"
                        filepath = os.path.join(folder_name, filename)

                        # write the file
                        open(filepath, "w").write(body)

                        # open in default browser
                        webbrowser.open(filepath)
                    print("="*100)


# close connection and logout
imap.close()
imap.logout()
