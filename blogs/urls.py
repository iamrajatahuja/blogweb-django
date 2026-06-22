from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('allposts',views.blogposts),

    # path('allposts/python-intro',views.python_intro),
    # path('allposts/django-basics',views.django_basic),
    # path('allposts/python-oops',views.python_oops),

    # Dynamic path segment
    # By default <blog> takes string, so order of the path matters
    # path('allposts/<blog>',views.blog_post)
    # path('allposts/<int:blog>', views.blog_post_by_number),
    # path('allposts/<str:blog>',views.blog_post)

    # slug type contains alphabets,numbers and hyphen
    path('allposts/<slug:blog>',views.blog_post, name='blog-post')
]