from django.conf.urls import url

from .views import tutorial_list,tutorial_detail,tutorial_list_published

urlpatterns = [
    url(r'^api/posts$', tutorial_list),
    url(r'^api/posts/(?P<pk>[0-9]+)$', tutorial_detail),
    url(r'^api/posts/published$', tutorial_list_published)
]