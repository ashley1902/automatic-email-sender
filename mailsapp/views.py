yfrom django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def Index(request):
    if request.method == "POST":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')
        print(sub,msg,email)
        send_mail(  
            sub,msg,'Enter your email id',
            [email]
        )
        return HttpResponse('email send that !')
    return render(request, 'mailsapp/form.html')
