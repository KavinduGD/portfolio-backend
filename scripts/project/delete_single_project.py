from portfolio_client import PortfolioClient

client = PortfolioClient()

ok, _ = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)
if not ok:
    exit("Login failed")

project_id = "6978a2c8456c10e4ea3ee8e5"

res = client.session.delete(f"{client.base_url}/project/{project_id}")

if res.status_code == 200:
    print("🗑️ Project deleted")
else:
    print("❌ Failed", res.text)
