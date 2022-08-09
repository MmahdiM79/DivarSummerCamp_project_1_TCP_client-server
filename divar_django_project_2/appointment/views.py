from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

from .forms import RegisterForm, LoginForm, EditForm
from .models import UserBioGender


# Create your views here.

def logout_(request: WSGIRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))


@login_required
def profile(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appointment/profile.html')


@require_http_methods(['GET'])
def search(request: WSGIRequest) -> HttpResponse:
    key = request.GET.get('search')
    '''
        finding all users in group 'Professor'
        which its username or first_name or last_name contain key
    '''
    res = UserBioGender.objects.all().filter(groups=1)
    res = res.filter(Q(username__contains=key) | Q(first_name__contains=key) | Q(last_name__contains=key))
    
    return render(request, 'appointment/search_result.html', {'res': res})


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'appointment/register.html'
    success_url = reverse_lazy('index')


class EditView(LoginRequiredMixin, generic.edit.UpdateView):
    template_name = 'appointment/edit.html'
    model = UserBioGender
    form_class = EditForm
    success_url = reverse_lazy('appointment:profile')

    def get_object(self, queryset=None):
        return self.request.user


class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'appointment/login.html'
    success_url = reverse_lazy('index')
    
    def post(self, request, *args, **kwargs) -> HttpResponse:
        form = self.get_form()
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(redirect_to=reverse_lazy('index'))
            else:
                return render(request, LoginView.template_name, {'form': form, 'error': True})
        else:
            return render(request, LoginView.template_name, {'form': form})
