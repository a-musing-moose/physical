# -*- coding: utf-8- -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PhysicalAppConfig(AppConfig):
    name = 'physical'
    verbose_name = _("physical")
