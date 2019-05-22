from django.db import models

from django.conf import settings

# Create your models here.
class Post(models.Model):
    # id 필드를 선언하지 않을 경우 자동적으로 객체 생성시마다 1부터 순차 부여됨
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('publish')
    image = models.ImageField(upload_to='images/', blank=True)
    content = models.TextField()

    def __str__(self):
        return self.content[:20]

    def summary(self):
        return self.content[:100]