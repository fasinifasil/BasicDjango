from django.shortcuts import render, redirect

from MovieApp.forms import MovieForm
from MovieApp.models import MovieDb


# Create your views here.
def ListFunction(request):
    # alldata = MovieDb.objects.filter(ReleasedYear=2021).filter(Movie_Title='Home')
    # alldata = MovieDb.objects.order_by('-ReleasedYear')
    # alldata = MovieDb.objects.filter(cast__actorName='Mohanlal')
    # alldata = MovieDb.objects.filter(ReleasedYear__gt=2022)
    # alldata = MovieDb.objects.filter(Movie_Title__startswith='R')
    alldata = MovieDb.objects.all()

    movieList = {'key':alldata}
    return render(request,'Listpage.html',movieList)
def EditFunction(request,pk):
    actform_Edit = MovieDb.objects.get(id=pk)
    if request.POST:
        # title=request.POST.get('Movie_Title')
        # Desc=request.POST.get('Description')
        # Year=request.POST.get('ReleasedYear')
        # actform_Edit.Movie_Title=title
        # actform_Edit.ReleasedYear=Year
        # actform_Edit.Description=Desc
        # actform_Edit.save()
        # return redirect('list')
        forms = MovieForm(request.POST,instance=actform_Edit)
        if forms.is_valid():
            actform_Edit.save()
            return redirect('list')

    movie=MovieForm(instance=actform_Edit)

    context={'key':movie}
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
        movieform=MovieForm(request.POST,request.FILES)
        if movieform.is_valid():
            movieform.save()
            return redirect('list')
    return render(request,'Createpage.html',context)