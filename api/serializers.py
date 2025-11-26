from rest_framework import serializers
from .models import Book
from .models import Author
import datetime 

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book

        fields = "__all__"



 # Custom field-level validation

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author

        fields = ['name']


# - Author name
# - A nested list of all related books using BookSerializer
# The `books` field is read-only and generated automatically
# from the related_name in the Book model.