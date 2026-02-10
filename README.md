# Portfolio Backend API

![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![ArgoCD](https://img.shields.io/badge/argocd-%23eb5b33.svg?style=for-the-badge&logo=argo&logoColor=white)

## 📌 Project Overview

This repository contains the **backend API** for a comprehensive portfolio website platform. The platform is designed as a microservices-based system consisting of:
1.  **Public Frontend**: Displaying the portfolio to the world.
2.  **Admin Panel**: Allowing the owner to manage content dynamically.
3.  **Backend API (This Repo)**: Powered by Node.js, Express, and TypeScript, serving data to both frontends.

The entire system is built with **DevOps** and **GitOps** best practices, featuring automated deployments to an **AWS EKS** cluster using **Argo CD** and infrastructure provisioning via **Terraform**.

---

## 🏗 Architecture

The system follows a cloud-native architecture deployed on AWS.

### Infrastructure & Deployment Flow
1.  **Infrastructure**: Provisioned using Terraform (EKS, VPC, etc.).
2.  **Containerization**: Applications are packaged into Docker images.
3.  **CI Pipeline (GitHub Actions)**:
    *   Builds and tests the application.
    *   Pushes Docker images to Docker Hub.
    *   Updates the specific environment overlay (stage/prod) in the **Manifest Repository**.
4.  **CD Pipeline (Argo CD)**:
    *   Monitors the Manifest Repository.
    *   Automatically syncs the new state to the EKS cluster.
    *   Zero-touch deployment for both Staging and Production environments.

### System Diagram
*(Refer to the architecture diagrams included in the project documentation for visual details on VPC peering, Load Balancers, and EKS node structure.)*

---

## 🚀 Features

*   **RESTful API**: Structured endpoints user, admin, projects, skills, and certificates.
*   **Authentication**: Secure admin authentication (likely JWT/Cookie based).
*   **Media Management**: Handling file uploads (local/cloud storage).
*   **Database**: Utilizes MongoDB with Mongoose for data modeling.
*   **Type Safety**: Written in TypeScript for robust development.
*   **Automated Testing**: Integrated Jest for unit/integration tests.

---

## 🛠 Tech Stack

*   **Runtime**: Node.js
*   **Framework**: Express.js
*   **Language**: TypeScript
*   **Database**: MongoDB
*   **DevOps**: Docker, Kubernetes (EKS), GitHub Actions, Argo CD, Terraform
*   **Tools**: ESLint, Prettier, Jest, Nodemon

---

## 📂 Project Structure

```bash
portfolio-backend/
├── .github/workflows/   # CI/CD Pipeline definitions
├── api_doc/             # OpenAPI/Swagger documentation
├── src/
│   ├── config/          # Database and app configuration
│   ├── controllers/     # Request handlers
│   ├── middleware/      # Express middleware (Auth, Error handling)
│   ├── models/          # Mongoose schemas
│   ├── routes/          # API route definitions
│   ├── utils/           # Utility functions
│   └── index.ts         # Application entry point
├── tests/               # Test suites
└── package.json         # Dependencies and scripts
```

---

## ⚙️ Getting Started

### Prerequisites
*   Node.js (v18+ recommended)
*   npm or yarn
*   MongoDB instance (Local or Atlas)
*   Docker (optional, for containerized run)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/KavinduGD/portfolio-backend.git
    cd portfolio-backend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Environment Configuration:**
    Create a `.env` file in the root directory (refer to `.env.example` if available) and configure:
    ```env
    PORT=3000
    MONGO_URI=mongodb://localhost:27017/portfolio
    JWT_SECRET=your_secret_key
    NODE_ENV=development
    ```

### Running Locally

*   **Development Mode** (with hot-reload):
    ```bash
    npm run dev
    ```

*   **Production Build**:
    ```bash
    npm run build
    npm start
    ```

*   **Run Tests**:
    ```bash
    npm test
    ```

---

## 🔄 GitOps Workflow

This project uses a **push-based CI** and **pull-based CD** workflow.

### continuous Integration (CI)
Defined in `.github/workflows/main.yaml`:
1.  **Trigger**: Merged Pull Request to `stage` or `main`.
2.  **Build & Test**: Installs dependencies, runs linting and tests.
3.  **Publish**: Builds the Docker image and pushes it to Docker Hub.
    *   Images are tagged with the Git Commit SHA.
4.  **Update Manifests**: The workflow automatically clones the `portfolio-manifests` repository and updates the `image` tag in the corresponding environment (`stage` or `prod`), implementing the **GitOps** pattern.

### Continuous Deployment (CD)
**Argo CD** detects the change in the manifest repository and syncs the new image version to the AWS EKS cluster, ensuring the live environment matches the desired state in Git.

---

## 📝 API Documentation

The API documentation is available in the `api_doc/` directory. It follows the OpenAPI specification.

---

## 🤝 Contributing

1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/amazing-feature`).
3.  Commit your changes (`git commit -m 'Add some amazing feature'`).
4.  Push to the branch (`git push origin feature/amazing-feature`).
5.  Open a Pull Request.

---

## 📄 License

This project is licensed under the ISC License.
