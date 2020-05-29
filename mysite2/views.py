# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': "Ritik", 'age': 20}
    return render(request, 'index.html', params)


def analyze(request):
    # get text
    text = request.GET.get('text', None)
    removepunc = request.GET.get('removepunc', None)
    fullcaps = request.GET.get('fullcaps', None)
    newlineremover = request.GET.get('newlineremover', None)
    spaceremover = request.GET.get('spaceremover', None)
    charcount = request.GET.get('charcount', None)
    # check for puctuation
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,; -./:<= >?@[\] ^ _`{ | }~'''
        analyzed_text = ""
        for char in text:
            if char not in punctuations:
                analyzed_text = analyzed_text+char
        d = {'analyzed_text': analyzed_text, 'purpose': 'removed puctuation'}
        return render(request, 'analyze.html', d)

    # check for capitalization
    elif fullcaps == 'on':
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        d = {'analyzed_text': analyzed, 'purpose': 'Changed to UPPERCASE'}
        return render(request, 'analyze.html', d)
    # new line remover
    elif newlineremover == 'on':
        analyzed = ""
        for char in text:
            if char != '\n':
                analyzed = analyzed + char
        d = {'analyzed_text': analyzed, 'purpose': 'Removed new lines'}
        return render(request, 'analyze.html', d)
    # Space remover
    elif spaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(text):
            if text[index] == ' ' and text[index+1] == ' ':
                pass
            else:
                analyzed = analyzed + char
        d = {'analyzed_text': analyzed, 'purpose': 'Removed extra Spaces'}
        return render(request, 'analyze.html', d)
    # Character counter
    elif charcount == 'on':
        analyzed = "No of Charaters = "+str(len(text))
        d = {'analyzed_text': analyzed, 'purpose': 'Characters Counted'}
        return render(request, 'analyze.html', d)
    else:
        return HttpResponse("<h1>Error<h1>")
