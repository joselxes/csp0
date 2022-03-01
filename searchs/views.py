# import re
from re import search
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
tasks=["a0","a1","a2"]
class TypeSearch:
    def __init__(self):
        self.r = False
        self.i = False
        self.a = False
regular="https://www.google.com/search?q="
imageUrl="&tbm=isch"
advanceUrL="https://www.google.com/search?as_q"
class NewTaskForm(forms.Form):
    q = forms.CharField(label="q")
class RegSearchForm(forms.Form):
    q = forms.CharField(label="Search")    
class AdvSearchForm(forms.Form):
    q = forms.CharField(label="All these words           ")    
    q1 = forms.CharField(label="This exact word or phrase")    
    q2 = forms.CharField(label="Any of these words       ")    
    q3 = forms.CharField(label="None of these words      ")    
    # priority = forms.IntegerField(label="Priority", min_value=1,max_value=8)
def index(request):
    search= RegSearchForm()
    qe=TypeSearch()
    qe.r=True
    if request.method == "POST":
        search = RegSearchForm(request.POST)
        # print("-----------------",search,"----------------------")
        if search.is_valid():
            name = request.POST
            rsearch = search.cleaned_data["q"]
            if 'btnI' in name:
                # print(name,"cccccccccccccc")
                return HttpResponseRedirect ( regular+rsearch+'&btnI')
            # print(rsearch)
            return HttpResponseRedirect ( regular+rsearch)
    return render(request, "searchs/index.html",{"page":qe,"search":RegSearchForm})

def img(request):
    qe=TypeSearch()
    qe.r=True
    if request.method == "POST":
        search = RegSearchForm(request.POST)
        print("--------------",regular+imageUrl,"--------------")
        if search.is_valid():
            rsearch = search.cleaned_data["q"]
            print("--------------",regular+rsearch+imageUrl,"--------------")
            return HttpResponseRedirect ( regular+rsearch+imageUrl)
    return render(request, "searchs/img.html",{"page":qe,"search":RegSearchForm})


def adv(request):
    qe=TypeSearch()
    qe.r=True
    if request.method == "POST":
        search = AdvSearchForm(request.POST)
        print("--------------",regular+imageUrl,"--------------",search.is_valid())
        if search.is_valid():
            advq = "="+search.cleaned_data["q"]
            advq1 = "&as_epq="+search.cleaned_data["q1"]
            advq2 = "&as_oq="+search.cleaned_data["q2"]
            advq3 = "&as_eq="+search.cleaned_data["q3"]
            # print("--------------x",advanceUrL+advq+advq1+advq2+advq3,"\n","x--------------")
            return HttpResponseRedirect ( advanceUrL+advq+advq1+advq2+advq3)
    return render(request, "searchs/adv.html",{"page":qe,"search":AdvSearchForm})


# https://www.google.com/search?
# &as_q=youtube
# &as_epq=hola
# &as_oq=unboxing
# &as_eq=giveaway

# https://www.google.com/search?as_q=1&as_epq=2&as_oq=3&as_eq=4
# https://www.google.com/search?as_q&as_q=1&as_epq=2&as_oq=3&as_eq=4