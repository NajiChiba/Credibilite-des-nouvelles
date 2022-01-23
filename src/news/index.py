'''import elasticsearch
from elasticsearch_dsl import Search




data_1 = {
    'title': 'breakin news',
    'body': 'loreampson',
}

def add_to_es():
    INDEX_NAME = 'news'
    ELASTIC_HOST = "http://localhost:9200"
    client = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])
    add_data = client.index(index = INDEX_NAME, body=data_1)
    print(add_data)

add_to_es()'''  