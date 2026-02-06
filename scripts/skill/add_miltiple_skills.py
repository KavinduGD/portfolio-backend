from portfolio_client import PortfolioClient
import os

client = PortfolioClient()

# --------- Admin Login ----------
ok, res = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)

if not ok:
    print("Admin login failed:", res)
    exit()

# --------- Skills to add ----------
skills = [
    {
        "skill": "Web Development",
        "description": "Building resEnd-to-end organization, ui/ux design, optimization, and maintenance of your mobile app project. technologies.",
        "image": "../assets/skillImages/web-dev.svg",
    },
    {
        "skill": "UI/UX Design",
        "description": "Designing End-to-end organization, ui/ux design, optimization, and maintenance of your mobile app project.ncing user experience.",
        "image": "../assets/skillImages/web-dev.svg",
    },
    {
        "skill": "Project Management",
        "description": "PlannEnd-to-end organization, ui/ux design, optimization, and maintenance of your mobile app project.efficiently and effectively.",
        "image": "../assets/skillImages/web-dev.svg",
    },
    {
        "skill": "Data Analysis",
        "description": "Analyzing dataEnd-to-end organization, ui/ux design, optimization, and maintenance of your mobile app project.support decision-making.",
        "image": "../assets/skillImages/web-dev.svg",
    },
    {
        "skill": "Digital Marketing",
        "description": "Promoting products or End-to-end organization, ui/ux design, optimization, and maintenance of your mobile app project.digital channels to reach a wider audience.",
        "image": "../assets/skillImages/web-dev.svg",
    },

]

url = f"{client.base_url}/skill"

# --------- Loop & upload ----------
for s in skills:
    if not os.path.exists(s["image"]):
        print(f"❌ Image not found: {s['image']}")
        continue

    data = {
        "skill": s["skill"],
        "description": s["description"]
    }

    files = {
        "skill-image": (
            os.path.basename(s["image"]),          # filename
            open(s["image"], "rb"),                 # file object
            "image/svg+xml"                         # MIME TYPE (IMPORTANT)
        )
    }

    response = client.session.post(url, data=data, files=files)

    if response.status_code == 201:
        print(f"✅ {s['skill']} added")
    else:
        print(f"❌ Failed to add {s['skill']}")
        print(response.status_code, response.text)
