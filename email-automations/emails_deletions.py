"""
IMAP

pip install imapclient
"""

import imaplib

imap_obj = imaplib.IMAP4_SSL('imap.gmail.com', 993)

# or

# from imapclient import IMAPClient

# imap_obj = IMAPClient('imap.mailserver.com', use_uuid=True, ssl=True)

# or

import imaplib

# enter your e-mail adress
username = input('Enter your e-mail: ')

# Enter your password
password = input('Enter your password: ')

# Login to the IMAP Server with the entered information
imapobj = (username, password)

# Once logged in, select the box you'd e-mails from
imap_obj.login(username, password)
imap_obj.select('Spam')

# You may search the specific e-mails based on the "From" or "Subject"
result, message = imap_obj.search(None, 'FROM "any_invalid@email.com"')
result, message = imap_obj.search(None, 'SUBJECT "This is a SPAM Subject"')

# To delete all the content inside a certain box, "Spam" for example
result, message = imap_obj.search(None, "All")

# Close the mailbox once you finished
imap_obj.close()

# Log out
imap_obj.logout()