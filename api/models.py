from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)
    publie = models.BooleanField(default=False)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date_creation']