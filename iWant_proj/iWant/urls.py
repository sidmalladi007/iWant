from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.index, name='home'),
    url(r'^signup/$', views.sign_up, name='signup'),
    url(r'^new-account/$', views.create_account, name='newaccount'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.sign_in, name='login'),
    url(r'^logout/$', views.sign_out, name='logout'),
    url(r'^create-wish/$', views.new_wish, name='create'),
    url(r'^wish-added/$', views.add_wish, name='add'),
    url(r'^(?P<wish_id>[0-9]+)/$', views.detail, name='detail'),
]

# Handle signup and profile in one link.