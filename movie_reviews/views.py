from django.shortcuts import redirect, render

def redirect_to_swagger(request):
    return redirect('/swagger/')

def index(request):
    return render(request, 'base.html')