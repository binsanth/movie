from django.http import HttpResponse
from django.shortcuts import render, redirect
from  . import models
from .models import movie_table
from .forms import update_form


# Create your views here.
def home(request):
    data=movie_table.objects.all()
    return render(request,'home.html',{'data':data})
def select(request,m_id):
    m=movie_table.objects.get(id=m_id)
    return render(request,'detail.html',{'id':m})
def add(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        dis=request.POST.get('dis',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        movie=movie_table(name=name,dis=dis,year=year,img=img)
        movie.save()
        return render(request,'add.html')
def update(request,id):
        movie=movie_table.objects.get(id=id)
        form=update_form(request.POST or None, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request,'update.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=movie_table.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')


