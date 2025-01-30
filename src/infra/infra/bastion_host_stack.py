import os
from aws_cdk import (
    CfnOutput,
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_s3_deployment as s3_deploy,
    aws_iam as iam,
)
from constructs import Construct


class BastionHostStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, vpc: ec2.Vpc, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.bastion = self._create_bastion_host(vpc)
        self._grant_permissions()

        self.bucket = s3.Bucket(self, "BastionHostBucket")
        self.bucket.grant_read_write(self.bastion.role)

        self._deploy_resources()

        CfnOutput(self, "BucketName", value=self.bucket.bucket_name)
        CfnOutput(
            self,
            "CopyMSKResources",
            value=f"aws s3 cp --recursive s3://{self.bucket.bucket_name} .",
            description=("Run as ec2-user to copy MSK resources onto the bastion host"),
        )

    def _create_bastion_host(self, vpc: ec2.Vpc) -> ec2.BastionHostLinux:
        """Creates a Bastion Host instance within the given VPC."""
        return ec2.BastionHostLinux(
            self,
            "BastionHost",
            vpc=vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2, ec2.InstanceSize.MICRO
            ),
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
        )

    def _grant_permissions(self) -> None:
        """Grants IAM permissions for Kafka, Secrets, and KMS."""
        self.bastion.role.add_to_principal_policy(
            iam.PolicyStatement(
                actions=[
                    "kafka:*",
                    "kafka-cluster:*",
                    "secretsmanager:GetSecretValue",
                    "kms:Decrypt",
                ],
                effect=iam.Effect.ALLOW,
                resources=["*"],
            )
        )

    def _deploy_resources(self) -> None:
        """Deploys MSK-related resources to an S3 bucket."""
        src_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "bastion-resources",
        )

        s3_deploy.BucketDeployment(
            self,
            "MskResourcesDeployment",
            sources=[s3_deploy.Source.asset(src_dir)],
            destination_bucket=self.bucket,
        )
