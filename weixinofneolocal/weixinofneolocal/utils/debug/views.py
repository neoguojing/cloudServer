# coding=utf-8
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def displayErr(request):
    t = get_template('err.html')
    c = Context({'errinfo':"fuck"});
    html = t.render(c)
    return HttpResponse(html)
