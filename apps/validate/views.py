from django.shortcuts import redirect,render
from django.views.generic import TemplateView,FormView
from django.views.generic import View
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

class ValidateDashBoardView(LoginRequiredMixin,TemplateView):
    template_name = 'ddashboard.html'
    def get_context_data(self, **kwargs):
        context=super(ValidateDashBoardView,self).get_context_data(**kwargs)
        context.update({
        })
        return context

    def get(self,request,*args,**kwargs):
        return super(ValidateDashBoardView,self).get(request,*args,**kwargs)