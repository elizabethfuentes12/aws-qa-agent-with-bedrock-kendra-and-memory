from constructs import Construct

from aws_cdk import ( 
    aws_iam as iam, Stack,
    aws_kendra as kendra
)

from kendra_constructs.roles import KendraServiceRole


class KendraIndex(Construct):
    def __init__(self, scope: Construct, id: str, edition="DEVELOPER_EDITION", **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        stk = Stack.of(self)
        self.role = KendraServiceRole(self, "KSR")
        
        self.index = kendra.CfnIndex(self, "I",
            edition=edition,
            name=stk.stack_name,
            role_arn=self.role.arn,
        )
        self.index_id = self.index.attr_id

