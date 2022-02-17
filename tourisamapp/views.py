from django.shortcuts import render

# Create your views here.
from tourisamapp.models import Person, News


def home(request):
    return render(request, 'html/home.html')


def places(request):
    return render(request, 'html/places.html')


def activity(request):
    return render(request, 'html/activity.html')


def gallery(request):
    return render(request, 'html/gallery.html')


def newsletter(request):
    return render(request, 'html/newsletter.html')


def accomodation(request):
    return render(request, 'html/accomodation.html')


def subscribe(request):
    return render(request, 'html/subscribe.html')


def trip(request):
    return render(request, 'html/trip.html')


def login(request):
    return render(request, 'html/login.html')


def save(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            a = Person(username=username, password=password)
            a.save()

            return render(request, 'html/login.html')

        except:
            return render(request, 'html/home.html')
    else:

        return render(request, 'html/home.html')



def register(request):
    return render(request, 'html/register.html')


def save1(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        cpassword = request.POST.get("cpassword")
        password = request.POST.get("password")
        try:
            a = Person(username=username, password=password, first_name=first_name, last_name=last_name, email=email, cpassword=cpassword)
            a.save()
            c="Registration Done Sucessfully"

            return render(request, 'html/register.html',{'c':c})
        except:
            return render(request, 'html/home.html')
    else:
        return render(request, 'html/login.html')

def save2(request):
    if request.method == "POST":
        email = request.POST.get("email")
        address = request.POST.get("address")
        address2 = request.POST.get("address2")
        city = request.POST.get("city")
        password = request.POST.get("password")
        zip = request.POST.get("zip")
        state=request.POST.get("state")
        check=request.POST.get("check")
        try:
            a = News(email=email, address=address, state=state, check=check, address2=address2, city=city, zip=zip, password=password)
            a.save()
            b="Request For Newsletter Send Successfully"
            return render(request, 'html/newsletter.html',{'b':b})
        except:
            return render(request, 'html/home.html')
    else:
        return render(request, 'html/home.html')


def applogin(request):
    if request.method == "POST":
        if Person.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            b = Person.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'html/home.html')


