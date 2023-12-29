from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

from conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    # apps
    path('accounts/', include('apps.accounts.urls'), name='accounts'),
    path('letters/', include('apps.letters.urls'), name='letters'),
]
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

