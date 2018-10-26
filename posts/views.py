from django.shortcuts import render
from  django.http import HttpResponse

from datetime import datetime

posts = [
    {
        "name" : "Como estudiar programacion a nivel intermedio",
        "user" : "Ulysses",
        "timeStamp": datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    },
    {
        "name" : "¿Son inportantes las bases?",
        "user" : "Ulises",
        "timeStamp": datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    },
    {
        "name" : "Naruto vs Sasuke",
        "user" : "Ulysses316",
        "timeStamp": datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    }
]

# Create your views here.
def lists_posts(request):
    contenido =[]
    for post in posts:
        contenido.append("""<p><strong>{name}<strong><p>
                            <p><small>{user}<i> {timeStamp}</i></small></p>
                            """.format(**post))
    return HttpResponse('<br>' .join(contenido))
