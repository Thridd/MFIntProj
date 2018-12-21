from django.shortcuts import render
import json, os, sys
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from .models import *
from .forms import HomeForm

# Index page view function
def index(request):
    with open(os.path.dirname(sys.modules['__main__'].__file__) + 'json/content_api.json') as content:
        content_json = json.load(content)
        return HttpResponse(render(request, "motleyfool/index.html", {"content_data": content_json}, RequestContext(request)))

# Content page view function
def content(request):
    param = request.GET.get('q', '')
    if param is not None and param != '':
        paramInt = int(param)


        # If method is Post, save the form data
        if request.method == "POST":
            commentID = uuid.uuid4()
            articleID = request.POST['articleID']
            commentText = request.POST['comment']
            form = HomeForm(request.POST)
            form.commentID = uuid.uuid4()

            commentObj = Comment(commentID = commentID, articleID = articleID, text = commentText)
            commentObj.save()

        #Retrieve json data for the quotes and content json files.
        with open(os.path.dirname(sys.modules['__main__'].__file__) + 'json/content_api.json') as content:
            content_json = json.load(content)
        with open(os.path.dirname(sys.modules['__main__'].__file__) + 'json/quotes_api.json') as quotes:
            quotes_json = json.load(quotes)

        #If the get parameter is greater than the result array, redirect them to the homepage
        if len(content_json['results']) < paramInt or len(quotes_json) < paramInt:
            return redirect('/motleyfool/')


        #If method is GET, retrieve the comments for that article
        comments = Comment.objects.filter(articleID = content_json['results'][paramInt]['uuid']).order_by('date_posted')

        #Return all the display data necessary to the article page
        return HttpResponse(render(request, "motleyfool/article.html", {"content_data": content_json['results'][paramInt], "quotes_data": quotes_json[paramInt], 'comments': comments}, RequestContext(request)))
    #if the parameter doesnt exist, redirect to the home page
    else:
        return redirect('/motleyfool/')

