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
            "pro_slug": hit.pro_slug,
            "pro_name": hit.pro_name,
            "pro_description": hit.pro_description,
            "pro_image" :hit.pro_image,
            "pro_price" :hit.pro_price,
            "pro_total_price" :hit.pro_total_price,
            "pro_status":hit.pro_status,
            "url" : hit.url,
        }
        q_results.append(data)
    return q_results