from portfolio_client import PortfolioClient
from tech_resolver import resolve_technology_ids
import os
import json
import mimetypes

client = PortfolioClient()

# ---------- LOGIN ----------
ok, _ = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)
if not ok:
    print("❌ Admin login failed")
    exit()


# ---------- PROJECT DATA ----------
project = {
    "projectName": "Campus Travel Management System",
    "projectDescription": "Web system to manage campus travel requests.",
    "startedDate": "2024-01-01",
    "technologies": ["Python", "JavaScript", "Java"],
    "links": [{
        "linkName": "GitHub",
        "link": "https://example.com"
    }],
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
}

# ---------- RESOLVE TECHNOLOGIES ----------
tech_ids = resolve_technology_ids(client, project["technologies"])

# ---------- BUILD MULTIPART ----------
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

# project images (MUST be exactly 2)
for img in project["projectImages"]:
    mime, _ = mimetypes.guess_type(img)
    files.append((
        "project-image",
        (os.path.basename(img), open(img, "rb"), mime)
    ))

# architecture images
for i, arch in enumerate(project["architectureImages"]):
    files.append((
        f"architecture[{i}][image]",
        (os.path.basename(arch["image"]), open(arch["image"], "rb"),
         mimetypes.guess_type(arch["image"])[0])
    ))
    data[f"architecture[{i}][diagramName]"] = arch["diagramName"]

# ---------- SEND ----------
url = f"{client.base_url}/project"
res = client.session.post(url, data=data, files=files)

if res.status_code == 200:
    print("✅ Project added")
else:
    print("❌ Failed")
    print(res.status_code, res.text)
