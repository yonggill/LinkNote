# -*- coding:utf-8 -*-

from django.conf.urls import url
from linknote.core.applications import Application

from .views import *


class LinkApp(Application):
    name = 'Link'

    def get_urls(self):
        urls = [
            url(r'^my_link/$',
                LinkListView.as_view(),
                name='landing'),

            url(r'^add/$',
                LinkAddAPI.as_view(),
                name='add')
        ]
        return urls

application = LinkApp()
