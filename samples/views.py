from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext


@staff_member_required
def my_model_list_view(request):
    r = render_to_response('sometemplate.html', {}, RequestContext(request))
    return HttpResponse(r)
