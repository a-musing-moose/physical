# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.conf.urls import url

from . import views
from .api import views as api_views


urlpatterns = [
    # waste:home
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(
        r'^api/capture$',
        api_views.ImageAPIView.as_view(),
        name='physical'
    )
]
