from django.contrib import admin
from django.urls import path
from api.views import ImageManipulateViewSet, ImageViewSet
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^api/upload/', ImageView.as_view()),
]

# Register viewset
router = DefaultRouter()
router.register(r'images', ImageManipulateViewSet, base_name='images')
router.register(r'uploads', ImageViewSet, base_name='uploads') 
urlpatterns += router.urls

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



