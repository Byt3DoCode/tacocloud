from __future__ import unicode_literals
from rest_framework import viewsets, status, mixins

from book_model.models import books
from book_model.serializers import BookSerializer

# Create your views here.


class BookModelViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    throttle_scope = "book_model"

    def get_queryset(self):
        product = books.objects.all()
        return product
