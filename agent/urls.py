from django.contrib import admin
from django.urls import path, include
from accounts.views import UserRegisterView, home_view

from django.conf import settings
from django.conf.urls.static import static
from post import views


urlpatterns = [
    path('', home_view, name='home'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('order/', include('order.urls'))
]
