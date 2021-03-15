from rest_framework import serializers
from .models import ProxyList, UpdateTimes


class ProxyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProxyList
        # fields = '__all__' //Все поля
        fields = 'ip','port','proxyType','country', 'ping_to_google', 'ping_to_yandex'
        
class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateTimes
        fields = 'date', 'good_proxy'
