__version__ = '0.1.0'

from graphql_scalars import scalars
from graphql_scalars.scalars import GraphQLDateTime, GraphQLVoid

all_scalars_defs = [GraphQLDateTime, GraphQLVoid]

__all__ = ['scalars', 'all_scalars_defs']
