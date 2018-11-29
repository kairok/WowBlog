from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()



class Category(models.Model):
    title=models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField("Тэг", max_length=50)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.title


class News(models.Model):
    user = models.ForeignKey(User,
            verbose_name="Author",
            on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                verbose_name="Category", on_delete=models.SET_NULL,
                null=True)
    title = models.CharField('Заголовок',max_length=100)
    text_min =models.TextField('Min Text', max_length=350)
    text=models.TextField("Text article")
    tag= models.ManyToManyField(Tag, verbose_name="Тэги")
    created = models.DateTimeField("date", auto_now_add=True)
    description = models.CharField("Discription", max_length=100)
    keywords = models.CharField("Key words", max_length=50)

    class Meta:
        verbose_name="Статья"
        verbose_name_plural="Статьи"

    def __str__(self):
        return self.title