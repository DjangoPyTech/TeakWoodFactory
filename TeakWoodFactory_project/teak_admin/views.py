from django.shortcuts import render

# Create your views here.
def admin_home(request):
    return render(request,'admin_temp/index.html')

def product_view(request):
    return render(request,'admin_temp/product.html')