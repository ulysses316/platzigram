from django.shortcuts import render
from  django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from datetime import datetime

posts = [
    {
        "name" : "Como estudiar programacion a nivel intermedio",
        "user" : "Ulysses",
        "timeStamp": datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        "img": "https://images.unsplash.com/photo-1460626399219-57a00a2361cb?ixlib=rb-0.3.5&s=7486c030f52264deaa23eadbeb92f48b&auto=format&fit=crop&w=750&q=80"
    },
    {
        "name" : "¿Son inportantes las bases?",
        "user" : "Ulises",
        "timeStamp": datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        "img": "https://images.unsplash.com/photo-1460750860062-82a52139a0d6?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=ad6f8d20e4b6da905c5bb18ea656ce60&auto=format&fit=crop&w=750&q=80"
    },
    {
        "name" : "Naruto vs Sasuke",
        "user" : "Ulysses316",
        "timeStamp": datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        "img": "https://images.unsplash.com/photo-1453668069544-b8dbea7a0477?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=7bdf2569bc30ad7aacdf645f834c766c&auto=format&fit=crop&w=750&q=80"
    }
]

# Create your views here.
@login_required
def lists_posts(request):
    return render(request, "posts/feed.html", {"posts" : posts})
