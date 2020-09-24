from rest_framework import generics
from ..models import Product
from ..api.serializers import ProductSerializer
from ..search import search, get_search_query


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q')
        if q is not None:
            return get_search_query(q)
        return super().get_queryset()
