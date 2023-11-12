
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
import config.settings.base as settings

from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet

schema_view = get_swagger_view(title='Fl4shr API')

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/',schema_view),

]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)