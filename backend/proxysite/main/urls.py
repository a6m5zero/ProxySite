from rest_framework import routers
from .api import ProxyListSet, GetUpdateTime, FileDownloadListAPIView
from django.urls import include, path

router = routers.DefaultRouter()
router.register('api/get_proxy', ProxyListSet, 'proxylist')
router.register('api/update_time', GetUpdateTime, 'time' )




urlpatterns = router.urls

urlpatterns = [ 
    path('', include(router.urls)),
    path('api/file_download/', FileDownloadListAPIView.as_view(), name="filedownload"),
]
