from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.views import View 
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed

from accounts.forms import LoginForm
from accounts.forms import UserForm
from folders.models import RootFolder

class SignUpView(FormView):
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")
    form_class = UserForm
    
    def form_valid(self, form):
        # create the user
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("pass1")
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # create the root directory for that user
        root = RootFolder.objects.create(root_owner=user, owner=user, name="root")
        root.save()
        
        return super().form_valid(form)

class HomeView(LoginRequiredMixin, View):
    login_url = reverse_lazy("accounts:login")
    
    def get(self, request):
        return render(request, "accounts/home.html")
    
    def post(self, request):
        return HttpResponseNotAllowed(("GET"))

class LogoutView(LoginRequiredMixin, View):
    login_url = reverse_lazy("accounts:login")
    def get(self, request):
        logout(request)
        return redirect("accounts:login")
    
    def post(self, request):
        return HttpResponseNotAllowed(("GET"))

class LoginView(FormView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy("accounts:home")

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("accounts:home")
        return super().get(request)

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(self.request, username=username, password=password)
        if user is None:
            form.add_error("username", "Username/password combination is not correct")
            return super().form_invalid(form)
        else:
            login(self.request, user)
            return super().form_valid(form)
