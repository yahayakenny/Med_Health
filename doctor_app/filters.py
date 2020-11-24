import django_filters
from doctor_app.models import Doctor
from django_filters import CharFilter

class DoctorFilter(django_filters.FilterSet):
    name = CharFilter(field_name = 'name')
    class Meta:
        model = Doctor
        fields = ('name',)