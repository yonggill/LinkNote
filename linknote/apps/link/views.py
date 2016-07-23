# -*- coding:utf-8 -*-


import json
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView, View, ContextMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from linknote.apps.link.models import Link
from django.contrib.auth.models import User
from jwt_auth.mixins import JSONWebTokenAuthMixin


class LinkListView(TemplateView):
    template_name = 'link/link_list.html'


class LinkAddAPI(ContextMixin, JSONWebTokenAuthMixin, View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LinkAddAPI, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        link = Link(
            user=request.user,
            url=data['url'],
            note=data['note']
        )
        link.save()
        return HttpResponse(json.dumps({'success': True}), content_type='application/json')