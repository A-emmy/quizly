from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from .forms import SignUp, Login

# Create your views here.
#  this is responsible for the logic behind the application its mostly the largest part of the application....render allows us display a page nb each class is a view in django and each function is a view

class SignUpView(View):
    def get(self, request):
        form = SignUp()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save(commit=False)    # save the user to the database
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user) # log the user in
            return redirect("/dashboard")
        return render(request, 'signup.html', {'form': form})    


class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')


class LoginView(View):
    def get(self, request):
        form = Login()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = Login(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/dashboard")
        return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/login")     


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')                           



























        