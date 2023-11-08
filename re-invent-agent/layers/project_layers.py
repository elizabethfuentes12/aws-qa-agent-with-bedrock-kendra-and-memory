import json
from constructs import Construct

from aws_cdk import (
    aws_lambda

)


class Layers(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #layer con beautiful soup y requests
        bs4_requests = aws_lambda.LayerVersion(
            self, "Bs4Requests", code=aws_lambda.Code.from_asset("./layers/bs4_requests.zip"),
            compatible_runtimes = [
                aws_lambda.Runtime.PYTHON_3_8,
                aws_lambda.Runtime.PYTHON_3_9,
                aws_lambda.Runtime.PYTHON_3_10,
                aws_lambda.Runtime.PYTHON_3_11], 
            description = 'BeautifulSoup y Requests')
        
        self.bs4_requests = bs4_requests


        bedrock = aws_lambda.LayerVersion(
            self, "Boto3+Bedrock", code=aws_lambda.Code.from_asset("./layers/boto3.1.28.62.zip"),
            compatible_runtimes = [
                aws_lambda.Runtime.PYTHON_3_8,
                aws_lambda.Runtime.PYTHON_3_9,
                aws_lambda.Runtime.PYTHON_3_10,
                aws_lambda.Runtime.PYTHON_3_11], 
            description = 'Boto3 with Bedrock API')

        self.bedrock = bedrock

        langchain = aws_lambda.LayerVersion(
            self, "Langchain", code=aws_lambda.Code.from_asset("./layers/langchain.zip"),
            compatible_runtimes = [
                aws_lambda.Runtime.PYTHON_3_8,
                aws_lambda.Runtime.PYTHON_3_9,
                aws_lambda.Runtime.PYTHON_3_10,
                aws_lambda.Runtime.PYTHON_3_11], 
            description = 'langchain')

        
        self.langchain = langchain


