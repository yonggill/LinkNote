# -*- coding:utf-8 -*-

from django.conf.urls import url
from linknote.core.applications import Application

from .views import LandingView


class LandingApp(Application):
    name = None

    def get_urls(self):
        urls = [
            url(r'^$',
                LandingView.as_view(),
                name='landing')
        ]
        return urls

application = LandingApp()
