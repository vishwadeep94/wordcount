from django.http import HttpResponse
from django.shortcuts import render

import operator

def homepage(request):
        return render(request, 'home.html')

def count(request):
    #Get is used to retrieve input data from website
    fulltext = request.GET['fulltext']
    #count spaces
    wordlist = fulltext.split()

    # counting the most repeated word
    worddictonary = {}

    for word in wordlist:
        if word in worddictonary:
            #Increment
            worddictonary[word] += 1
        else:
            #add the word to the dictionary
            worddictonary[word] = 1

    sorted_words = sorted(worddictonary.items(), key = operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist), 'sortedwords':sorted_words})

def about(request):
    return render(request, 'about.html')
