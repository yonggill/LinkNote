# -*- coding:utf-8 -*-

from django.conf.urls import include, url
from linknote.core.applications import Application

from linknote.apps.account.apps import application as AccountApp
from linknote.apps.landing.apps import application as LandingApp
from linknote.apps.link.apps import application as LinkApp


class LinkNoteApp(Application):
    name = None

    account_app = AccountApp
    landing_app = LandingApp
    link_app = LinkApp

    def get_urls(self):
        urls = [
            url(r'^accounts/', include(self.account_app.urls)),
            url(r'^', include(self.landing_app.urls)),
            url(r'^link/', include(self.link_app.urls))
        ]
        return urls

linknote_app = LinkNoteApp()
