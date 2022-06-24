from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from HospitalWebsiteDjango.settings import EMAIL_HOST_USER
from hospital.models import appointment, sub_e_mail, contact, contact1


def appo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Phone = request.POST.get('phone')
        make = request.POST.get('make')
        message = request.POST.get('msg')
        try:
            mem = appointment(full_name=name, mail=email, phone=Phone, make_an_appointment=make, message=message)
            mem.save()
            return render(request, 'home2.html', {'member': mem})
        except:
            return render(request, 'home.html')

    else:
        return render(request, 'home.html')


def index(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def conta_ct(request):
    return render(request, 'contact.html')


def facility(request):
    return render(request, 'facility.html')


def post(request):
    return render(request, 'post.html')


def review(request):
    return render(request, 'review.html')


def ema(request):
    member = sub_e_mail(email=request.POST['mail'], )
    member.save()
    subject = 'From HealthCare....! NewsLetter'
    message = 'HealthCare- Know your Treatment is established with an intention to encourage growth and intake of Hospitals. As many patients who are doing contemporary farming are in fact getting aware of the importance of Organic cultivation and Natural farming, but are hesitant to adapt those methods, we wanted to go in aid of them. We wanted to provide those farmers who are producing organic food or following ZBNF or natural methods of cultivation without using chemical fertilizers and pesticides, a market place to sell their products for fair enough prices.' \
              'When we had an interaction with such farmers, they helplessly said that they had to sell organic products at normal market price those it took them lot of efforts to get the crop out. Also the consumers complained that the cost of organic and natural products which they are getting in the markets is too high and hence can’t afford to buy, also they say that they can’t be sure of the authenticity of the products which are available in the market, claiming to be organic.' \
              'To give an answer to all these concerns, we at HealthCare took an initiative. We are a small group of software developers who are basically into website and mobile app development business. But we possess a passion of cultivating healthy organic food as we come from a farming back ground. As we are aware of the concerns regarding organic production and market in the present society, we wanted to go in aid of the farmers as well as consumers.' \
              'Welcome To Our World ...! Nice To Meet You...!' \
              'We Will Always Care About You' \
              '' \
              'We Wiil Send All The Updates We Have'
    recepient = str(member.email)
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
    return render(request, 'home.html')


def con(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        subject1 = request.POST.get('subject')
        message1 = request.POST.get('message')
        try:
            mem2 = contact1(full_name=name1, Email=email1, subject=subject1, message=message1)
            mem2.save()
            return render(request, 'home2.html', {'member1': mem2})
        except:
            return render(request, 'home.html')

    else:
        return render(request, 'home.html')


def learn_more(request):
    return render(request, 'learn_more.html')
