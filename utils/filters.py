import django_filters
from cars.models.features import Features
from cars.models.cars import Cars


class CarsFilter(django_filters.FilterSet):
    # default for CharFilter is to have exact lookup_expr
    name = django_filters.CharFilter(lookup_expr='icontains')
    brand = django_filters.CharFilter(lookup_expr='icontains')
    pickup_time = django_filters.DateTimeFromToRangeFilter()
    dropoff_time = django_filters.DateTimeFromToRangeFilter()
    pickup_location = django_filters.CharFilter(lookup_expr='icontains')
    dropoff_location = django_filters.CharFilter(lookup_expr='icontains')

    # tricky part - how to filter by related field?
    # but not by its foreign key (default)
    # `to_field_name` is crucial here
    # `conjoined=True` makes that, the more tags, the more narrow the search
    features = django_filters.ModelMultipleChoiceFilter(
        queryset=Features.objects.all(),
        to_field_name='name',
        conjoined=True,
    )

    class Meta:
        model = Cars
        fields = ['name', 'brand', 'pickup_time', 'dropoff_time'
                  , 'pickup_location', 'dropoff_location', 'features'
        ]