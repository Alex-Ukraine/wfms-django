from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True) # Не обязательно к заполнению
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)  # изменение при редактировании
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)