from django.urls import path
from .views import ListTypeView, ListHairstyleView

urlpatterns = [

    path('type/', ListTypeView.as_view(), name='all-types'),
    path('hairstyle/', ListHairstyleView.as_view(), name='all-types'),

]
