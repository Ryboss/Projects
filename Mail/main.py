import smtplib
import email.message
message = {
    'name': input('Введите имя'),
    'recipient': input('Введите почту получателя'),
    'phone': input('Введите номер телефона'),
    'message': input('Введите сообщение'),
    'subject':input('Введите тему')

}
email_content = f"""
<html>
 
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    
   <title>New Message</title>

</head>
 
<body>
<p>Name recipient {message['name']}</p>
<p>Phone recipient {message['phone']}</p>
<p>Message {message['message']}</p>
</body>
</html>"""
msg = email.message.Message()
msg['Subject'] = message['subject']
msg['From'] = 'Your mail'
msg['To'] = 'gilmanovamirqa@gmail.com'
password = "your password"
msg.add_header('Content-Type', 'text/html')
msg.set_payload(email_content)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()

# Login Credentials for sending the mail
s.login(msg['From'], password)

s.sendmail(msg['From'], [message['recipient']], msg.as_string())