from django_filters import rest_framework as filters
from . import models

class CasamentoFilter(filters.FilterSet):
    approved = filters.BooleanFilter(field_name='approved')
    
    class Meta:
        model = models.Casamento
        fields = ['approved']