from django.conf.urls import url
from place import views

urlpatterns = [
	url(r'^$', views.PlaceList.as_view(), name = 'place_list'),
	url(r'^(?P<id>\d+)$', views.get_or_update_place, name = 'get_or_update_place'),
	url(r'^user-experiences/$', views.UserExperienceView.as_view(), name = 'user_experiences'),
]