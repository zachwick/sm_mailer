import smtplib
from email import encoders
from email.message import Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''
The lines below are automatically truncated after the '=' character in order
to not provide you all with my email credentials.

See lines 38 - 45 for the blank out implementation
'''
user = "XXXXXXXXXXXXXXX" #blank
pswd = "XXXXXXXXXXXXXXX" #blank
addr = "XXXXXXXXXXXXXXX" #blank
host = "XXXXXXXXXXXXXXX" #blank

def unicode_stringify(msg_str):
    stringified_unicode = ""
    for char in msg_str:
        stringified_unicode += str(ord(char))
    return stringified_unicode

def main():
    # Construct the outer multipart-mime message
    outer_mail = MIMEMultipart()
    outer_mail['Subject'] = 'Senior Software Engineer Position'
    outer_mail['To'] = unicode_stringify('hiring')+"@smartgift.it"
    outer_mail['From'] = addr

    # Construct the resume text file attachment
    resume = open('wick_resume.txt','r')
    msg = MIMEText(resume.read(), _subtype='plain')
    msg.add_header('Content-Disposition', 'attachment', filename='wick_resume.txt')
    resume.close()
    # Attach the resume attachment to the outer_mail envelope
    outer_mail.attach(msg)

    # Sanitize this code for others' eyes
    sg_mailer = open('sg_mailer.py','r')
    sg_sanitized = open('sg_sanitized.py','w')
    for line in sg_mailer.readlines():
        if '#blank' in line:
            line =  line[0:7] + "________" + line[-6:]
        sg_sanitized.write(line)
    sg_sanitized.close()

    # Construct the sg_mailer.py file attachment
    sg_attach = open('sg_sanitized.py','r')
    sg_msg = MIMEText(sg_attach.read(), _subtype='plain')
    sg_msg.add_header('Content-Disposition','attachment',filename='sg_sanitized.py')
    sg_attach.close()
    # Attach the sg_sanitized.py attachment to the outer_mail envelope
    outer_mail.attach(sg_msg)

    # Construct the body of the outer_mail envelope
    body = "Hello,\nI would like to submit myself as a candidate for the Senior Software Engineer position with SmartGift.\nI have the experience that is sought, and have written software for all parts of the software spectrum - embedded systems, desktop apps, web apps, and web APIs. Notably, I have written REST APIs that are used by millions of users (Copy.com while at Barracuda Networks) and REST APIs that handle wireless sensor nodes sending data at very fast rates.\n\nOn HackerNews, a coding challenge was issued, the result of which was the email address of where applicants should apply. That challenge is 3-4 lines in python, so instead, I wrote a simple python script that when run will generate this entire email, attach my resume, expunge my personal email credentials from itself, attach itself to the email, and send the email.\n\nMy Github account (https://github.com/zachwick) and my personal site (https://zachwick.com) have more examples of my work and a little bit more about me.\n\nI would love to chat with you all more about how can fit into the SmartGift team, and I look forward to hearing back from you.\n\n-zach"
    body_msg = MIMEText(body)
    outer_mail.attach(body_msg)

    # Finally send the message
    smtp_client = smtplib.SMTP(host)
    smtp_client.starttls()
    smtp_client.login(user,pswd)

    smtp_client.sendmail(addr, outer_mail['To'], outer_mail.as_string())
    smtp_client.quit()
    
if __name__ == "__main__":
    main()
    
    
