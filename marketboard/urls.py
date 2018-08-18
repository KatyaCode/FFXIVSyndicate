from django.urls import re_path

from marketboard import views
from marketboard.models import SERVER_LIST

server_list_re = '|'.join([server for server in SERVER_LIST])

urlpatterns = [
    re_path(r'^(?P<server_name>' + server_list_re + ')$', views.home, name='home'),
]
