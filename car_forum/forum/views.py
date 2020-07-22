from django.shortcuts import render

posts = [
    {
        "author": "reuben Hawley",
        "title": "check out my first car",
        "content": "so i bought a new mercedes benz, check it out",
        "date_posted": "2020/07/23",
    },
    {
        "author": "Yorique jensen",
        "title": "me and my st",
        "content": "my st killing it at the track today",
        "date_posted": "2020/06/18",
    }
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, "forum/Home.html", context)
# Create your views here.


def about(request):
    context = {
        "posts": posts
    }
    return render(request, "forum/About.html",context)
