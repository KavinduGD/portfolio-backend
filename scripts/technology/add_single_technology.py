"""
add_single_technology.py
Add ONE technology with icon image
"""

from portfolio_client import PortfolioClient
import os
import mimetypes

client = PortfolioClient()

# ---------- ADMIN LOGIN ----------
ok, res = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)

if not ok:
    print("❌ Admin login failed:", res)
    exit()

# ---------- TECHNOLOGY DATA ----------
tech = {
    "technology": "Docker12",
    "level": "2",
    "type": "DevOps",
    "image": "../assets/technologyImages/git.jpg",
}

if not os.path.exists(tech["image"]):
    print("❌ Image not found:", tech["image"])
    exit()

url = f"{client.base_url}/technology"

image_path = tech["image"]

mime_type, _ = mimetypes.guess_type(image_path)
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

response = client.session.post(url, data=data, files=files)

if response.status_code == 201:
    print("✅ Technology added")
    print(response.json())
else:
    print("❌ Failed")
    print(response.status_code, response.text)
