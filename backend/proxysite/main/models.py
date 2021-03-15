from django.db import models


http, https, socks5, socks4 = 0 , 1, 2, 3,
proxyTypes = [('http','HTTP'),('https','HTTPS'),('socks5','SOCKS5'),('socks4','SOCKS4')]

class ProxyList(models.Model):
    ip = models.CharField(max_length = 100, blank = False)
    port = models.IntegerField(blank = False)
    proxyType = models.CharField(max_length = 100, choices = proxyTypes)
    country = models.CharField(max_length = 100)
    ping_to_google = models.FloatField()
    ping_to_yandex = models.FloatField()


class UpdateTimes(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    good_proxy = models.IntegerField()
    