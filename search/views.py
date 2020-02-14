from django.shortcuts import render

from .models import Question

def index(request):
    try:
        search_result = Question.objects.filter(question_stem__contains=request.POST['query'])
        context={
            'search_result':search_result,
            'previous_query':request.POST['query'],
        }
        return render(request,'search/index.html',context)
    except:
        return render(request,'search/index.html')