from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('fundlist/',views.user_page, name='fund'),
    path('nav/',views.navbarfunction,name='navbar'),
    path('registration/',views.register,name='form'),
    path('equity/',views.equity,name='equity'),
    path('debt/',views.debt,name='debt'),
    path('hybrid/',views.hybrid,name='hybrid'),
    path('postlist',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/(?P<pk>\d+)', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/(?P<pk>\d+)/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/(?P<pk>\d+)/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/(?P<pk>\d+)/publish/', views.post_publish, name='post_publish'),
    path('post/(?P<pk>\d+)/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/(?P<pk>\d+)/approve/', views.comment_approve, name='comment_approve'),
    path('comment/(?P<pk>\d+)/remove/', views.comment_remove, name='comment_remove'),
    path('list/',views.listf,name='listfund'),
    path('recommend/',views.recoma,name='recom'),
    # path('buy/(?P<pk>[0-9]+)/',views.buy,name='buy'),
    path('buy/',views.buy,name='buy1'),

]
