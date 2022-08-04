from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    position = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='images/testimonial/')

    def __str__(self):
        return self.name


class Requirement(models.Model):
    requirement = models.CharField(max_length=255)
    requirement_am = models.CharField(max_length=255, default='')
    requirement_or = models.CharField(max_length=255, default='')
    requirement_tg = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.requirement


class Course(models.Model):
    requirements = models.ManyToManyField(Requirement, related_name='courses')
    name = models.CharField(max_length=255)
    name_or = models.CharField(max_length=255, default='')
    name_am = models.CharField(max_length=255, default='')
    name_tg = models.CharField(max_length=255, default='')

    aka = models.CharField(max_length=255, null=True)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return str(self.name) + ' - ' + str(self.phone)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    images = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class About(models.Model):
    image = models.ImageField(upload_to='images/about/')
    text = models.TextField()

    def __str__(self):
        return self.text
