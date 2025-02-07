from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from random import randint
import ghasedakpack
from account.models import User

# otp = randint(100_000, 999_999)
ghasedak = ghasedakpack.Ghasedak('api-key')
good_line_number_for_sending_otp = '80005088'

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
        sms = ghasedak.verification({'receptor':Login.phone_number,'linenumber':good_line_number_for_sending_otp,'type':'1','template':'django','param1':Login.otp,'param2':Login.otp})
        if sms == True:
            return render(request, 'account/login.html')
        else:
            messages.error(request,'در ارسال پیامک مشکلی پیش امدی است')
        messages.success(request, Login.otp)
        context = {}
        return render(request, 'account/login.html',context)
    def post(self, request, *args, **kwargs):
        code=request.POST.get('code')
        if code == Login.otp:
            user = User.objects.filter(username=Login.username,phone=Login.phone_number).first()
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            else:
                new_user = User.objects.create(username=Login.username,phone=Login.phone_number)
                login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')
        else:
            print('no')
        context = {}
        return render(request, 'account/login.html', context)