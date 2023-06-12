import django_filters
from .models import CommentView

class CommentFilter(django_filters.FilterSet):
    min_stars = django_filters.NumberFilter(field_name='stars', lookup_expr='gte')
    max_stars = django_filters.NumberFilter(field_name='stars', lookup_expr='lte')
    tour = django_filters.NumberFilter(field_name='tour')

    class Meta:
        model = CommentView
        fields = ['min_stars', 'max_stars']

    @property
    def ordering(self):
        ordering = self.request.query_params.get('ordering', None)
        if ordering:
            return [ordering, 'date']
        return ['stars', 'date']