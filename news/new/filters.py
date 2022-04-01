from django_filters import FilterSet, DateFilter
import django.forms
from .models import Post


# создаём фильтр
class PostFilter(FilterSet):
    time_public = DateFilter(lookup_expr='gte', widget=django.forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = {'author': ['exact'],
                  }
