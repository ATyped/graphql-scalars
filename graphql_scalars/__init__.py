__version__ = '0.1.0'

from graphql_scalars import scalars
from graphql_scalars.scalars import GraphQLDateTime

all_scalars_defs = [GraphQLDateTime]

__all__ = ['scalars', 'all_scalars_defs']
