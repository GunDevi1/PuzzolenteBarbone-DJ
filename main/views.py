from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def recipe1(request):
    return render(request, 'main/recipe_rizotto.html')

def recipe2(request):
    return render(request, 'main/recipe_ravioli.html')

def recipe3(request):
    return render(request, 'main/recipe_carbonara.html')

def recipe4(request):
    return render(request, 'main/recipe_balaneza.html')

def recipe5(request):
    return render(request, 'main/recipe_lazania.html')

def recipe6(request):
    return render(request, 'main/recipe_porcketa.html')