from django.db import models
from mongoengine import Document
from mongoengine.fields import (
    StringField,
    ObjectIdField,
    IntField
)
# Create your models here.

class New(Document):
    meta = {"collection": "new"}
    title = StringField()
    body = StringField()
    fake = IntField()
