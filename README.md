# cdk-network-bastion

This project sets up a network infrastructure with a bastion host using AWS CDK in Python.

- The networking components are defined in the `infra` directory.
- The bastion host configuration is in the `infra` directory.

---

## **Getting Started**

### **1. Prerequisites**

Before working with this project, ensure the following tools are installed and configured:

1. **Python**:
   - Install Python 3.7 or higher.
   - Verify the installation:

     ```bash
     python --version
     ```

2. **AWS CLI**:
   - Install the AWS CLI and configure credentials for your AWS account:

     ```bash
     aws configure
     ```

3. **npm (Node.js)**:
   - Install Node.js, which includes npm.
     - [Download and install Node.js](https://nodejs.org/).
   - Verify the installation:

     ```bash
     npm --version
     ```

4. **AWS CDK Toolkit**:
   - Install the AWS CDK CLI globally:

     ```bash
     npm install -g aws-cdk
     ```

   - Verify the installation:

     ```bash
     cdk --version
     ```

5. **SSM Client**:
   - Ensure the AWS SSM plugin is installed for connecting to the bastion host.
   - Verify SSM:

     ```bash
     aws ssm start-session --target <bastion-instance-id>
     ```

---

## **Project Structure**

```plaintext
.
├── app.py                         # CDK application entry point
├── infra                          # Infrastructure configuration
│   ├── bastion_host_stack.py      # Bastion host stack definition
│   ├── network_stack.py           # Network stack definition
│   ├── __init__.py                # Marks infra as a Python module
│   ├── README.md                  # Documentation
├── bastion-resources              # Resources for bastion host setup
│   └── setup                      # Scripts for bastion host provisioning
├── requirements.txt               # Python dependencies
├── requirements-dev.txt           # Development dependencies
├── README.md                      # Project documentation
├── LICENSE                        # License for the project
```

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
