from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import contactForm
from django.core.mail import send_mail, get_connection, EmailMessage

#def homeView (request):
    #return render (request, 'home.html')

def homeView(request):
    submitted = False
    if request.method =='POST':
        form = contactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #assert False
            con = get_connection('django.core.mail.backends.smtp.EmailBackend')
            email = EmailMessage(
                cd['subject'],
                cd['message'],
                cd['email'],
                ['smithrh20@gmail.com'],
                reply_to=[cd.get('email')],
                connection=con
            ).send()
            return HttpResponseRedirect('/#?submitted=True')
    else:
        form = contactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render (request, 'home.html', {'form':form, 'submitted': submitted})