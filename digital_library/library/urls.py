from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    BorrowBookAPIView,
    RateBookAPIView,
    CommentBookAPIView,
    BookListCreateAPIView,
    AuthorListCreateAPIView,
    PublisherListCreateAPIView,
    CategoryListCreateAPIView,
    RatingListCreateAPIView,
    CommentListCreateAPIView,
    BorrowListCreateAPIView,
)

urlpatterns = [
    path('api/books/<int:pk>/comment/', CommentBookAPIView.as_view(), name='comment-book'),
    path('api/books/<int:pk>/rate/', RateBookAPIView.as_view(), name='rate-book'),
    path('api/books/<int:pk>/borrow/', BorrowBookAPIView.as_view(), name='borrow-book'),

    path('api/borrows/', BorrowListCreateAPIView.as_view(), name='borrow-list'),
    path('api/comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('api/ratings/', RatingListCreateAPIView.as_view(), name='rating-list'),
    path('api/publishers/', PublisherListCreateAPIView.as_view(), name='publisher-list'),
    path('api/categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('api/authors/', AuthorListCreateAPIView.as_view(), name='author-list'),
    path('api/books/', BookListCreateAPIView.as_view(), name='book-list'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

