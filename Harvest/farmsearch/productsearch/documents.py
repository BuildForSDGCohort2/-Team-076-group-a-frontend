from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Product
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch

connections.create_connection()

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Product

        fields = [
            'title',
            'description',
            'price',
            'slug',
            'date_created',
            'date_updated',
            'quantity',
            'in_stock',
        ]


