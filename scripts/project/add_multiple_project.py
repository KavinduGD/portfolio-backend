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
        "projectName": "Campus Travel Management System",
        "projectDescription": "Web system to manage campus travel requests.",
        "startedDate": "2024-01-01",
        "technologies": ["Python", "JavaScript", "Java"],
        "links": [
            {"linkName": "GitHub", "link": "https://example.com"}
        ],
        "architectureDescription": "Microservice-based architecture",
        "tags": ["web", "mern", "university"],
        "score": 90,
        "projectImages": [
            "../assets/projectImages/kts/p1.png",
            "../assets/projectImages/kts/p2.png"
        ],
        "architectureImages": [
            {
                "diagramName": "High Level Design",
                "image": "../assets/projectImages/kts/arch1.png"
            }
        ]
    },
    {
        "projectName": "Portfolio Website",
        "projectDescription": "Personal portfolio website.",
        "startedDate": "2023-05-01",
        "technologies": ["React", "CSS"],
        "links": [
            {"linkName": "Live", "link": "https://example.com"}
        ],
        "architectureDescription": "SPA architecture",
        "tags": ["portfolio", "frontend"],
        "score": 85,
        "projectImages": [
            "../assets/projectImages/portfolio/p1.webp",
            "../assets/projectImages/portfolio/p2.jpg"
        ],
        "architectureImages": [
            {
                "diagramName": "Site Map",
                "image": "../assets/projectImages/portfolio/arch1.png"
            },
            {
                "diagramName": "Component Diagram",
                "image": "../assets/projectImages/portfolio/arch2.png"
            },
            {"diagramName": "Deployment Diagram",
             "image": "../assets/projectImages/portfolio/arch3.png"
             }
        ]
    }
]

# ---------- LOOP ----------
success = 0
for project in projects:
    if add_single_project(client, project):
        success += 1

print(f"\n🎯 Finished: {success}/{len(projects)} projects added")
