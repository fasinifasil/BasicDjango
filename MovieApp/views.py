from django.shortcuts import render

# Create your views here.
def ListFunction(request):
    movieList = {'films': [
        {
            'title': 'maheshinte Prathikaaram',
            'year': 2016,
            'description': 'Mahesh, sets out to take revenge on the stranger as he feels insulted after the incident.',
            'Images'    :   'img_1.png',
            'success': True
        },
        {
            'title': 'Kumbalangi Nights',
            'year': 2019,
            'description': ' a story of four brothers – incomplete, disoriented and broken men leading unfulfilling lives in a pitiful abode on an islet in Kumbalangi. ',
            'Images': 'img_2.png',
            'success': True
        },
        {
            'title': 'Super Sharanya',
            'year': 2022,
            'description': 'Sharanya experiences her first love, makes new friends and enjoys her college days as she walks on the tricky path towards adulthood',
            'Images': 'img_3.png',
            'success': False
        }

    ]
    }

    return render(request,'Listpage.html',movieList)
def EditFunction(request):
    return render(request,'EditList.html')
def CreateFunction(request):
    if request.method == 'POST':
        print(request.POST.get('title'))
        print(request.POST.get('desc'))
    return render(request,'Createpage.html')