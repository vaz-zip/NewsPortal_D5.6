from django.urls import path
from .views import News, PostSearch, post_filter, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, \
    UserUpdateView

urlpatterns = [
    path('', News.as_view()),
    path('add/', PostCreateView.as_view(), name='_add'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('search', post_filter),
    path('edit/<int:pk>', PostUpdateView.as_view(), name='_edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('edit/', PostCreateView.as_view(), name='_edit'),
    path('search/', PostSearch.as_view(), name='_search'),
    path('user_edit/', UserUpdateView.as_view(), name='user_edit'),

]
