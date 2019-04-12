# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Alpha.models import AccessRecord, Webpage, Topic
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)

