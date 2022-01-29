from django.contrib import admin
from django.urls    import path, include


urlpatterns = [
    path('admin', admin.site.urls),
    path('users', include('awesome27.apps.users.urls')),
    path('products', include('awesome27.apps.products.urls')),
]