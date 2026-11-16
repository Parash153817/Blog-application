from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('create_blog/',views.create_blog_view,name='create_blog'),
    path('blog/<int:blog_id>/', views.blog_detail_view, name='blog_detail'),
    path('edit-blog/<int:blog_id>/',views.edit_blog_view,name='edit_blog'),
    path('delete-blog/<int:blog_id>/',views.delete_blog_view,name='delete_blog'),
    path('explore/',views.explore_blogs_view,name='explore_blogs'),
    path('profile/<int:user_id>/',views.profile_view,name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path(
    'blog/<int:blog_id>/comment/',views.add_comment_view,name='add_comment'),
]

