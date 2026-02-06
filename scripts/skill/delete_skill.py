from portfolio_client import PortfolioClient

client = PortfolioClient()

# --------- Admin Login ----------
ok, res = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)

if not ok:
    print("Admin login failed:", res)
    exit()


skill_id = "6978510b00244c16ec1e1f7b"

base_url = f"{client.base_url}/skill"

response = client.session.delete(f"{base_url}/{skill_id}")

if response.status_code == 200:
    print("✅ Skill deleted successfully")
else:
    print("❌ Failed to delete skill")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
