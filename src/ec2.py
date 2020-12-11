RDS_SECURITY_GROUP_NAME = "my-rds-public-sg"


class EC2:
    def __init__(self, client):
        self._client = client
        """:type : pyboto3.ec2"""

    def create_security_group(self):
        print("Creating RDS Securyt Group with name " + RDS_SECURITY_GROUP_NAME)
        return self._client.create_security_group(
            GroupName=RDS_SECURITY_GROUP_NAME,
            Description='RDS security group for public access',
            VpcId='vpc-5eb16d23'
        )

    def add_inbound_rule_to_sg(self, security_group_id):
        print("Adding inbound access rule to security group " + security_group_id)
        self._client.authorize_security_group_ingress(
            GroupId=security_group_id
        )