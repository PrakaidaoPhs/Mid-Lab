from django.db import models

class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True) #ไแดีหนัง
    title = models.CharField(max_length=100) # ชื่อ
    release_date = models.DateField() #วันที่เข้าฉาย
    duration = models.IntegerField()  # ระยะเวลาของภาพยนตร์ในนาที เช่น 250 นาที
    genre = models.CharField(max_length=50) # ประเภท
    director = models.CharField(max_length=100) # ผู้กำกับ
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True)

    def __str__(self):
        return self.title
