from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField(max_length=5000)
    time=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class SolutionModel(models.Model):
    title=models.CharField(max_length=200)
    question=models.TextField(max_length=5000)
    code=models.TextField()
    comment=models.TextField(max_length=500)
    time=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title



class SingleModel(models.Model):
    class Meta:
        abstract=True
    def save(self, *args, **kwargs):
        self.pk=1
        kwargs.pop('force_insert',None)
        super().save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj,created=cls.objects.get_or_create(pk=1)
        return obj
    

class LinksModel(SingleModel):
    telegram=models.CharField(max_length=100)
    github=models.CharField(max_length=100)
    linkedin=models.CharField(max_length=100)

    def __str__(self):
        return "Havolalar"

class AboutMeModel(SingleModel):
    text=models.TextField(max_length=5000)
    def __str__(self):
        return "Men haqimda"