import elasticsearch
from elasticsearch_dsl import Search
import pathlib

def add_data_to_elastic(title, content, fake):
    INDEX_NAME = 'news-index'

    ELASTIC_HOST = 'http://localhost:9200/'

    client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])

    data_1 = {
        'title': title,
        'body': content,
        'fake': fake,
    }

    client.index(index= INDEX_NAME, body= data_1)