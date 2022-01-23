from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema
from . import views
urlpatterns = [
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
    path("news", views.check_news),
    path("feeling", views.check_sentiment),
]


