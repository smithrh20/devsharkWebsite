from django import forms

class contactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    yourname.widget.attrs.update({'class': 'formInput'})
    email = forms.EmailField(label='Your Email Address')
    email.widget.attrs.update({'class': 'formInput'})
    subject = forms.CharField(max_length=100)
    subject.widget.attrs.update({'class': 'formInput'})
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'contentInput'}))