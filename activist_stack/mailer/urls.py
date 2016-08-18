# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    # URL pattern for the Mailer
    url(
        regex=r'^editor$',
        view=TemplateView.as_view(template_name='mailer/editor.html'),
        name='mailer-editor',
    ),
]
