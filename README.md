# automatic-email-sender
This auto email sender web app is used to send mail from a preset email id to others automatically.



Functions:
"from django.core.mail import send_mail" this is the command that django provides for sending mail
Notes:
1.enter the location path of the project in templates column of the settings file
2.enter your email id and password in the settings file at the end
3.enter your email id in views.py in the mailsapp folder

send_mail(  
            sub,msg,'enter your mail id',
            [email]
            )
       in the above command you should enter your mail id and "[email]" which is the receiver mail id that is displayed in front end and stored in backend.     
