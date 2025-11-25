from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
    


    class Book(models.Model):
        title = models.CharField(max_length=200)
        publication_year = models.ForeignKey()
        author = models.ForeignKey( 

            Author, on_delete=models.CASCADE, 
            related_name="book"
            )
        
        def __str__(self):
            return f"{self.title} ({self.publication_year})"
        


        # Book Serializer
# ===========================
# Serializes all Book fields.
# Includes custom validation to ensure the publication_year is not in the future.