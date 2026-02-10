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
        "skill": "DevOps Engineering",
        "description": "Designing, automating, and maintaining cloud-native infrastructure using CI/CD pipelines, GitOps practices, infrastructure as code, and container orchestration to ensure reliable and scalable deployments.",
        "image": "../assets/skillImages/devops.png",
    },
    {
        "skill": "Cloud & Infrastructure Engineering",
        "description": "Building and managing scalable cloud infrastructure on AWS and Azure, including networking, compute, storage, and security, with a strong focus on automation and reliability.",
        "image": "../assets/skillImages/cloud.png",
    },
    {
        "skill": "Full-Stack Web Development",
        "description": "Developing end-to-end web applications using modern frontend and backend technologies, ensuring seamless integration with cloud services, APIs, and automated deployment pipelines.",
        "image": "../assets/skillImages/web.png",
    },
    {
        "skill": "CI/CD & Automation",
        "description": "Implementing robust CI/CD pipelines using tools like GitHub Actions, Jenkins, GitLab CI/CD, and AWS CodePipeline to automate testing, building, and deployment workflows.",
        "image": "../assets/skillImages/cicd.png",
    },
    {
        "skill": "AI & Machine Learning Systems",
        "description": "Building and deploying machine learning and deep learning solutions, including model training, evaluation, and production deployment with cloud-native and scalable architectures.",
        "image": "../assets/skillImages/ml.png",
    },
    {
        "skill": "System Design & Architecture",
        "description": "Designing scalable, reliable, and maintainable systems using microservices, containerized architectures, and cloud-native design principles with a strong focus on performance and security.",
        "image": "../assets/skillImages/system.png",
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
