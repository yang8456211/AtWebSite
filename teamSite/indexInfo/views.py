from django.shortcuts import render

from django.shortcuts import render_to_response

def showIndex(request):
    return render_to_response('index.html')