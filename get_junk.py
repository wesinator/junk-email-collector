#!/usr/bin/env python
import config
from datetime import date
import outlook

def get_junk(email_account, password):
    mail = outlook.Outlook()
    mail.login(email_account, password)
    mail.junk()
    
    unread_ids = mail.unreadIds()
    for email_id in unread_ids:
        if email_id != b'':
            msg = mail.getEmail(email_id)
            with open("Junk/%s_%s.eml" % (date.today(), msg["subject"]), "wb") as eml:
                eml.write(msg.as_string())
                
                print(msg["Date"])
                print(msg["subject"])

get_junk(config.email, config.password)
