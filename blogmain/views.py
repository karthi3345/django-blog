from django.http import HttpResponse
from django.shortcuts import render


def home(request): #request eduku na  #Without request, your view cannot know who is making the request, what data was sent, or what URL was called.
    #Django always passes this automatically when it calls your view.
    return render(request, "home.html") # http direct reuest edukum response kudukumnu   render function dierctly template file ku poi render pannuumnu solrum
    #render function 3 arguments edukum 1st request 2nd template name 3rd optional context dictionary
    #context dictionary la data pass panni template la display pannanum na atha kudukkalam
    #argument na function ku pass pannanum values and atha function atha eduthu use pannum