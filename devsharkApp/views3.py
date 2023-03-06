from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import contactForm
from django.core.mail import send_mail, get_connection

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
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['smithrh20@gmail.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = contactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render (request, 'home.html', {'form':form, 'submitted': submitted})