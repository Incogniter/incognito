import pygeoip


gip=pygeoip.GeoIP("GeoLiteCity.dat")
res =gip.record_by_addr('103.231.217.253')
for key, val in res.items():
    print('%s:%s' % (key,val))