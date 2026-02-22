from portfolio_client import PortfolioClient
from tech_resolver import resolve_technology_ids
import os
import json
import mimetypes


def add_single_project(client, project):
    """
    Upload ONE project.
    Returns True on success, False on failure.
    """

    # ---------- RESOLVE TECHNOLOGIES ----------
    tech_ids = resolve_technology_ids(client, project["technologies"])

    # ---------- BUILD FORM DATA ----------
    data = {
        "projectName": project["projectName"],
        "projectDescription": project["projectDescription"],
        "startedDate": project["startedDate"],
        "technologies": json.dumps(tech_ids),
        "links": json.dumps(project["links"]),
        "architectureDescription": project["architectureDescription"],
        "tags": json.dumps(project["tags"]),
        "score": str(project["score"]),
    }

    files = []

    # ---------- PROJECT IMAGES (exactly 2) ----------
    if len(project["projectImages"]) != 2:
        print(f"❌ {project['projectName']} must have exactly 2 project images")
        return False

    for img in project["projectImages"]:
        if not os.path.exists(img):
            print(f"❌ Missing project image: {img}")
            return False

        mime, _ = mimetypes.guess_type(img)
        files.append((
            "project-image",
            (os.path.basename(img), open(img, "rb"), mime)
        ))

    # ---------- ARCHITECTURE IMAGES ----------
    for i, arch in enumerate(project.get("architectureImages", [])):
        if not os.path.exists(arch["image"]):
            print(f"❌ Missing architecture image: {arch['image']}")
            return False

        mime, _ = mimetypes.guess_type(arch["image"])
        files.append((
            f"architecture[{i}][image]",
            (os.path.basename(arch["image"]), open(arch["image"], "rb"), mime)
        ))

        data[f"architecture[{i}][diagramName]"] = arch["diagramName"]

    # ---------- SEND ----------
    url = f"{client.base_url}/project"
    res = client.session.post(url, data=data, files=files)

    if res.status_code == 200:
        print(f"✅ {project['projectName']} added")
        return True
    else:
        print(f"❌ Failed: {project['projectName']}")
        print(res.status_code, res.text)
        return False


# ===================== MAIN =====================

client = PortfolioClient()

# ---------- LOGIN ----------
ok, _ = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)
if not ok:
    print("❌ Admin login failed")
    exit()

# ---------- PROJECT LIST ----------
projects = [
    {
        "projectName": "University Travel Management System",
        "projectDescription": "This project is a University Bus Travel Ticket System built using the MERN stack, designed to modernize and simplify campus transportation. The system features a responsive and intuitive interface developed with MUI and Tailwind CSS, secure user authentication using JWT, and real-time feedback through Toastify notifications. Administrators can easily create and manage bus routes, ensuring accurate and up-to-date travel information. Students can browse routes, purchase tickets online, and receive QR-code–based digital tickets for fast and secure validation. Integrated with the Google Maps API, the platform enables seamless route exploration, delivering an efficient, reliable, and user-friendly travel experience.",
        "startedDate": "2023-11-01",
        "technologies": ["JavaScript", "React", "Nodejs", "MongoDB", "AWS", "Docker", "GitHub", "Jenkins", "Ansible", "Terraform", "SonarQube", "Figma", "Lucidchart", "Linux Commands", "Bash Scripting"],
        "links": [
            {"linkName": "Backend GitHub",
                "link": "https://github.com/KavinduGD/kts_backend"},
            {"linkName": "User GitHub", "link": "https://github.com/KavinduGD/kts_user"},
            {"linkName": "Admin GitHub",
                "link": "https://github.com/KavinduGD/kts_admin"},
            {"linkName": "User Live Demo",
                "link": "https://kts-user.kavindu-gihan.tech/"},
            {"linkName": "Admin Live Demo",
                "link": "https://kts-admin.kavindu-gihan.tech/"},
            {"linkName": "Figma", "link": "https://www.figma.com/design/rpqLnXUTYQZGWuv7r85pA8/Untitled?node-id=0-1&t=Y2b2PwdIL1nsHPmx-1"},
            {"linkName": "Lucidchart", "link": "https://lucid.app/lucidchart/4f38daa2-d44d-4ef8-bb3d-9ab331462116/edit?viewport_loc=1919%2C-174%2C3828%2C2235%2C0_0&invitationId=inv_b0c27982-c016-492d-b22b-e2d79fcfdaff"},
            {"linkName": "YouTube", "link": "https://www.youtube.com/watch?v=IDwjNiLyGk8"}
        ],
        "architectureDescription": "This architecture implements a fully automated, secure, and scalable CI/CD pipeline on AWS. The infrastructure is provisioned using Terraform, with configuration management handled through Ansible. The system includes separate repositories for the backend, user service, and frontend. When developers push and merge code into the main branch, GitHub webhooks trigger a Jenkins pipeline that builds Docker images, runs tests, and performs static code analysis using SonarQube. After passing quality gates, a webhook triggers the deployment server to pull and redeploy the latest images. Users access the application via Route 53, an Application Load Balancer, and SSL certificates, ensuring secure and reliable access.",
        "tags": ["Full stack web development", "Devops", "CICD", "Architecture design", "Cloud", "Infrastructure as Code", "Linux", "Automation"],
        "score": 90,
        "projectImages": [
            "../assets/projectImages/kts/p1.png",
            "../assets/projectImages/kts/p2.png"
        ],
        "architectureImages": [
            {
                "diagramName": "System Architecture",
                "image": "../assets/projectImages/kts/system-arch.png"
            },
            {
                "diagramName": "Network Architecture",
                "image": "../assets/projectImages/kts/network-arch.png"
            }
        ]
    },
    {
        "projectName": "Audio Classification System with admin panel",
        "projectDescription": "Learn how to build a real-time audio classification model to enhance environmental awareness for hearing-impaired individuals using AWS SageMaker. This video walks through the development of a Convolutional Neural Network (CNN2D) model for sound classification, optimized for mobile deployment. With AWS cloud resources, including SageMaker, Lambda, and S3, this system enables scalable, low-latency sound detection, helping users identify crucial sounds like alarms or doorbells. The video covers data preprocessing, model training, and deployment steps, and demonstrates a user-friendly interface that allows non-experts to manage and adapt the model in real time. Ideal for those interested in applying machine learning to assistive technology.",
        "startedDate": "2024-07-01",
        "technologies": ["JavaScript", "React", "Flask", "AWS", "Docker", "Kubernetes", "GitHub", "GitHub Actions", "Deep Learning", "Lucidchart", "DynamoDB", "Flutter", "Linux Commands"],
        "links": [
            {"linkName": "Backend GitHub",
                "link": "https://github.com/KavinduGD/audio-backend"},
            {"linkName": "Admin GitHub",
                "link": "https://github.com/KavinduGD/audio-frontend"},
            {"linkName": "Admin Live Demo",
                "link": "https://audio-admin.kavindu-gihan.live"},
            {"linkName": "Figma", "link": "https://www.figma.com/design/5lqS6OpiAoC6R2cbm3R7fJ/Research-diagrams?node-id=0-1&t=gjWvFiq1Jb6W7dGu-1"},
            {"linkName": "Lucidchart", "link": "https://lucid.app/lucidchart/f90e1a49-442b-4329-b088-ba32419aace0/edit?viewport_loc=242%2C-298%2C3080%2C1490%2C0_0&invitationId=inv_e93115b4-3fb2-40f2-95cb-cae2b3c98125"},
            {"linkName": "YouTube", "link": "https://www.youtube.com/watch?v=CAm5Ql8ZELI"},
            {"linkName": "Research Paper",
                "link": "https://link.springer.com/chapter/10.1007/978-981-96-6932-5_23"},
        ],
        "architectureDescription": "The proposed system architecture consists of a cloud-based, scalable pipeline designed to support real-time environmental sound recognition for deaf and hard-of-hearing individuals. The architecture integrates a mobile application with a cloud backend hosted on AWS, enabling seamless data processing, model management, and real-time inference. Audio data uploaded via a web-based admin interface is stored in Amazon S3 and processed using AWS SageMaker for feature extraction and model training. Trained models are deployed through SageMaker endpoints and accessed via AWS Lambda and API Gateway for low-latency predictions. This modular architecture ensures scalability, flexibility, and accessibility while allowing non-technical administrators to manage and deploy models efficiently.",
        "tags": ["Full stack web development", "Devops", "CICD", "Architecture design", "Cloud", "Deep Learning", "ECS", "Flutter", "Audio Processing", "ML Ops"],
        "score": 85,
        "projectImages": [
            "../assets/projectImages/audio/p1.png",
            "../assets/projectImages/audio/p2.png"
        ],
        "architectureImages": [
            {
                "diagramName": "System Architecture",
                "image": "../assets/projectImages/audio/system-arch.png"
            },
            {
                "diagramName": "Flow Diagram",
                "image": "../assets/projectImages/audio/flow-arch.png"
            },

        ]
    },
    {
        "projectName": "Portfolio Website with Gitops",
        "projectDescription": "This project is a portfolio website platform composed of three services: a public frontend, a backend API, and an admin panel that allows the owner to manage and update portfolio content dynamically. The system is fully integrated with DevOps and GitOps practices, enabling automated and reliable deployments without manual intervention. All cloud infrastructure is provisioned using Terraform, with workloads managed on an AWS-based Kubernetes cluster. The backend is built with TypeScript and Express, while both the frontend and admin interfaces are developed using TypeScript and React. Through this project, I gained hands-on experience with TypeScript, CI/CD pipelines, and GitOps-driven automation, resulting in a seamless, production-ready system.",
        "startedDate": "2025-11-01",
        "technologies": ["JavaScript", "TypeScript", "React", "Nodejs", "MongoDB", "AWS", "Docker", "Kubernetes", "Kustomize", "Terraform", "GitHub", "GitHub Actions", "ArgoCD", "Lucidchart", "OpenAPI", "Bash Scripting", "Linux Commands"],
        "links": [
            {"linkName": "Backend GitHub",
                "link": "https://github.com/KavinduGD/portfolio-backend"},
            {"linkName": "Frontend GitHub",
                "link": "https://github.com/KavinduGD/portfolio-frontend"},
            {"linkName": "Admin GitHub",
                "link": "https://github.com/KavinduGD/portfolio_admin"},
            {"linkName": "Infra GitHub",
                "link": "https://github.com/KavinduGD/portfolio-infra"},
            {"linkName": "Manifest GitHub",
                "link": "https://github.com/KavinduGD/portfolio-manifests"},
            {"linkName": "Frontend Live Demo",
                "link": "https://kavindu-gihan.online/"},
            {"linkName": "Admin Live Demo",
                "link": "https://admin.kavindu-gihan.online/"},
            {"linkName": "Lucidchart", "link": "https://lucid.app/lucidchart/a271f945-410d-4e4f-8e03-0017d28997c2/edit?viewport_loc=4764%2C-1252%2C5104%2C2980%2C0_0&invitationId=inv_2f892674-66b2-4607-9dab-595ba1438a70"},
            {"linkName": "OpenAPI",
                "link": "http://portfolio-openapi-doc.s3-website.ap-south-1.amazonaws.com"},
        ],
        "architectureDescription": "The system is deployed on an AWS EKS cluster and follows GitOps principles for fully automated application delivery. It consists of three main code repositories: frontend, admin, and backend. When developers push code to the stage or production branches, GitHub Actions pipelines build Docker images and push them to the corresponding container registry. Argo CD continuously monitors the Git repositories and automatically synchronizes application state with the EKS cluster for both staging and production environments. Infrastructure is provisioned using Terraform, ensuring consistent and reproducible environments. Applications run as Kubernetes workloads and are exposed externally through Ingress-managed load balancers, enabling scalable, reliable, and zero-manual-intervention deployments.",
        "tags": ["Full stack web development", "Devops", "CICD", "Architecture design", "Cloud", "GitOps", "Container Orchestration", "Linux", "Infrastructure as Code"],
        "score": 100,
        "projectImages": [
            "../assets/projectImages/portfolio/p1.png",
            "../assets/projectImages/portfolio/p2.png"
        ],
        "architectureImages": [
            {
                "diagramName": "Cluster Architecture",
                "image": "../assets/projectImages/portfolio/cluster-arch.png"
            },
            {
                "diagramName": "System Architecture",
                "image": "../assets/projectImages/portfolio/system-arch.png"
            },
            {"diagramName": "Argocd Diagram",
             "image": "../assets/projectImages/portfolio/argo-arch.png"
             }
        ]
    },
    {
        "projectName": "Project using wso2 services",
        "projectDescription": "This is a cloud-based Recipe Management System built with React and Node.js. Users can securely create, view, update, and delete recipes. Authentication is handled using Asgardeo. Both frontend and backend services are deployed on WSO2 Choreo, ensuring secure, scalable, and cloud-native application management.",
        "startedDate": "2026-02-22",
        "technologies": ["JavaScript", "React", "Nodejs", "MongoDB", "GitHub", "Lucidchart",],
        "links": [
            {"linkName": "Backend GitHub",
                "link": "https://github.com/KavinduGD/portfolio-backend"},
            {"linkName": "Frontend GitHub",
                "link": "https://github.com/KavinduGD/recipe_frontned"},
            {"linkName": "Frontend Live Demo",
                "link": "https://436f4379-7f55-44b5-b30e-7c69c9573686.e1-us-east-azure.choreoapps.dev/"},
        ],
        "architectureDescription": "The system consists of a React frontend, Node.js backend API, and Asgardeo for authentication. The frontend communicates with the backend using secured REST APIs. Users authenticate through Asgardeo and receive access tokens. WSO2 Choreo manages deployment, service connectivity, and cloud infrastructure for both application components.",
        "tags": ["Full stack web development", "Cloud", "API Management", "Authentication"],
        "score": 80,
        "projectImages": [
            "../assets/projectImages/wso2/p1.png",
            "../assets/projectImages/wso2/p2.png"
        ],
        "architectureImages": [
            {
                "diagramName": "Cluster Architecture",
                "image": "../assets/projectImages/wso2/arch.png"
            },
        ]
    }
]

# ---------- LOOP ----------
success = 0
for project in projects:
    if add_single_project(client, project):
        success += 1

print(f"\n🎯 Finished: {success}/{len(projects)} projects added")
