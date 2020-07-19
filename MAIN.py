import email
import imaplib
import webbrowser

# GMAIL USER AND PASS
user = ''
password = ''

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(user, password)

mail.select("INBOX")

result, data = mail.uid('search', None, 'ALL')
inbox = data[0].split()

newest = inbox[-1]  # LATEST MAIL
oldest = inbox[0]  # OLDEST MAIL

r2, new = mail.uid('fetch', newest, '(RFC822)')
r3, old = mail.uid('fetch', oldest, '(RFC822)')

raw_mail = new[0][1].decode("utf-8")
message = email.message_from_string(raw_mail)

counter = 1
found = False
print(message['From'])
print(message['To'])
print(message['Subject'])
for part in message.walk():
    if part.get_content_maintype() == "multipart":
        continue
    filename = part.get_filename()
    if not filename:
        ext = '.html'
        filename = 'msg-part-%08d%s' % (counter, ext)
    counter += 1
    ct = part.get_payload()
    print("--------------------", ("meet.google.com" in ct), ct.find("meet.google.com"), "---------------------")
    lst = []
    str = ' '
    str = (ct[ct.find("meet.google.com"):ct.find("meet.google.com") + 28]) + str
    print(ct)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    if "meet.google.com" in ct:
        found = True

print(str)

if found:
    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(str)
else:
    print("NOT FOUND")
