from django.conf.urls import url
from . import views

app_name = 'WME'
urlpatterns = [
    url(r'^contact/$', views.get_contact, name='get_contact'),
    url(r'^(?P<policyholder_id>[0-9]+)/child/$', views.get_child, name='get_child'),
    url(r'^(?P<policyholder_id>[0-9]+)/bank/$', views.get_bank, name='get_bank'),
url(r'^(?P<bank_id>[0-9]+)/disclosures/$', views.get_disclosures, name='get_disclosures'),

]


