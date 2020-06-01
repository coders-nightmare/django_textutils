# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': "Ritik", 'age': 20}
    return render(request, 'index.html', params)


def analyze(request):
    # get text
    text = request.POST.get('text', None)
    removepunc = request.POST.get('removepunc', None)
    fullcaps = request.POST.get('fullcaps', None)
    newlineremover = request.POST.get('newlineremover', None)
    spaceremover = request.POST.get('spaceremover', None)
    charcount = request.POST.get('charcount', None)
    count = 0
    # check for puctuation
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,;-./:<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed+char
        d = {'analyzed_text': analyzed, 'purpose': 'removed puctuation'}
        text = analyzed
        count = count+1

    # check for capitalization
    if fullcaps == 'on':
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        d = {'analyzed_text': analyzed, 'purpose': 'Changed to UPPERCASE'}
        text = analyzed
        count = count+1
    # new line remover
    if newlineremover == 'on':
        analyzed = ""
        for char in text:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        d = {'analyzed_text': analyzed, 'purpose': 'Removed new lines'}
        text = analyzed
        count = count+1
    # Space remover
    if spaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(text):
            try:
                if text[index] == ' ' and text[index+1] == ' ':
                    pass
                else:
                    analyzed = analyzed + char
            except:
                pass
        d = {'analyzed_text': analyzed, 'purpose': 'Removed extra Spaces'}
        text = analyzed
        count = count+1
    # Character counter
    if charcount == 'on':
        analyzed = "No of Charaters = "+str(len(text))
        d = {'analyzed_text': analyzed, 'purpose': 'Characters Counted'}
        count = count+1
    # Done to show purpose accordingly
    if(count == 1):
        return render(request, 'analyze.html', d)
    elif(count > 1):
        d = {'analyzed_text': analyzed, 'purpose': 'Multi Formatting'}
        return render(request, 'analyze.html', d)
    else:
        return HttpResponse("<h1>Error<h1>")
