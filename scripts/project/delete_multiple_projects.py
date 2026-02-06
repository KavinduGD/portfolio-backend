from portfolio_client import PortfolioClient

client = PortfolioClient()

ok, _ = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)
if not ok:
    exit("Login failed")

# ---------- GET ALL PROJECTS ----------
res = client.session.get(f"{client.base_url}/project")
projects = res.json()

print(f"Found {len(projects)} projects")

for project in projects:
    project_id = project["projectID"]
    del_res = client.session.delete(
        f"{client.base_url}/project/{project_id}"
    )

    if del_res.status_code == 200:
        print(f"🗑️ Deleted {project['projectName']}")
