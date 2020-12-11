from src.client_factory import EC2Client

class RDS:
    def __init__(self, client):
        self._client = client
        """:type : pyboto3.rds"""

    def create_postgresql_instance(self):
        """Create a Amazon RDS PostgreSQL DB Instance"""
        print("Creating Amazon RDS PostgreSQL DB Instance...")
        self._client.create_db_instance()

    def create_db_security_group_and_rules(self):
        ec2_client = 

