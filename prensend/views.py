from django.shortcuts import render


# Create your views here.
def prensend(request):
    return render(
        request,
        'prensend/prensend.html',
    )
