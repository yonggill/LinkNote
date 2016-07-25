# -*- coding: utf-8 -*-

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib import messages

# 로그아웃 뷰
@login_required
def logout_view(request):
    # 로그인 후 메인 페이지로 이동
    logout(request)
    return HttpResponseRedirect('/')


# 로그인 뷰
class LoginView(TemplateView):
    template_name = 'account/login.html'

    def post(self, request, *args, **kwargs):
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            url = '/link/my_link/'
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(url)
                else:
                    return HttpResponseRedirect('/accounts/not_active/')
        messages.add_message(request, messages.WARNING, u'아이디와 비밀번호를 다시 확인해주세요.')
        return self.get(request, *args, **kwargs)


# 로그인 뷰
class LoginTokenView(TemplateView):
    template_name = 'account/login.html'

    def post(self, request, *args, **kwargs):
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if 'next' in request.POST:
                url = request.POST['next']
                print url
            else:
                url = '/link/my_link/'
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(url)
                else:
                    return HttpResponseRedirect('/accounts/not_active/')
        messages.add_message(request, messages.WARNING, u'아이디와 비밀번호를 다시 확인해주세요.')
        return self.get(request, *args, **kwargs)


# 회원가입 뷰
class SignupView(TemplateView):
    template_name = 'account/signup.html'

    def post(self, request, *args, **kwargs):
        validation, data = self.check_data_validate(request.POST)
        if validation:
            user = User.objects.create_user(
                data['username'],
                data['email'],
                data['password']
            )
            user = authenticate(username=user.username, password=data['password'])
            login(request, user)
            return HttpResponseRedirect('/link/my_link/')
        else:
            messages.add_message(request, messages.WARNING, u'잘못 입력된 값이 있습니다.')
        return self.get(request, *args, **kwargs)

    def check_data_validate(self, data):
        validation = True
        result = dict()
        if 'username' in data and data['username']:
            result['username'] = data['username']
        else:
            validation = False
        if 'password1' in data and 'password2' in data \
                and data['password1'] == data['password2']:
            result['password'] = data['password1']
        else:
            validation = False
        if 'email' in data and data['email']:
            result['email'] = data['email']
        else:
            validation = False
        return (validation, result)
