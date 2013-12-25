from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


# Create your views here.



def index(request):
    template = loader.get_template('mysite/index.html')
    #context = RequestContext(request, {
    #    'latest_question_list': latest_question_list,
    #})  
    context=RequestContext(request,{}
        )
    return HttpResponse(template.render(context))

def about(request):
    return HttpResponse("This is the About page")
    
    
    