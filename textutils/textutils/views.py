# I have created this file - ASN
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html', )

    # return HttpResponse('<a target="_blank" href="http://127.0.0.1:8000/">Home</a><br>'
    #                     '<a target="_blank" href="http://127.0.0.1:8000/removepunc">Remove Punctuation</a><br>'
    #                     '<a target="_blank" href="http://127.0.0.1:8000/capfirst">Capitalize First</a><br>'
    #                     '<a target="_blank" href="http://127.0.0.1:8000/newlineremove">New Line Remove</a><br>'
    #                     '<a target="_blank" href="http://127.0.0.1:8000/spaceremove">Space Remover</a><br>'
    #                     '<a target="_blank" href="http://127.0.0.1:8000/charcount">Character Counter</a><br>')


def analyze(request):
    #Get the text
    djtext = (request.GET.get('text', 'default'))
    removepunc = (request.GET.get('removepunc', 'off'))
    print(removepunc)
    print(djtext)
    if removepunc == "on" and (len(djtext) > 0):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*+~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        #Analyse the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

