from django.shortcuts import render, redirect

from personal.settings import TITLE, BANNER, EMAIL


def about_me(request):
    from personal.settings import BANNER_HOME, TITLE_HOME
    context = {
        TITLE: TITLE_HOME,
        BANNER: BANNER_HOME,
        'style': 'border-top: 1px solid #fff',
    }
    return render(request, 'about_me.html', context)


def contact_me(request):
    from personal.forms import ContactInfoForm
    from personal.settings import EMAIL_ADDRESS, SUBJECT_DEFAULT, TITLE_CONTACT, BANNER_CONTACT, FORM
    context = {
        TITLE: TITLE_CONTACT,
        BANNER: BANNER_CONTACT,
        EMAIL: {
            'address': EMAIL_ADDRESS,
            'subject_default': SUBJECT_DEFAULT,
        },
        FORM: ContactInfoForm()
    }
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, 'contact.html', context)
