from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class LoginView(DjangoLoginView):
    template_name = 'scoreguru/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, "You have successfully logged in!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)

class CreateAccountView(CreateView):
    template_name = 'scoreguru/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Account created successfully! You can now log in.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error creating your account. Please correct the issues below.")
        return self.render_to_response(self.get_context_data(form=form))
    
class LogoutView(DjangoLogoutView):
    http_method_names = ['get', 'post']
    next_page = 'login'
    
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect('/')
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been successfully logged out.")
        return super().dispatch(request, *args, **kwargs)