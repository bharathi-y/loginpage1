from django.shortcuts import render
def main_page(request):
    return render(request,'main_page.html',context={})
def sign_in(request):
    return render(request,'sign_in.html',context={})
def sign_up(request):
    return render(request,'sign_up.html',context={})
# Create your views here.
