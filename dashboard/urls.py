from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("web.urls",namespace="web")),
    path("product/",include("product.urls",namespace="product")),
    path("user/",include("user.urls",namespace="user")),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    