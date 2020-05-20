from django.shortcuts import render, redirect

from .handlers.email import set_default_reply, relay_portfolio_message
from .settings import TITLE, BANNER, EMAIL, STYLE, STATES


def about_me(request):
    from .settings import BANNER_HOME, TITLE_HOME
    context = {
        TITLE: TITLE_HOME,
        BANNER: BANNER_HOME,
        STYLE: 'border-top: 1px solid #fff',
    }
    return render(request, 'pages/about_me.html', context)


def contact_me(request):
    from .forms import ContactInfoForm
    from .settings import EMAIL_ADDRESS, SUBJECT_DEFAULT, TITLE_CONTACT, BANNER_CONTACT, FORM
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
            self_notice = relay_portfolio_message(form.data['email'], form.data['name'], form.data['message_content'], form.data['message_type'])
            if self_notice.status_code == 200:
                set_default_reply(form.data['email'], form.data['name'])
            return redirect('main')
    return render(request, 'pages/contact.html', context)


def sample_api(request):
    from ..common_handler.settings import STATES_LIST
    from .settings import TITLE_SAMPLE_API, BANNER_SAMPLE_API, DISCLAIMER_SAMPLE_API, DISCLAIMER
    context = {
        TITLE: TITLE_SAMPLE_API,
        BANNER: BANNER_SAMPLE_API,
        DISCLAIMER: DISCLAIMER_SAMPLE_API,
        STYLE: 'border-top: 1px solid #fff',
        STATES: STATES_LIST
    }
    return render(request, 'pages/sample_api.html', context)