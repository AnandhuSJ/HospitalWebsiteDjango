from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^facility$', views.facility, name='facility'),
    url(r'^conta_ct$', views.conta_ct, name='conta_ct'),
    url(r'^post$', views.post, name='post'),
    url(r'^review$', views.review, name='review'),
    url(r'^appo$', views.appo, name='appo'),
    url(r'^con$', views.con, name='con'),
    url(r'^ema$', views.ema, name='ema'),
    url(r'^learn_more$', views.learn_more, name='learn_more'),
]
