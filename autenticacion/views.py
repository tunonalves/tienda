from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm, AdminPasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User 
from .forms import CustomUserChangeForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

class VRegistro(View):

    def get(self,request):
        form = UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})

    def post(selft, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request,usuario)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,"registro/registro.html",{"form":form})



def cerrar_seccion(request):
    logout(request)
    return redirect("Home")



def loguear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("username")
            password_user = form.cleaned_data.get("password")
            user = authenticate(username=name_user,password=password_user)
            if user is not None:
                login(request,user)
                return redirect('Home')
            else:
                messages.error(request, "Usuario No Valido")
        else:
            messages.error(request, "Informacion No Valida")
    form = AuthenticationForm()
    return render(request,"login/login.html",{"form":form})



@login_required
def user_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(instance=request.user)
        if form.is_valid():
            user = form.save()
            user.save()
    form = CustomUserChangeForm(instance=request.user)
    return render(request,"edit/edit.html",{"form":form})



class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'auth/listUser.html'

class UserDetalle(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'auth/user_details.html'

class UserCreacion(CreateView):
    model = User
    success_url = reverse_lazy('user_list')#
    fields='__all__'

class UserEdicion(UpdateView):
    model = User
    success_url = reverse_lazy('user_list')#
    fields='__all__'

class UserEliminacion(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')#
    fields='__all__'