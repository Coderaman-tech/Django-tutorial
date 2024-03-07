from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name='Mumbai'
    dest1.desc='City of dreams'
    dest1.price=700
    dest1.img='destination_9.jpg'

    dest2=Destination()
    dest2.name='Hyderabad'
    dest2.desc='Famous of Briyani'
    dest2.price=900
    dest2.img='destination_5.jpg'

    dest3=Destination()
    dest3.name='Bengaluru'
    dest3.desc='IT Hub of INDIA'
    dest3.price=1000
    dest3.img='destination_4.jpg'

    dests=[dest1,dest2,dest3]
    return render(request,"index.html",{'dests':dests})
