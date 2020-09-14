from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    # 텍스트 길이 200내에서 작성 가능
    pub_date = models.DateTimeField()
    # 시간을 알아서 저장
    content = models.TextField()
    # 메서드 텍스트필드는 글자수 제한 