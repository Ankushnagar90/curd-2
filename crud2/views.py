from django.shortcuts import render,HttpResponseRedirect
from .forms import studentregister
from django import forms
from .models import Person
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

#git commit bnana
# git commit 2************

# Create your views here.

class UserAddShowView(TemplateView):
    template_name = 'crud2/addstudent.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        fm=studentregister()
        stud = Person.objects.all()
        context = {'stu':stud, 'form':fm}
        return context
    def post(self,request):
        fm = studentregister(request.POST)
        if fm.is_valid():
            fnm = fm.cleaned_data['first_name']
            lnm = fm.cleaned_data['last_name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg=Person(first_name=fnm,last_name=lnm,email=em,password=pwd)
            reg.save()
            return HttpResponseRedirect('/')






#update function

class UserUpdateView(View):
    def get(self,request,id):
        pi = Person.objects.get(pk=id)
        fm = studentregister(instance=pi)
        return render(request,'crud2/updatestu.html',{'form':fm})
        # return HttpResponseRedirect('crud2/updatestu.html')

    def post(self,request,id):
        pi = Person.objects.get(pk=id)
        fm=studentregister(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()

        return HttpResponseRedirect('/')



# def update_data(request,id):
#     if request.method == 'POST':
#         pi = Person.objects.get(pk=id)
#         fm=studentregister(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:
#         pi = Person.objects.get(pk=id)
#         fm = studentregister(instance=pi)
#     return render(request,'crud/updatestu.html',{'form':fm})



# Delete function:

class UserDeleteView(RedirectView):
    url='/'
    def get_redirect_url(self,*args, **kwargs):
        del_id=(kwargs['id'])
        print(del_id)
        Person.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)




# def delete_data(request,id):
#     if request.method == 'POST':
#         pi=Person.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')
