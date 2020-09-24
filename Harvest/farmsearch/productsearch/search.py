from elasticsearch_dsl.query import Q
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections

connections.create_connection(alias='host', hosts=['localhost'], timeout=60)


def get_search_query(phrase):
    s = Search(using='host')
    response = Q("match", query=phrase)
    s.query(response)
    result = s.execute(ignore_cache=True)
    return result


def search(phrase):
    return get_search_query(phrase).to_queryset()

# def bulk_indexing():
#         ProductDocument.init()
#         es = Elasticsearch()
#         bulk(client=es, actions=(p.indexing() for p in Product.objects.all().iterator()))
