from django.views import View 
from django.http import JsonResponse
from django.shortcuts import render
from .models import Item

class Home(View):
  def get(self, request):
    items = Item.objects.all().values()
    return render(request,"home.html",{"items":items})
  def post(self, request):
    i = Item(name=request.POST["name"],code=request.POST["code"])
    i.save()
    items = Item.objects.all().values()
    return render(request,"home.html",{"items":items})

class ItemHandler(View):
  def get(self, request):
    items = list(Item.objects.all().values())
    return JsonResponse(items,safe=False)
  def post(self,request):
    i = Item(name=request.POST["name"],code=request.POST["code"])
    i.save()
    return JsonResponse({})
