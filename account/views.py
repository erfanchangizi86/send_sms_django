from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from random import randint

from account.models import User

otp = randint(100_000, 999_999)


class ShowHomePage(TemplateView):
    template_name = 'account/index.html'


class Login(TemplateView):
    otp = '0'
    username = ''
    phone_number = ''

    def get(self, request, *args, **kwargs):
        Login.username = request.GET.get('username')
        Login.phone_number = request.GET.get('phone')
        Login.otp = str(randint(100000, 999999))
        messages.success(request, Login.otp)
        context = {}
        return render(request, 'account/login.html',context)
    def post(self, request, *args, **kwargs):
        code=request.POST.get('code')
        if code == Login.otp:
            user = User.objects.filter(username=Login.username).filter()
            if user.exists():
                pass
            else:
                User.objects.create(username=Login.username,phone=Login.phone_number)
        else:
            print('no')
        context = {}
        return render(request, 'account/login.html', context)