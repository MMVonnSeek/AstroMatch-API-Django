from django.shortcuts import render

def home_bonita(request):
    return render(request, 'api_signs.html')

def sign_detail(request, sign_id):
    return render(request, 'sign_detail.html')
