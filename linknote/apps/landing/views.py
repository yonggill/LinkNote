# -*- coding:utf-8 -*-

from django.views.generic.base import TemplateView
from django.http.response import HttpResponseRedirect


class LandingView(TemplateView):
    template_name = 'landing/landing.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/link/my_link/')
        return super(LandingView, self).get(request, *args, **kwargs)
