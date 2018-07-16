#!/usr/bin/env python
import config
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
            sha256 = hashlib.sha256(msg_data).hexdigest()
            
            with open(config.junk_folder + "/%s.eml" % sha256, "wb") as eml:
                eml.write(msg_data)
                
                print("\n" + msg["Date"])
                print(msg["Subject"])
                print(sha256)

get_junk(config.email, config.password)
