from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)
    month_to_learn = models.IntegerField()

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AbstractPerson(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100)

    class Meta:
        abstract = True

    # def save(self, *args, **kwargs):
    #     self.phone_number = self.phone_number.replace('0', '+996')
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Student(AbstractPerson):
    os_choices = [
        ('windows', 'Windows'),
        ('macOS', 'MacOS'),
        ('linux', 'Linux')
    ]
    work_study_place = models.CharField(max_length=100, blank=True, null=True)
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(max_length=100, choices=os_choices)

    def __str__(self):
        return self.preferred_os


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=100, blank=True, null=True)
    experience = models.DateField()
    student = models.ManyToManyField(Student, through='Course')

    def __str__(self):
        return self.main_work


class Course(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    # def get_end_date(self):
    #     months = self.date_started + Language.month_to_learn
    #     return months

    def __str__(self):
        return self.name

