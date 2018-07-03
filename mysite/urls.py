from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import polls.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',polls.views.home, name='home'),
    path('blog/', include('jpbs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
