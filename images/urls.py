from unicodedata import name
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('food/',views.food_images,name='food'),
    path('nairobi/',views.travel_images,name='travel'),
    path('nature/',views.nature_images,name='nature'),
    path('fashion/',views.fashion_images,name='fashion'),
    path('image_details/<int:image_id>',views.image_details,name='image.detail'),
    path('search_category/',views.search_images, name='search_images')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
