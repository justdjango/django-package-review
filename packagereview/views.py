from django import forms
from django.shortcuts import render, redirect
from honeypot.decorators import check_honeypot

class ContactForm(forms.Form):
    email2343242 = forms.EmailField(label='Email')


@check_honeypot(field_name='email')
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data['email2343242'])
        return redirect("/contact")
    context = {
        'form': form
    }
    return render(request, "contact.html", context)