from django.contrib import admin
from .models import User, Author, Book, Category, Publisher, Borrow, Rating, Comment

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Borrow)
admin.site.register(Rating)
admin.site.register(Comment)
