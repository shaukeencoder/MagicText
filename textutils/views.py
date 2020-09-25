from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator
translator = Translator()

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    transtext = request.POST.get('transtext', 'off')
    wordcount = request.POST.get('wordcount', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>.?/@#$%^&*~'''
        analyzed = ""     #blank string
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # Analyse the text
        return render(request, 'analyze.html', param)

    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    elif newlineremover == "on":
        analyzed = ""  # blank string
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        param = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analysed text
        return render(request, 'analyze.html', param)

    elif extraspaceremover == "on":
        analyzed = ""  # blank string
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        param = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        # Analysed text
        return render(request, 'analyze.html', param)

    elif wordcount == "on":
        analyzed = 1  # blank string
        for char in djtext:
            if char == " ":
                analyzed = analyzed + 1
        param = {'purpose': 'Total Words in The Text', 'analyzed_text': analyzed}
         # Analyse the text
        return render(request, 'analyze.html', param)

    elif charactercounter == "on":
        analyzed = 0 # blank string
        for index, char in enumerate(djtext):
            if not (djtext[index] == " "):
                analyzed = analyzed + 1
        param = {'purpose': 'Number Of Characters', 'analyzed_text': analyzed}
        # Analyse the text
        return render(request, 'analyze.html', param)

    elif transtext == "on":
        translations = translator.translate(djtext, dest='hi')
        analyzed = translations.text
        param = {'purpose': 'Your Translated Text', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    else:
        return HttpResponse('''<h2>Error!</h2> <br><a href='/'>Back to Home</a>''')




