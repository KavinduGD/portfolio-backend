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
        "technology": "Python",
        "level": 90,
        "type": "programming",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "JavaScript",
        "level": 80,
        "type": "programming",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "Java",
        "level": 70,
        "type": "programming",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "TypeScript",
        "level": 80,
        "type": "programming",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "HTML",
        "level": 90,
        "type": "web",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "CSS",
        "level": 90,
        "type": "web",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "React",
        "level": 90,
        "type": "web",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "Express",
        "level": 80,
        "type": "web",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "Flask",
        "level": 70,
        "type": "web",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "WordPress",
        "level": 70,
        "type": "web",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "OpenAPI",
        "level": 80,
        "type": "web",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "Docker",
        "level": 80,
        "type": "devops",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "Kubernetes",
        "level": 70,
        "type": "devops",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "GitHub",
        "level": 90,
        "type": "devops",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "GitHub Actions",
        "level": 80,
        "type": "devops",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "Jenkins",
        "level": 70,
        "type": "devops",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "Ansible",
        "level": 60,
        "type": "devops",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "Terraform",
        "level": 70,
        "type": "devops",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "GitLab CI/CD",
        "level": 70,
        "type": "devops",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "AWS CodePipeline",
        "level": 60,
        "type": "devops",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "Machine Learning",
        "level": 70,
        "type": "ai_ml",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "Deep Learning",
        "level": 70,
        "type": "ai_ml",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "AI Agents",
        "level": 60,
        "type": "ai_ml",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "Figma",
        "level": 70,
        "type": "design",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "Lucidchart",
        "level": 70,
        "type": "design",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "Draw.io",
        "level": 80,
        "type": "design",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "AWS",
        "level": 80,
        "type": "cloud",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "Azure",
        "level": 60,
        "type": "cloud",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "MySQL",
        "level": 80,
        "type": "database",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "MongoDB",
        "level": 80,
        "type": "database",
        "image": "../assets/technologyImages/git.jpg"
    },
    {
        "technology": "Linux Commands",
        "level": 90,
        "type": "linux",
        "image": "../assets/technologyImages/react.webp"
    },
    {
        "technology": "Bash Scripting",
        "level": 80,
        "type": "linux",
        "image": "../assets/technologyImages/git.jpg"
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
