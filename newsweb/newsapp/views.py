from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key='1cc9691b8a194ae3845258cd1eae2991')
    top = newsapi.get_top_headlines(sources='fox-news')

    l = top['articles']
    title = []
    description = []
    content = []
    img = []
    url = []

    for i in range(len(l)):
        f = l[i]
        title.append(f['title'])
        description.append(f['description'])
        content.append(f['content'])
        img.append(f['urlToImage'])
        url.append(f['url'])

    mylist = zip(title,description,content,img,url)
    return render(request,'newsapp/index.html',context={"mylist":mylist})


