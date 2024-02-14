from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Baner(BaseModel):
    img = models.ImageField(upload_to="Baner/")
    title = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title



class Static(BaseModel):
    count_student = models.IntegerField(default=1)
    count_university = models.IntegerField(default=1)
    year_experienced = models.IntegerField(default=1)
    count_country = models.IntegerField(default=1)


    def __str__(self):
        return self.count_student



class Service(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ("order",)

    def __str__(self) -> str:
        return self.title



class Result(BaseModel):
    img = models.ImageField(upload_to='Result/')
    name = models.CharField(max_length=100)
    insitute_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)



class Contact(BaseModel):
    class DegreeChoise(models.TextChoices):
        BACHLOR = "bachlor", "Bakalavr"
        MASTER = "master", "Master"
    

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    choise_insitution = models.CharField(choices=DegreeChoise.choices, default= DegreeChoise.BACHLOR, max_length=100)
    phone = models.CharField(max_length=13)
    message = models.TextField()



class Review(BaseModel):
    img = models.ImageField(upload_to="Review/")
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)



class Social_acaount(BaseModel):
    icon = models.CharField(max_length=100)
    order = models.IntegerField(default=1)
    link = models.URLField()

    class Meta:
        ordering = ("order",)

