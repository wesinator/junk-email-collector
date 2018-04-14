#!/usr/bin/env python2
import config
from datetime import date
import outlook

mail = outlook.Outlook()
mail.login(config.outlook_email,config.outlook_password)
mail.junk()

unread_ids = mail.unreadIds()
for email_id in unread_ids:
    if email_id != '':
        with open("Junk/%s_%s.eml" % (date.today(), email_id), "wb") as eml:
            #print(mail.getEmail(email_id)["Date"])
            eml.write(mail.getEmail(email_id).as_string())
