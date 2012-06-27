from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    user = request.user
    if not user.id or not request.session.get('code_sucess'):
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/register/')

