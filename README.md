# Read your emails programmatically
A handy tool that reads your emails and automatically download attachments. 

The tool uses [imaplib](https://docs.python.org/3/library/imaplib.html) module to list and read your emails using python via **IMAP protocol**

## Getting Started
Make sure you have python installed locally

1. Clone repo && cd into `read-email-via-imap`
```
git clone https://github.com/AMuriuki/read-email-via-imap.git

cd read-email-via-imap
```

2. Create virtual env & activate it (optional)
```
python3 -m venv venv

. venv/bin/activate
```

3. Install requirements
```
pip install -r requirements.txt
```

4. Create a .env file in the root of the directory (or edit `env.example`)

```
username="your email"
password="your password"

# https://www.systoolsgroup.com/imap/ for your provider's IMAP server address

imap_server="your email provider IMAP's server"
```
>NB:  *From May 30, 2022, ​​Google no longer supports the use of third-party apps or devices which ask you to sign in to your Google Account using only your username and password. Therefore, this code won't work for Gmail accounts. If you want to interact with your Gmail account in Python, check out this [repo](https://github.com/AMuriuki/gmail-api-python).*






