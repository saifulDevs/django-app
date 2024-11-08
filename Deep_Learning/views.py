from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'deep_learning/deep_learning.html')
