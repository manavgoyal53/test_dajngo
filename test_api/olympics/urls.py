from django.urls import path
from . import views
urlpatterns = [
    path('schedule/',views.list_events),
    path('filter_events/<str:date>/<str:country>',views.filter_events),
    path('update_medal/<str:country>/<str:medal>',views.upadte_medal),
    path('get_medal_telly/',views.get_medal_counts),
    path('add_cheer/<str:country>',views.add_cheer),
    path('get_cheers',views.get_cheers)
]