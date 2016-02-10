import smtplib

fromaddr = 'info3180.justenmorgan@gmail.com'

fromname = "Justen Morgan"

toaddr  = 'info3180.justenmorgan@gmail.com'

toname = "Justen Morgan"

msg = "Messaging message"

subject = "Subject Message"

message = """

From: {} <{}>

To: {} <{}>

Subject: {}

{}

"""

messagetosend = message.format(

                             fromname,

                             fromaddr,

                             toname,

                             toaddr,

                             subject,

                             msg)

# Credentials (if needed)

username = 'info3180.justenmorgan@gmail.com'

password = 'info3180'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()