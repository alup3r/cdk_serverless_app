from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    Tags,
    aws_dynamodb as dynamodb,
    aws_lambda as _lambda,
)
from constructs import Construct

class ServerlessAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # DynamoDB Table definition
        #
        products_table = dynamodb.Table(
                self, 'ProductsTable',
                partition_key=dynamodb.Attribute(
                    name='id',
                    type=dynamodb.AttributeType.STRING
                    ),
                removal_policy=RemovalPolicy.DESTROY)


        # Lambda Function definition and tags
        product_list_function = _lambda.Function(
                self, 'ProductListTable',
                runtime=_lambda.Runtime.PYTHON_3_12,
                handler='product_list_function.handler',
                code=_lambda.Code.from_asset('lambda_src'),
                environment={
                    'TABLE_NAME': products_table.table_name
                },
                timeout=Duration.minutes(15))


        # Grant read permissions on DynamoDB table to Lambda function 
        products_table.grant_read_data(product_list_function)


        Tags.of(products_table).add('env', 'dev')
        Tags.of(product_list_function).add('env', 'dev')
