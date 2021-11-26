from django.db import models
from django.utils.encoding import smart_text


# Create your models here.
class Kind(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return smart_text(self.name)
    
    class Meta:
        verbose_name = 'Type of Film'
        verbose_name_plural = 'Types of Film'


class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.IntegerField()
    release_date = models.DateField()
    kind = models.ForeignKey('Kind', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return smart_text(self.title)


class Role(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return smart_text(self.name)


class Person(models.Model):
    given_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return smart_text(self.given_name + " " + self.last_name)


class FilmPerson(models.Model):
    film = models.ForeignKey('Film', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return smart_text(self.film.title
                          + " - "
                          + self.person.given_name
                          + " "
                          + self.person.last_name)
    
    class Meta:
        verbose_name = 'Film Person'
        verbose_name_plural = 'Film Cast'


class Season(models.Model):
    name = models.CharField(max_length=100)
    film = models.ForeignKey(
                             'Film',
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True,
                             limit_choices_to={'kind__name': 'Series'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return smart_text(self.film.title
                          + " - "
                          + self.name)


class Episode(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return smart_text(self.season.name
                          + "x"  
                          + str(self.number)
                          + ": "
                          + self.name)
