from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'banner': 'A <em>REALISTIC APPROACH</em> TO THE PROBLEM <br> BUILDING A <em>RELIABLE SOLUTION</em>.'
    }
    return render(request, 'index.html', context)


def about_me(request):
    context = {
        'title': 'About Me',
        'banner': 'My name is <em>Seongwon</em> and I\'m a <em>Web Developer</em>.'
    }
    return render(request, 'about_me.html', context)


def tech_stack(request):
    context = {
        'title': 'Tech Stack',
        'banner': '<em>Languages</em> and <em>Frameworks</em>',
        'style': 'border-top: 1px solid #fff',

    }
    return render(request, 'tech_stack.html', context)
