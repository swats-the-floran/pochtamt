from django.contrib import admin
from django.urls import include, path

from conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # apps
    path('accounts/', include('apps.accounts.urls'), name='accounts'),
    path('letters/', include('apps.letters.urls'), name='letters'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

