from django.shortcuts import render,get_object_or_404,redirect
from .models import Image,Location,Category
from django.http import HttpResponse,Http404, request
from django.core.exceptions import ObjectDoesNotExist
import datetime as dt

# Create your views
def index(request):
    images =Image.objects.all()
    location =Location.objects.all()
    return render(request, 'index.html',{'images':images, 'location':location})


def search_images(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_images(search_term)
        message = f"{search_term}" 

        return render(request, 'search_images.html', {"message":message, "images":searched_images})

    else:
        message = 'you have not searched for any term'
        return render(request, 'search_images.html', {"message":message})

def image_details(requset,image_id):
    locations = Location.objects.all()

    try:
        image = get_object_or_404(Image, pk =image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'image_details.html', {'image':image, "locations":locations})

def fashion_images(request):
    try:
        images = Image.objects.filter(location =1)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'image_location.html', {'images':images})

def food_images(request):
  try:
    images = Image.objects.filter(location =2)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'image_location.html', {'images':images})

def travel_images(request):
  try:
    images = Image.objects.filter(location =3)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'image_location.html', {'images':images})

def nature_images(request):
  try:
    images = Image.objects.filter(location =4)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'image_location.html', {'images':images})                        
