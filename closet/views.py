import json
import ast
from urllib2 import quote, unquote

from django.conf import settings
from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic.base import View


def home(request):
    return render(request, "home.html",{},
                            content_type='text/html')
