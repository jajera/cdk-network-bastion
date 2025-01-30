# Infra Module

The `infra` directory contains the AWS CDK codebase for defining and managing the cloud infrastructure of the **CDK Network Bastion Project**. This project provisions a secure network architecture, including a VPC, subnets, security groups, and a bastion host for secure SSM access.

---

## **Structure**

The `infra` module consists of the following files:

```plaintext
infra/
├── __init__.py           # Marks the directory as a Python module
├── app.py                # Entry point for the CDK application
├── bastion_host_stack.py # Bastion host definition
└── network_stack.py      # Network infrastructure definition
```

### **File Descriptions**

- **`app.py`**:
  - Entry point for the AWS CDK application.
  - Instantiates the `NetworkStack` and `BastionHostStack` classes
    and synthesizes them into a CloudFormation template.

- **`network_stack.py`**:
  - Defines the network stack, including:
    - **VPC**: Public and private subnets for networking.
    - **Security Groups**: Firewall rules for secure access.

- **`bastion_host_stack.py`**:
  - Defines the bastion host stack, including:
    - **Bastion Host**: Secure instance for SSM access.
    - **IAM Policies**: Permissions for accessing Kafka and Secrets Manager.
    - **S3 Deployment**: Copies required resources to an S3 bucket.

- **`__init__.py`**:
  - Marks the `infra` directory as a Python module to enable imports.

---

## **Getting Started**

### **Prerequisites**

1. **Python Environment**:
   - Ensure Python 3.7 or higher is installed.
   - Activate your virtual environment:

     **Linux/macOS**:

     ```bash
     source .venv/bin/activate
     ```

     **Windows**:

     ```cmd
     .venv\Scripts\activate
     ```

---

## **How to Use**

**Note:** The following steps are only required when setting up the `infra` directory for the first time.

1. **Create the Directory**:
   Navigate to the project root and create the `infra` directory:

   ```bash
   mkdir -p src/infra
   cd src/infra
   ```

2. **Initialize the CDK Project**:
   Set up the directory as a CDK project:

   ```bash
   cdk init app --language python
   ```

3. **Add Required Files**:
   Add the `app.py`, `network_stack.py`, `bastion_host_stack.py`, and `__init__.py`
   files to define your infrastructure as described in the structure above.

4. **Install Dependencies**:
   Ensure all required Python packages are installed. From the `src/infra` directory, run:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. **Synthesize the Stack**:
   Run this command from the `src/infra` directory to generate the CloudFormation template from the CDK code:

   ```bash
   cdk synth
   ```

6. **Deploy the Stack**:
   Deploy the stack to your AWS account:

   ```bash
   cdk deploy --all
   ```

7. **Destroy the Stack**:
   To clean up and remove the resources:

   ```bash
   cdk destroy --all
   ```

---

## **Key Features**

- **VPC**:
  - A Virtual Private Cloud with public and private subnets for resource isolation.

- **Security Groups**:
  - Enforces secure access rules for different network layers.

- **Bastion Host**:
  - Provides secure SSM access to private resources in the VPC.

- **IAM Policies**:
  - Grants necessary permissions to access Kafka, Secrets Manager, and KMS.

- **S3 Deployment**:
  - Deploys necessary resources for the bastion host to an S3 bucket.

---

## **Troubleshooting**

1. **CDK Bootstrap Issues**:
   - Ensure AWS CLI is configured and the account/region has the required permissions.

2. **Deployment Errors**:
   - Check the CloudFormation console for detailed error logs and event histories.

3. **Connectivity Issues**:
   - Verify that the correct SSM session is used to access the bastion host.

---

## **Testing the Deployment**

After deploying, verify the infrastructure:

1. Confirm that the VPC and subnets are created successfully.
2. Connect to the bastion host using SSM to verify network access:

   ```bash
   aws ssm start-session --target <bastion-instance-id>
   ```

3. Check AWS Console for deployed resources and logs.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.
