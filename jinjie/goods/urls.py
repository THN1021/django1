from django.conf.urls import url, include
from goods import views as goods_views
urlpatterns = [
    url(r'^product/', goods_views.Acquire.as_view()),
]