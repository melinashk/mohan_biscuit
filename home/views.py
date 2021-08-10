import random

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import View
from twilio.rest import Client
from .forms import *
from .models import *


# Create your views here.
class BaseView(View):
    view = {}


class AboutView(BaseView):
    def get(self, request):
        self.view['aboutus'] = Aboutus.objects.all()
        return render(request, 'aboutus.html', self.view)


class HomeView(BaseView):
    def get(self, request):
        self.view['slider'] = Slider.objects.all()
        self.view['status'] = Status.objects.all()
        self.view['slideshow'] = Slideshow.objects.all()
        return render(request, 'index.html', self.view)


class ContactView(BaseView):
    def get(self, request):
        self.view['distributor'] = Distributor.objects.all()
        self.view['manager'] = Manager.objects.all()
        self.view['accountant'] = Accountant.objects.all()
        self.view['salesperson'] = Salesperson.objects.all()
        return render(request, 'contact.html', self.view)


class ProductView(BaseView):
    def get(self, request):
        self.view['product'] = Product.objects.all().order_by('category', 'name')
        return render(request, 'product.html', self.view)


account_sid = 'ACf2d702d07a31e858bcc0071e5a4a1be7'
auth_token = '43d51d20106d3d48cb34e6a1bd0f5886'
client = Client(account_sid, auth_token)


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        otp = str(random.randint(1000, 9999))
        profile = Person(name=name, email=email, phone=phone, otp=otp)
        profile.save()

        message = client.messages.create(
            body=otp,
            from_='+14159680282',
            to=phone
        )
        request.session['phone'] = phone
        return render(request, 'otp.html')
    else:
        return render(request, 'rating.html')


def otp(request):
    phone = request.session['phone']
    context = {'phone': phone}
    if request.method == 'POST':
        otp = request.POST['otp']
        profile = Person.objects.filter(phone=phone).first()

    if otp == profile.otp:
        return redirect('ratepage')
    else:
        print('Wrong OTP')

        context = {'message': 'Wrong OTP', 'class': 'danger', 'phone': phone}
        return render(request, 'otp.html', context)

    return render(request, 'otp.html', context)


def ratepage(request):
    if request.method == 'POST':
        form = Rateform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('ratepage')
    else:
        form = Rateform()

    return render(request, 'rate_page.html', {'form': form})


class StatusView(BaseView):
    def get(self, request):
        self.view['careerstatus'] = CareerStatus.objects.all()
        return render(request, 'career_access.html', self.view)


def career(request):
    if request.method == 'POST':
        form = CareerForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('career')
    else:
        form = CareerForm()

    return render(request, 'career.html', {'form': form})


def inquiry(request):
    if request.method == "POST":
        name = request.POST['name']
        number = request.POST['number']
        address = request.POST['address']
        email = request.POST['email']
        query = request.POST['query']

        print(name, number, address, email, query)

        data = Inquiry(
            name=name,
            number=number,
            address=address,
            email=email,
            query=query,
        )
        data.save()

        send_mail(
            'Inquiry by ' + name + '.',
            'You have got mail from ' + email + '. The query is: ' + query + '.',
            email,
            ['mohan.biscuit.f@gmail.com'],
            fail_silently=False,
        )

        send_mail(
            'Reply to ' + name + '.',
            'The query is: ' + query + ' has been received.',
            'mohan.biscuit.f@gmail.com',
            [email],
            fail_silently=False,
        )
    return render(request, "inquiry.html")
