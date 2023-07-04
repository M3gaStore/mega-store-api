from django_filters import rest_framework as filters
from products.models import Product


class ProductsFilter(filters.FilterSet):
    id = filters.CharFilter(field_name="id", lookup_expr="exact")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    category = filters.CharFilter(field_name="category", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['id', 'name', 'category']