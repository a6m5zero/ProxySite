from .models import ProxyList, UpdateTimes
from rest_framework import viewsets, permissions, generics
from .serializers import ProxyListSerializer, TimeSerializer
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from wsgiref.util import FileWrapper
from io import StringIO 

class ProxyListSet(viewsets.ModelViewSet):
    serializer_class = ProxyListSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        ptype = self.request.query_params.get('type', None)
        print(self.request)
        if ptype is not None:
            return ProxyList.objects.filter(proxyType=ptype)
        else:
            return ProxyList.objects.all()
    
    @action(detail = False, methods = ['get'])
    def delete_all(self, request):
        ProxyList.objects.all().delete()
        return Response('Success')

class GetUpdateTime(viewsets.ModelViewSet):
    serializer_class = TimeSerializer
    permission_classes = [permissions.AllowAny]
    queryset = UpdateTimes.objects.all()

    @action(detail = False, methods = ['get'] )
    def update_time(self, request):
        UpdateTimes.objects.all().delete()
        g_proxy = ProxyList.objects.all().count()
        new_time = UpdateTimes(good_proxy = g_proxy)
        new_time.save()
        return Response('Time Updated')

class FileDownloadListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        ptype = self.request.query_params.get('filter', None)
        proxy_file = ''
        if ptype != None:
            queryset = ProxyList.objects.filter(proxyType=ptype)
        else:
            queryset = ProxyList.objects.all()
        filename = datetime.now().strftime(format = "%d%m%y_%H%M%S") + '.txt'
        for obj in queryset:
            proxy_file += (obj.ip + ':' + str(obj.port)+'\n')
        f = StringIO(proxy_file)
        response = StreamingHttpResponse(f, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response

