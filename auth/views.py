from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['code_sucess'] = True
                return HttpResponseRedirect(reverse('registration.views.register_form'))
            else:
                state = "Your account is not active, please contact the site"
        else:
            state = "Your username and/or password were incorrect."
    
    if not request.user.id or not request.session.get('code_sucess'):
        return render_to_response('auth/login_form.html',{'state':state, 'username':username}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('registration.views.register_form'))
     
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_login_required(var):
    def wrap(request, *args, **kwargs):
        user = request.user
        if not user.id or not request.session.get('code_sucess'):
            return HttpResponseRedirect('/login/')
            
        return var(request, *args, **kwargs)
    wrap.__doc__=var.__doc__
    wrap.__name__=var.__name__
    return wrap
