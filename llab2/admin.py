from django.contrib import admin

from django.contrib import admin
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import CheckboxSelectMultiple
from django.forms import ModelForm

from .models import City, Route, Country

# Register your models here.


class RouteForm(ModelForm):
    def clean_cities(self):
        routes = Route.objects.all()

        if len(set(self.cleaned_data['cities'])) <= 1:
            raise ValidationError("Route must contain minimum 2 stations")
        for route in routes:
            if ((set(route.cities.all()) == set(self.cleaned_data['cities'])) and
                    self != route):
                raise ValidationError("There is already exact route in DB")
        return self.cleaned_data['cities']


class RouteAdmin(admin.ModelAdmin):
    form = RouteForm
    fields = ('number', 'cities')
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.site_url = '/home'
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Route, RouteAdmin)
