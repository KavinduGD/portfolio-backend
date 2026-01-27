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

# ---------- CERTIFICATE DATA ----------
certificate = {
    "name": "AWS Certified Cloud Practitioner",
    "issuer": "Amazon Web Services",
    "issueDate": "2024-02",
    "credentialsId": "ABC123XYZ",
    "certificateLink": "https://example.com/cert",
    "tags": ["cloud", "aws", "certification"],
    "score": 90,
    "image": "../assets/certImages/aws.jpeg",
}

if not os.path.exists(certificate["image"]):
    print("❌ Certificate image not found")
    exit()

# ---------- BUILD REQUEST ----------
data = {
    "name": certificate["name"],
    "issuer": certificate["issuer"],
    "issueDate": certificate["issueDate"],
    "credentialsId": certificate["credentialsId"],
    "certificateLink": certificate["certificateLink"],
    "tags": json.dumps(certificate["tags"]),
    "score": str(certificate["score"]),
}

mime, _ = mimetypes.guess_type(certificate["image"])

files = {
    "certificate-image": (
        os.path.basename(certificate["image"]),
        open(certificate["image"], "rb"),
        mime,
    )
}

url = f"{client.base_url}/certificate"
res = client.session.post(url, data=data, files=files)

if res.status_code == 201:
    print("✅ Certificate added")
else:
    print("❌ Failed")
    print(res.status_code, res.text)
