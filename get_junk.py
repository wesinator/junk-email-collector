#!/usr/bin/env python
import config
from datetime import date
import hashlib
import outlook

def get_junk(email_account, password):
    mail = outlook.Outlook()
    mail.login(email_account, password)
    mail.junk()
    
    unread_ids = mail.unreadIds()
    for email_id in unread_ids:
        if email_id != b'':
            msg = mail.getEmail(str(email_id))
            msg_data = msg.as_string()
            
            with open(config.junk_folder + "/%s.eml" % hashlib.sha256(msg_data).hexdigest(), "wb") as eml:
                eml.write(msg_data)
                
                print(msg["Date"])
                print(msg["subject"] + "\n")

get_junk(config.email, config.password)
