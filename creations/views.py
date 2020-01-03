from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from django.core.paginator import Paginator
from .models import creation, slider, testimonial
from .forms import contactForm

# Create your views here.


def home(request):
    posts_list = creation.objects.all()
    sliders = slider.objects.all()
    paginator = Paginator(posts_list, 6)  # Show 25 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, "creations/portfolio.html", {'posts': posts, 'sliders': sliders})


def test(request):
    posts = testimonial.objects.all()
    return render(request,'creations/testimonials.html',{'posts':posts})


def contactus(request):
    if request.method == "POST":
        subject = request.POST['subject']
        name = request.POST['name']
        sender = request.POST['email']
        message = request.POST['msg']
        recipients = ['rakesh.linux@gmail.com']
        subject = subject + '- ' + name
        send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect('/thanks/')
    else:
        return render(request, 'creations/contact.html')

def contact(request):
    if request.method =="POST":
        form = contactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            message = form.cleaned_data['msg'] 
            recipients = ['rakesh.linux@gmail.com']
            subject = subject+" " + name
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = contactForm(request.POST)
        return render(request, 'creations/contact1.html',{'form': form})


def thanks(request):
    return render(request, 'creations/thanks.html')
