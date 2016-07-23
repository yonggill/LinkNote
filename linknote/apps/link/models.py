# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    user = models.ForeignKey(
        User,
        null=False,
        related_name='links'
    )

    url = models.URLField(
        null=False
    )

    note = models.TextField(
        blank=True,
        null=True
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    @property
    def domain(self):
        return self.url.split('/')[2]
