from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Course
from .forms import RegisterForm, LoginForm, EditForm, NewCourse




def logout_(request: WSGIRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))


@login_required
def profile(request: WSGIRequest) -> HttpResponse:
    return render(request, 'portal/profile.html')


@login_required
def panel(request: WSGIRequest) -> HttpResponse:
    return render(request, 'portal/panel.html', 
                  context={
                      'courses': Course.objects.all(),
                      'is_admin': request.user.is_superuser,
                    })


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'portal/register.html'
    success_url = reverse_lazy('index')
    
    
class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'portal/login.html'
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


class EditView(LoginRequiredMixin, generic.edit.UpdateView):
    template_name = 'portal/edit.html'
    form_class = EditForm
    success_url = reverse_lazy('portal:profile')

    def get_object(self):
        return self.request.user


class NewCourseView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    template_name = 'portal/new_course.html'
    model = Course
    form_class = NewCourse
    success_url = reverse_lazy('portal:panel')
    
    def test_func(self):
        return self.request.user.is_superuser

