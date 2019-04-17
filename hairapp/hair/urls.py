from django.urls import path
from .views import ListTypeView, ListHairstyleView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('type/', ListTypeView.as_view(), name='all-types'),
    path('hairstyle/', ListHairstyleView.as_view(), name='all-types'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
