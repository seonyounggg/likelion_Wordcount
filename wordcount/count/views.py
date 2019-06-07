from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    fulltext= request.GET['fulltext']

    word_list = fulltext.split()
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'result.html', {'inputtext' : fulltext, 'words' : len(word_list), 'dictionary' : word_dictionary.items()})