from django.db import models


class Creator(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    logo = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    style = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.style


class Creation(models.Model):
    title = models.CharField(max_length=255)
    prompt = models.TextField()
    description = models.TextField()
    link = models.URLField()
    artist = models.ForeignKey(
        Creator, on_delete=models.CASCADE, related_name="creations"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CreationHasCategory(models.Model):
    creation = models.ForeignKey(
        Creation, on_delete=models.CASCADE, related_name="categories"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="creations"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.creation.title} - {self.category.style}"
