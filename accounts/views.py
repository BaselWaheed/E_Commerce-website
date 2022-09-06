from django.shortcuts import render  ,HttpResponseRedirect
from accounts.forms import MyUserLoginForm , CustomUserCreationForm
from django.contrib.auth import logout , login 
from django.views import View





class LoginView(View):
    form_class = MyUserLoginForm
    initial = {'key': 'value'}
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


    def post(self, request , *args , **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            print(user)
            login(request , user)
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


class SignUpView(View):
    form_class = CustomUserCreationForm
    initial = {'key': 'value'}
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request , *args , **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


            


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')




