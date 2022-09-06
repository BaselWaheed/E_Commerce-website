import elasticsearch
from elasticsearch_dsl import Search


ELASTIC_HOST = 'http://localhost:9200'
INDEXES= ['products']
client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])


def lookup(query, index='products', fields=['pro_name', 'pro_description']):
    if not query:
        return 
    results = Search(
        index=index).using(client).query("multi_match", fields=fields, fuzziness='AUTO', query=query)

    q_results = []

    for hit in results:
        data = {
            "slug": hit.pro_slug,
            "title": hit.pro_name,
            "description": hit.pro_description,
            "image" :hit.pro_image,
            "pro_price" :hit.pro_price,
            "pro_total_price" :hit.pro_total_price,
            "pro_status":hit.pro_status,
            "url" : hit.url,
        }
        q_results.append(data)
    return q_results