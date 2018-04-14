#!/usr/bin/env python3
import config
from datetime import date
import outlook

mail = outlook.Outlook()
mail.login(config.outlook_email,config.outlook_password)
mail.junk()

unread_ids = mail.unreadIds()
print(unread_ids)

for email_id in unread_ids:
    if unread_ids[0] != '':
        with open("Junk/%s_%s.eml" % (date.today(), email_id), "wb") as eml:
            #print(mail.getEmail(email_id)["Date"])
            eml.write(mail.getEmail(email_id).as_string())
