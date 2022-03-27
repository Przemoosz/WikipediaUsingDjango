from django.urls import path
from . import views
# TODO
# After finishin path('forum1', views.forum,name='forum'), is to delete, also
# forum view is to delete
urlpatterns = [path('', views.home, name="home"),
               path('forum1', views.forum,name='forum'),
               path('forum/create', views.PostCreateView.as_view(), name='post_create'),
               path('forum',views.ForumView.as_view(),name="forum_view"),
               path('forum/user_posts',views.user_posts,name='user_post'),
               path('forum/<int:pk>',views.PostViewPk.as_view(),name='post'),
               path('forum/<int:pk>/delete', views.PostDeleteView.as_view(),name='delete'),
               path('forum/user_comments',views.UserComments.as_view(),name='user_comments'),
               path('forum/search',views.SearchView.as_view(),name='search'),
               path('forum/search/<str>',views.SearchViewResult.as_view(),name='search_result')]