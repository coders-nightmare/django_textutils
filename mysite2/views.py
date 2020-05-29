# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

# Code for practice
# def index(request):
#     return HttpResponse('''<h1>Hello Ritik</h1>
#     <br>
#     <br>
#     <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7" alt="youtube">Youtube.com</a> ''')


# def about(request):
#     return HttpResponse("<h1>About Ritik</h1>")


# def home(request):
#     file = open("home.txt")
#     return HttpResponse(file.readlines())
#     file.close()


def index(request):
    params = {'name': "Ritik", 'age': 20}
    return render(request, 'index.html', params)


def analyze(request):
    text = request.GET.get('text', None)
    removepunc = request.GET.get('removepunc', None)
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,; -./:<= >?@[\] ^ _`{ | }~'''
        analyzed_text = ""
        for char in text:
            if char not in punctuations:
                analyzed_text = analyzed_text+char
        d = {'analyzed_text': analyzed_text, 'purpose': 'removed puctuation'}
        return render(request, 'analyze.html', d)
    else:
        return HttpResponse("<h1>Error<h1>")
