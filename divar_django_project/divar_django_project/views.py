from django.http import HttpResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse_lazy
from .forms import ContactUsForm
from django.core.mail import send_mail
from django.conf import settings
from django.views import generic


def index(request: WSGIRequest) -> HttpResponse:
    return render(request, 'index.html')



class ContactUsView(generic.FormView):
    template_name = 'contact-us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('index')
    
    def post(self, request, *args, **kwargs) -> HttpResponse:
        form = self.get_form()
        if form.is_valid():
            self.__send_mail(form)
            return render(request, template_name=ContactUsView.template_name,
                            context={
                                'form': form,
                                'res': 'done'
                            })
        else:
            return render(request, template_name=ContactUsView.template_name,
                            context={
                              'form': form, 
                              'res': 'error'
                            })
            
    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, template_name=ContactUsView.template_name, 
                            context={'form': self.get_form()})
    
    
    
    def __send_mail(self, form) -> None:
        message = f'''  موضوع: {form.cleaned_data.get('title')}
                        ایمیل فرستنده: {form.cleaned_data.get('email')}
                            
                        متن پیام: {form.cleaned_data.get('message')}
                    '''
        subject = form.cleaned_data.get('title')
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, ['danial.erfanian@divar.ir'], fail_silently=True)