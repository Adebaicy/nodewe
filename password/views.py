from django.shortcuts import render
from django.http import HttpResponse#to make it html like
import random
# Create your views here.
 

def home(request):
    return render(request, 'password/home.html', {'BROKE': 2})
def about(request):
    return render(request, 'password/about.html')

def seun(request):
    lent=int(request.GET.get("ll", 55))
    alpha=list('abcdefghijklmn')
    if request.GET.get('uppercase') == 'on':
        alpha.extend(list('ABCDE'))
    if request.GET.get('special') == 'on':
        alpha.extend(list('82617@$#'))
        
    
    passw=''
    for i in range(lent):
        passw+=random.choice(alpha)
   
    return render(request, 'password/seun.html', {'password': passw})