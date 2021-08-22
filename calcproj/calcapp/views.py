from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
def index(request):
    return render(request,"index.html")
def submitquery(request):
    q=request.GET['query']
    ans=eval(q)
    # return HttpResponse(f"{q} = {eval(q)}")
    mydictionary={
        'q':q,
        'ans':ans,

    }
    # jsondict={
    #     'q':q
    # }
    # return JsonResponse(jsondict)
    return render(request,'index.html',context=mydictionary)
