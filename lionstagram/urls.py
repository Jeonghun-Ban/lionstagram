from django.contrib import admin
from django.urls import path
import page.views
# media 사용시 필요
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page.views.home, name='home'),
    path('detail/<int:post_id>', page.views.detail, name='detail'),
    path('new', page.views.new, name='new'),
    path('delete/<int:post_id>', page.views.delete, name='delete'),
] + static('/media/', document_root=settings.MEDIA_ROOT)