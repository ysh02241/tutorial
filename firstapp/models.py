from django.db import models

# Create your models here.
class Curriculum(models.Model):
    #무조건 상속. 외우기.
    name = models.CharField(max_length=50)
    #문자열. 무조건 길이 설정해줘야 해서 max 쓰는거.

    def __str__(self):
        return '커리큘럼 : ' + self.name




