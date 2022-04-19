from django.urls import path
from support.views import support_list_view, support_detail_view

app_name='support'

urlpatterns = [
    path('',support_list_view, name='support-list'),
    path('<int:id>/', support_detail_view),
]