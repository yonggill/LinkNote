# -*- coding:utf-8 -*-

from django.conf.urls import url
from linknote.core.applications import Application

from .views import *


class AccountApp(Application):
    name = None

    def get_urls(self):
        urls = [
            url(r'^logout/$',
                logout_view,
                name='logout'),

            url(r'^login/$',
                LoginView.as_view(),
                name='login'),

            url(r'^login_return_token/$',
                LoginTokenView.as_view(),
                name='login'),

            url(r'^signup/$',
                SignupView.as_view(),
                name='signup')
        ]
        return urls

application = AccountApp()
