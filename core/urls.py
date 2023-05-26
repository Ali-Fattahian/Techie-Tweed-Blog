from django.urls import path
from . import views

urlpatterns = [
    path('', views.LatestPostsView.as_view(), name = 'homepage'),
    path('posts/', views.all_posts, name = 'posts'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name = 'post'),
    path('add-new-post/', views.AddNewPostView.as_view(), name="add-new-post"),
    path('update-post/<slug:slug>', views.UpdatePostView.as_view(), name = 'update-post'),
    path('read-later', views.ReadLaterView.as_view(), name = 'read-later'),
    path('about-us', views.get_about_page, name = 'about-us')
]
