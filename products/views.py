from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'title':'Gretong a Ecommerce Category Flat Bootstarp Responsive Website Template | Home :: w3layouts',
        'is_promosion': False
    }
    return render(request,'products/index.html', context)


def details(request):
    return render(request,'products/details.html')

def women(request):
    return render(request,'products/women.html')

def register(request):
    return render(request,'products/register.html')

def contact(request):
    return render(request,'products/contact.html')

def checkout(request):
    return render(request,'products/checkout.html')