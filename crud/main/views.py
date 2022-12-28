import http
from django.http import HttpResponse
from django.shortcuts import render
from main.models import User,Logs
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
from django.http import QueryDict

# Create your views here.
def index(request):
    newsdata = User.objects.all()
    # articles per page
    per_page = 5
    # Paginator in a view function to paginate a queryset
    # show 4 news per page
    obj_paginator = Paginator(newsdata,per_page)
    # list of objects on first page
    first_page = obj_paginator.page(1).object_list
    # range iterator of page numbers
    page_range = obj_paginator.page_range

    context = {
    'obj_paginator':obj_paginator,
    'first_page':first_page,
    'page_range':page_range
    }
    #
    if request.method == 'POST':
        #getting page number
        page_no = request.POST.get('page_no', None) 
        results = list(obj_paginator.page(page_no).object_list.values())
        return JsonResponse({"results":results})

    return render(request, 'index.html',context)

def users(request):
    if request.method == 'GET':
        try:
            user_id =request.GET["user_id"]
            data = list(User.objects.filter(id=user_id).values())
            jsondata={
             'status':200,
             'success':'true',
             'results':data
            }
            Logs.objects.create(logtype='GET',text='Fetch user id '+user_id+'')
            return JsonResponse(jsondata,safe=False,status=200)
        except:
             jsondata={
             'status':200,
             'success':'true',
             'results':''
            }
             Logs.objects.create(logtype='GET',text='This user id '+user_id+' not present')
             return JsonResponse(jsondata,safe=False,status=500)
    if request.method == 'POST':
             username =request.POST["username"]
             firstname =request.POST["firstname"]
             lastname =request.POST["lastname"]
             email =request.POST["email"]
             try:
                User.objects.create(username=username,firstname=firstname,lastname=lastname,email=email)
                latest_id = User.objects.latest('id').id

                data = list(User.objects.filter(id=latest_id).values())
                jsondata={
                'status':200,
                'success':'true',
                'results':data
                }
                Logs.objects.create(logtype='POST',text='New user created with using email '+email+'')
                return JsonResponse(jsondata,safe=False,status=200)
             except:
                jsondata={
                'status':200,
                'success':'true',
                'results':'Something went wrong'
                }
                Logs.objects.create(logtype='POST',text='Something went wrong When Creating New User')
                return JsonResponse(jsondata,safe=False,status=500)

def updateuser(request):
     if request.method == 'POST':
        username =request.POST["username"]
        firstname =request.POST["firstname"]
        lastname =request.POST["lastname"]
        email =request.POST["email"]
        id =request.POST["id"]
        if  User.objects.filter(id=id).exists():
             try:
                User.objects.filter(id=id).update(username=username,firstname=firstname,lastname=lastname,email=email)
                data = list(User.objects.filter(id=id).values())
                jsondata={
                'status':200,
                'success':'true',
                'results':data
                }
                Logs.objects.create(logtype='PUT',text='User Updated with using email '+email+'')
                return JsonResponse(jsondata,safe=False,status=200)
             except:
                jsondata={
                'status':200,
                'success':'true',
                'results':'Something went wrong '
                }
                Logs.objects.create(logtype='PUT',text='Somthing Went wrong for updating User Id : '+id+' ')
                return JsonResponse(jsondata,safe=False,status=500)
        else:
             jsondata={
                'status':200,
                'success':'false',
                'results':'This user id is not present In our Records',
                }
             Logs.objects.create(logtype='PUT',text='User Id : '+id+' Not present is database and we are trying to update this id')
             return JsonResponse(jsondata,safe=False,status=200)
    
def delete(request):
    if request.method == 'POST':
        id =request.POST["id"]
        if  User.objects.filter(id=id).exists():
             try:
                User.objects.filter(id=id).delete()
                jsondata={
                'status':200,
                'success':'true',
                'results':'User Deleted successfully'
                }
                Logs.objects.create(logtype='DELETE',text='User Deleted successfully for User Id : '+id+' ')
                return JsonResponse(jsondata,safe=False,status=200)
             except:
                jsondata={
                'status':200,
                'success':'true',
                'results':'Something went wrong '
                }
                Logs.objects.create(logtype='DELETE',text='Somthing Went wrong for Deleting User Id : '+id+' ')
                return JsonResponse(jsondata,safe=False,status=500)
        else:
             jsondata={
                'status':200,
                'success':'false',
                'results':'',
                'message':'This user id is not present In our Records'
                }
             Logs.objects.create(logtype='DELETE',text='User Id : '+id+' not present In our Records')
             return JsonResponse(jsondata,safe=False,status=200)
    
def logs(request):
    newsdata = Logs.objects.all()
    # articles per page
    per_page = 5
    # Paginator in a view function to paginate a queryset
    # show 4 news per page
    obj_paginator = Paginator(newsdata,per_page)
    # list of objects on first page
    first_page = obj_paginator.page(1).object_list
    # range iterator of page numbers
    page_range = obj_paginator.page_range

    context = {
    'obj_paginator':obj_paginator,
    'first_page':first_page,
    'page_range':page_range
    }
    #
    if request.method == 'POST':
        #getting page number
        page_no = request.POST.get('page_no', None) 
        results = list(obj_paginator.page(page_no).object_list.values())
        return JsonResponse({"results":results})

    return render(request, 'logs.html',context)
