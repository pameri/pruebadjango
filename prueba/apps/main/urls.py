from django.conf.urls import patterns, url

urlpatterns = patterns('prueba.apps.main.views',
						url(r'^$', 'index_view', name='url_index'),
						)