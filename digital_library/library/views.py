from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer
from .serializers import BookSerializer
from .models import Category,Publisher,Rating,Comment,Book, Borrow
from .serializers import CategorySerializer,PublisherSerializer,RatingSerializer,CommentSerializer,BorrowSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import BorrowSerializer
from .models import Rating
from .serializers import RatingSerializer


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class PublisherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
class RatingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
class BorrowListCreateAPIView(generics.ListCreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

class BorrowBookAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "الكتاب غير موجود"}, status=404)

        data = {
            "user": request.user.id,
            "book": book.id,
            "borrow_date": request.data.get("borrow_date"),
            "return_date": request.data.get("return_date"),
        }
        serializer = BorrowSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class RateBookAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "الكتاب غير موجود"}, status=404)


        rating, created = Rating.objects.update_or_create(
            user=request.user,
            book=book,
            defaults={'value': request.data.get('value')}
        )
        serializer = RatingSerializer(rating)
        return Response(serializer.data, status=201 if created else 200)
class CommentBookAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "الكتاب غير موجود"}, status=404)

        data = {
            "user": request.user.id,
            "book": book.id,
            "text": request.data.get("text"),
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
