from django.shortcuts import render


def clicker_html(request):
    return render(request, 'clicker.html')
