# To see media items locally, since user-uploaded content is assumed to exist in a production context
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin (Hardening the admin security)
    # using admin-honeypot to catch those trying to access the admin page.
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path('bookstore-site-admin/', admin.site.urls),

    # User management
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")),

    # Local apps
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# We only want Debug Toolbar to appear if DEBUG is true
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns



