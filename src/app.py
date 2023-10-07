"""Module for Intializing APP"""
from fastapi import FastAPI

from strawberry.fastapi import GraphQLRouter
from . import graphql

app = FastAPI()

app.include_router(GraphQLRouter(graphql.schema), prefix="/graphql")
