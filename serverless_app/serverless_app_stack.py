from aws_cdk import (
    RemovalPolicy,
    Stack,
    Tags,
    aws_dynamodb as dynamodb,
)
from constructs import Construct

class ServerlessAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        products_table = dynamodb.Table(self, 'ProductsTable',
                                        partition_key=dynamodb.Attribute(
                                            name='id',
                                            type=dynamodb.AttributeType.STRING
                                        ),
                                        removal_policy=RemovalPolicy.DESTROY)


        Tags.of(products_table).add('env', 'dev')
