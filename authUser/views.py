from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.http import HttpRequest

# Create your views here.
    #with templateView and OO
class LoginView(TemplateView):
    template_name = 'auth/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            django_login(request, user)
            return redirect('index')
        
        message = 'Credenciais inválidas'
        return render(request, 'auth/login.html', {'message': message})

# with templateView and OO
# class LogoutView(TemplateView):
#     template_name = 'auth/login.html'
    
#     def get(self, request, *args, **kwargs):
#         django_logout(request)
#         return redirect('index')

# with view and OO
# class LoginView(View):
#     template_name = 'auth/login.html'
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             django_login(request, user)
#             return redirect('index')
        
#         message = 'Credenciais inválidas'
#         return render(request, self.template_name, {'message': message})

# without view and OO
# class LogoutView(View):
#     def get(self, request, *args, **kwargs):
#         django_logout(request)
#         return redirect('index')

# without OO
# def login(request: HttpRequest):
#     if request.method == "GET":
#         return render(request, "authUser/templates/auth/login.html")

#     username = request.POST.get("username")
#     password = request.POST.get("password")

#     user = authenticate(username=username, password=password)

#     if user:
#         django_login(request, user)
#         #next_param = request.GET.get('next')
#         #if next_param:#
#         return redirect('index')
    
#     message = "Credenciais inválidas"
#     return render(request, 'authUser/templates/auth/login.html', {'message': message})


# without OO
# def logout(request: HttpRequest):
#     django_logout(request)
#     return redirect('userLogin')