from django.contrib import admin
from .models import ProxyList, UpdateTimes
# Register your models here.

@admin.register(ProxyList)
class ProxyListAdmin(admin.ModelAdmin):
    list_display = ('ip','port','proxyType','country', 'ping_to_google', 'ping_to_yandex')
    list_filter = ('proxyType',)

@admin.register(UpdateTimes)
class UpdateTimesAdmin(admin.ModelAdmin):
    list_display = ('date', 'good_proxy')
    list_filter = ('date',)
