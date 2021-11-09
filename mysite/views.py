from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    params = {'name': 'sahil', 'age': '24'}
    return render(request, 'index.html', params)


def analyze(request):
    removepunc = request.POST.get('removepunc', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    djtext = request.POST.get('text', 'default')
    newlineremover = request.POST.get('newlineremover', 'off')
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed


    if spaceremove == "on":
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char
        params = {'purpose': 'Space Remove', 'analyzed_text': analyzed}
        djtext = analyzed
    if uppercase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
        djtext = analyzed


    if (removepunc == 'off' and spaceremove == "off" and uppercase == "off" and newlineremover == "on"):
        return HttpResponse("Please Select any utility ")

    return render(request, 'analyze.html', params)