from django.db import models

# Create your models here.
from aplicatie1.models import Location

"""
 un nou model cu urmatoarele campuri:
 -  name         -> charfield50
 -  webstite     -> charfield100
 -  company_type -> chartfield10
 Trebuie sa realizati actiunile de:
 - listare date companii
 - adaugare date companie
 - modificare date companie
 - pagina de listare companii este accesibila din headerul oricarei pagini
"""


class Companies(models.Model):
    company_choices = (('SRL', 'S.R.L'),
                       ('SA', 'S.A.'))

    name = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    company_type = models.CharField(max_length=10, choices=company_choices)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
