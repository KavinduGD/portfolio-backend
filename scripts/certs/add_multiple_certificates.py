from portfolio_client import PortfolioClient
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

certificates = [
    {
        "name": "AWS Certified Cloud Practitioner12",
        "issuer": "Amazon Web Services",
        "issueDate": "2024-02",
        "credentialsId": "AWS-001",
        "certificateLink": "https://example.com/aws",
        "tags": ["aws", "cloud"],
        "score": 90,
        "image": "../assets/certImages/azure.png",
    },
    {
        "name": "12Docker Foundations",
        "issuer": "Docker Inc",
        "issueDate": "2023-11",
        "credentialsId": "DOC-123",
        "certificateLink": "https://example.com/docker",
        "tags": ["docker", "devops"],
        "score": 85,
        "image": "../assets/certImages/aws.jpeg",
    },
]

url = f"{client.base_url}/certificate"

for cert in certificates:
    if not os.path.exists(cert["image"]):
        print(f"❌ Image not found: {cert['name']}")
        continue

    data = {
        "name": cert["name"],
        "issuer": cert["issuer"],
        "issueDate": cert["issueDate"],
        "credentialsId": cert["credentialsId"],
        "certificateLink": cert["certificateLink"],
        "tags": json.dumps(cert["tags"]),
        "score": str(cert["score"]),
    }

    mime, _ = mimetypes.guess_type(cert["image"])

    files = {
        "certificate-image": (
            os.path.basename(cert["image"]),
            open(cert["image"], "rb"),
            mime,
        )
    }

    res = client.session.post(url, data=data, files=files)

    if res.status_code == 201:
        print(f"✅ {cert['name']} added")
    else:
        print(f"❌ Failed: {cert['name']}")
        print(res.status_code, res.text)
