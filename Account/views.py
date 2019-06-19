from django.shortcuts import  render, redirect
from .models import CreateCustomer,Create_login, Customer_Account
from django.views.generic.edit import FormView,CreateView
from django.urls import reverse_lazy
from  django import forms


class SignUp(CreateView):
    template_name='Account/SignUp_in.html'
    form_class=CreateCustomer
    success_url = reverse_lazy('account:sign_in')
    extra_context={'tittle':'SignUp'}


class SignIn(FormView):
    template_name='Account/SignUp_in.html'
    form_class=Create_login

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            customer = Customer_Account.objects.get(User_Name=form.cleaned_data['User_Name'])
            request.session['username'] = customer.name
            return redirect('product:home')
        return render(request, self.template_name, {'form': form,'tittle':'SignIn'})

    def get(self, request, *args, **kwargs):
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if request.session.has_key('username'):
                    del request.session['username']
        return render(request, self.template_name, {'form': Create_login(),'tittle':'SignIn'})







