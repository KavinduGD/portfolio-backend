"""
add_multiple_technologies.py
Add MULTIPLE technologies
"""

from portfolio_client import PortfolioClient
import os
import mimetypes

client = PortfolioClient()

# ---------- ADMIN LOGIN ----------
ok, _ = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)

if not ok:
    print("❌ Admin login failed")
    exit()

technologies = [
    {
        "technology": "JavaScript",
        "level": 90,
        "type": "Language",
        "image": "../assets/technologyImages/javascript.png"
    },
    {
        "technology": "TypeScript",
        "level": 85,
        "type": "Language",
        "image": "../assets/technologyImages/typescript.png"
    },
    {
        "technology": "Python",
        "level": 80,
        "type": "Language",
        "image": "../assets/technologyImages/python.png"
    },
    {
        "technology": "Java",
        "level": 75,
        "type": "Language",
        "image": "../assets/technologyImages/java.png"
    },
    {
        "technology": "HTML",
        "level": 100,
        "type": "Web Development",
        "image": "../assets/technologyImages/html.png"
    },
    {
        "technology": "CSS",
        "level": 95,
        "type": "Web Development",
        "image": "../assets/technologyImages/css.png"
    },
    {
        "technology": "Nodejs",
        "level": 90,
        "type": "Web Development",
        "image": "../assets/technologyImages/nodejs.png"
    },
    {
        "technology": "React",
        "level": 90,
        "type": "Web Development",
        "image": "../assets/technologyImages/react.png"
    },
    {
        "technology": "OpenAPI",
        "level": 90,
        "type": "Web Development",
        "image": "../assets/technologyImages/openapi.png"
    },
    {
        "technology": "Flask",
        "level": 85,
        "type": "Web Development",
        "image": "../assets/technologyImages/flask.png"
    },
    {
        "technology": "WordPress",
        "level": 80,
        "type": "Web Development",
        "image": "../assets/technologyImages/wordpress.png"
    },
    {
        "technology": "Docker",
        "level": 95,
        "type": "DevOps",
        "image": "../assets/technologyImages/docker.png"
    },
    {
        "technology": "Kubernetes",
        "level": 90,
        "type": "DevOps",
        "image": "../assets/technologyImages/kubernetes.png"
    },
    {
        "technology": "GitHub",
        "level": 85,
        "type": "DevOps",
        "image": "../assets/technologyImages/github.png"
    },
    {
        "technology": "GitHub Actions",
        "level": 85,
        "type": "DevOps",
        "image": "../assets/technologyImages/github_actions.png"
    },
    {
        "technology": "Jenkins",
        "level": 90,
        "type": "DevOps",
        "image": "../assets/technologyImages/jenkins.png"
    },
    {
        "technology": "Ansible",
        "level": 90,
        "type": "DevOps",
        "image": "../assets/technologyImages/ansible.png"
    },
    {
        "technology": "Terraform",
        "level": 90,
        "type": "DevOps",
        "image": "../assets/technologyImages/terraform.png"
    },
    {
        "technology": "GitLab CI/CD",
        "level": 80,
        "type": "DevOps",
        "image": "../assets/technologyImages/gitlab_ci_cd.png"
    },
    {
        "technology": "AWS CodePipeline",
        "level": 75,
        "type": "DevOps",
        "image": "../assets/technologyImages/aws_codepipeline.png"
    },
    {
        "technology": "Kustomize",
        "level": 85,
        "type": "DevOps",
        "image": "../assets/technologyImages/kustomize.png"
    },
    {
        "technology": "SonarQube",
        "level": 80,
        "type": "DevOps",
        "image": "../assets/technologyImages/sonarqube.png"
    },
    {
        "technology": "Machine Learning",
        "level": 75,
        "type": 'AI / Machine Learning',
                "image": "../assets/technologyImages/machine_learning.png"
    },
    {
        "technology": "Deep Learning",
        "level": 75,
        "type": 'AI / Machine Learning',
                "image": "../assets/technologyImages/deep_learning.png"
    },
    {
        "technology": "AI Agents",
        "level": 70,
        "type": 'AI / Machine Learning',
                "image": "../assets/technologyImages/ai_agents.png"
    },
    {
        "technology": "Figma",
        "level": 85,
        "type": "Design",
        "image": "../assets/technologyImages/figma.png"
    },
    {
        "technology": "Lucidchart",
        "level": 80,
        "type": "Design",
        "image": "../assets/technologyImages/lucidchart.png"
    },
    {
        "technology": "Draw.io",
        "level": 80,
        "type": "Design",
        "image": "../assets/technologyImages/drawio.png"
    },
    {
        "technology": "AWS",
        "level": 90,
        "type": "Cloud",
        "image": "../assets/technologyImages/aws.png"
    },
    {
        "technology": "Azure",
        "level": 75,
        "type": "Cloud",
        "image": "../assets/technologyImages/azure.png"
    },
    {
        "technology": "MySQL",
        "level": 85,
        "type": "Database",
        "image": "../assets/technologyImages/mysql.png"
    },
    {
        "technology": "MongoDB",
        "level": 85,
        "type": "Database",
        "image": "../assets/technologyImages/mongodb.png"
    },
    {
        "technology": "DynamoDB",
        "level": 80,
        "type": "Database",
        "image": "../assets/technologyImages/dynamodb.png"
    },
    {
        "technology": "Linux Commands",
        "level": 85,
        "type": "Linux",
        "image": "../assets/technologyImages/linux_commands.png"
    },
    {
        "technology": "Bash Scripting",
        "level": 75,
        "type": "Linux",
        "image": "../assets/technologyImages/bash_scripting.png"
    },
    {
        "technology": "Flutter",
        "level": 75,
        "type": "Mobile",
        "image": "../assets/technologyImages/flutter.png"
    }


]

url = f"{client.base_url}/technology"

for tech in technologies:
    if not os.path.exists(tech["image"]):
        print(f"❌ Image not found: {tech['image']}")
        continue

    image_path = tech["image"]
    mime_type, _ = mimetypes.guess_type(image_path)

    # fallback (important)
    if mime_type is None:
        mime_type = "application/octet-stream"

    data = {
        "technology": tech["technology"],
        "level": tech["level"],
        "type": tech["type"],
    }

    files = {
        "tech-icon-image": (
            os.path.basename(tech["image"]),
            open(tech["image"], "rb"),
            mime_type
        )
    }

    res = client.session.post(url, data=data, files=files)

    if res.status_code == 201:
        print(f"✅ {tech['technology']} added")
    else:
        print(f"❌ Failed: {tech['technology']}")
        print(res.status_code, res.text)
