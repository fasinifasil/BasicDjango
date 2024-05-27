from django.shortcuts import render, redirect

from MovieApp.forms import MovieForm
from MovieApp.models import MovieDb


# Create your views here.
def ListFunction(request):
    alldata = MovieDb.objects.all()

    movieList = {'key':alldata}
    return render(request,'Listpage.html',movieList)
def EditFunction(request,pk):
    actform_Edit = MovieDb.objects.get(id=pk)
    movielist=MovieForm(instance=actform_Edit)
    if request.method=='POST':
        movieform = MovieForm(request.POST)
        if movieform.is_valid():
            movieform.save()
            return redirect('list')

    context={'key':movielist}
    return render(request, 'Createpage.html', context)


def DeleteFunction(request,pk):
    actform =MovieDb.objects.get(id=pk)
    actform.delete()

    return redirect('list')
    return render(request, 'EditList.html')
def CreateFunction(request):
    movieform=MovieForm()
    context={'key':movieform}
    # if request.method == 'POST':
    #     title=request.POST.get('Movie_Title')
    #     desc=request.POST.get('Description')
    #     year=request.POST.get('ReleasedYear')
    #     movie=MovieDb.objects.create(Movie_Title=title,ReleasedYear=year,Description=desc)
    #     movie.save()
    if request.method == 'POST':
        movieform=MovieForm(request.POST)
        if movieform.is_valid():
            movieform.save()
            return redirect('list')
    return render(request,'Createpage.html',context)