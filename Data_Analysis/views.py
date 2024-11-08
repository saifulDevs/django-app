from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'data_analysis/data_analysis.html')
