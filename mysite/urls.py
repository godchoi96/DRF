# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # shkim
#     path('', HomeView.as_view(), name='home'),
#     path('blog/', include('blog.urls')),
#     path('api/', include('api.urls')),
#     # DRF
#     path('api-auth/', include('rest_framework.urls')),
# ]

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api2/', include('api2.urls')),

    # path('', include(router.urls)),
    # 로그인 버튼 객체의 유무
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
