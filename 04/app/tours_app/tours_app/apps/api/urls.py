from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views #manage_items, manage_item

app_name = 'api'
urlpatterns = [
    path('', views.manage_items, name="items"),
    path('<slug:key>', views.manage_item, name="single_item")
]
# urlpatterns = format_suffix_patterns(urlpatterns)
# </slug:key>