from django.shortcuts import render

def main(request):
     return render(request, 'main/index.html')

def resume(request):
     return render(request, 'main/index2.html')

def projects(request):
     return render(request, 'main/index3.html')

def contact(request):
     return render(request, 'main/index4.html')