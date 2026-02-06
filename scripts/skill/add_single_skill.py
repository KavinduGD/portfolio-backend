"""
add_skill.py

Adds a single skill with an image to the portfolio backend.
Requires admin login.
"""

from portfolio_client import PortfolioClient
import os

# ---------- CONFIG ----------
IMAGE_MIME = "image/svg+xml"  # change if you upload png/jpg

# ---------- CLIENT ----------
client = PortfolioClient()

# ---------- ADMIN LOGIN ----------
ok, res = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)

if not ok:
    print("❌ Admin login failed:", res)
    exit()

# ---------- SKILL DATA ----------
skill_data = {
    "skill": "Web Development",
    "description": "End-to-end web application development, UI/UX, performance optimization, and maintenance.",
    "image": "../assets/skillImages/web-dev.svg",
}

# ---------- VALIDATE IMAGE ----------
if not os.path.exists(skill_data["image"]):
    print(f"❌ Image not found: {skill_data['image']}")
    exit()

# ---------- REQUEST ----------
url = f"{client.base_url}/skill"

data = {
    "skill": skill_data["skill"],
    "description": skill_data["description"]
}

files = {
    "skill-image": (
        os.path.basename(skill_data["image"]),   # filename
        open(skill_data["image"], "rb"),          # file object
        IMAGE_MIME                                # MIME type
    )
}

response = client.session.post(url, data=data, files=files)

# ---------- RESPONSE ----------
if response.status_code == 201:
    print("✅ Skill added successfully")
    print(response.json())
else:
    print("❌ Failed to add skill")
    print(response.status_code, response.text)
