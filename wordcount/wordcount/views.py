from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):

    bigText = request.GET['bigText']
    #print(bigText)

    wordsSplit = bigText.split(" ")
    wordDiction = {}

    for w in wordsSplit:

        if w in wordDiction:
            wordDiction[w] += 1 # Increase the count in the dictionary
        else:
            wordDiction[w] = 1 # Create a new spot for the new word

    return render(request, 'count.html', {'bigText': bigText, 'wordSplitCount':len(wordsSplit), 'wordDiction':wordDiction.items()})
