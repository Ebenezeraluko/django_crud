from django.shortcuts import render

# Create your views here.


class PostListView(models.Model):

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )
