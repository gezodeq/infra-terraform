# infra-terraform

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Terraform](https://img.shields.io/badge/Terraform-%237B42F6.svg?style=flat-square&logo=terraform)](https://www.terraform.io/)

## Description

`infra-terraform` is a Terraform project designed to automate the provisioning and management of infrastructure across various cloud providers. It provides reusable modules and configurations for deploying common infrastructure components, such as virtual machines, networking resources, databases, and more. This project aims to streamline infrastructure setup, reduce manual configuration errors, and promote infrastructure as code (IaC) best practices.

This project is designed to be modular and extensible, allowing users to customize and adapt the configurations to meet their specific requirements.  It emphasizes idempotency, meaning the infrastructure will be brought to the desired state regardless of the current state.

## Features

*   **Multi-Cloud Support:**  Designed to be compatible with multiple cloud providers (e.g., AWS, Azure, Google Cloud Platform) with clear separation of provider-specific configurations.
*   **Modular Design:**  Utilizes Terraform modules to encapsulate reusable infrastructure components, promoting code reuse and maintainability.
*   **Idempotent Infrastructure:**  Ensures that Terraform configurations can be applied repeatedly without unintended side effects, guaranteeing consistent infrastructure states.
*   **Version Control:**  Leverages Git for version control, enabling tracking of changes, collaboration, and rollback capabilities.
*   **Parameterization:**  Employs Terraform variables to allow customization of infrastructure deployments without modifying the core configurations.
*   **State Management:**  Supports remote state management (e.g., using Terraform Cloud, AWS S3, Azure Storage Account) for collaboration and data persistence.
*   **Example Configurations:** Provides example configurations for deploying common infrastructure patterns, such as web applications, databases, and load balancers.
*   **Comprehensive Documentation:** Includes detailed documentation on how to use the modules, customize configurations, and troubleshoot common issues.
*   **Automated Testing (Future):**  Planned integration with testing frameworks like Terratest to validate infrastructure deployments.

## Technologies Used

*   **Terraform:**  Infrastructure as code tool for provisioning and managing cloud resources.
*   **HCL (HashiCorp Configuration Language):**  Configuration language used to define infrastructure resources in Terraform.
*   **Git:** Version control system for managing code changes and collaboration.
*   **Cloud Providers:** (Choose and list the providers your project supports)
    *   AWS (Amazon Web Services)
    *   Azure (Microsoft Azure)
    *   GCP (Google Cloud Platform)
*   **(Optional: List any other relevant technologies, e.g., Packer for image building, CI/CD tools, specific databases)**

## Installation

### Prerequisites

*   **Terraform:**  Install Terraform (version 1.0 or higher recommended) from [https://www.terraform.io/downloads.html](https://www.terraform.io/downloads.html).  Ensure that the `terraform` executable is in your system's `PATH`.
*   **Cloud Provider CLI:**  Install and configure the CLI for your chosen cloud provider(s) (e.g., AWS CLI, Azure CLI, Google Cloud SDK).  Ensure that the CLI is properly authenticated with your cloud provider account.
    *   **AWS CLI:** [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/)
    *   **Azure CLI:** [https://docs.microsoft.com/en-us/cli/azure/install-azure-cli](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
    *   **Google Cloud SDK:** [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)
*   **Git:**  Install Git from [https://git-scm.com/downloads](https://git-scm.com/downloads).

### Steps

1.  **Clone the Repository:**

    ```bash
    git clone <your-repository-url>
    cd infra-terraform
    ```

2.  **Configure Cloud Provider Credentials:**

    Configure your cloud provider credentials using the appropriate CLI.  Refer to your cloud provider's documentation for instructions. For example, for AWS:

    ```bash
    aws configure
    ```

    Or set environment variables like `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_REGION`.

    For Azure, use:

    ```bash
    az login
    az account set --subscription "<your_subscription_id>"
    ```

    For GCP, use:

    ```bash
    gcloud auth login
    gcloud config set project <your_project_id>
    ```

3.  **Navigate to the desired example or module directory:**

    ```bash
    cd examples/<your_example>  # or  cd modules/<your_module>
    ```

4.  **Initialize Terraform:**

    ```bash
    terraform init
    ```

    This command downloads the necessary provider plugins and initializes the Terraform working directory.

5.  **Plan the Infrastructure:**

    ```bash
    terraform plan
    ```

    This command shows you the changes that Terraform will make to your infrastructure. Review the plan carefully before applying it.

6.  **Apply the Configuration:**

    ```bash
    terraform apply
    ```

    This command applies the Terraform configuration and provisions the infrastructure.  You will be prompted to confirm the changes. Type `yes` to proceed.

7.  **(Optional) Destroy the Infrastructure:**

    ```bash
    terraform destroy
    ```

    This command destroys all the infrastructure resources created by Terraform. Use with caution!  You will be prompted to confirm the changes. Type `yes` to proceed.

## Usage

Refer to the `examples/` directory for example configurations. Each example provides a self-contained demonstration of how to use the modules and configurations in this project.  Customize the variables in the `terraform.tfvars` file or through environment variables to tailor the deployments to your specific needs.

For detailed information on specific modules, refer to the module's individual `README.md` file.

## Contributing

We welcome contributions to `infra-terraform`! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.