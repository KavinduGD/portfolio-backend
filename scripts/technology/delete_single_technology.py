"""
delete_single_technology.py
Delete ONE technology by ID
"""

from portfolio_client import PortfolioClient

client = PortfolioClient()

# ---------- ADMIN LOGIN ----------
ok, _ = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)

if not ok:
    print("❌ Admin login failed")
    exit()

technology_id = "PUT_TECH_ID_HERE"

url = f"{client.base_url}/technology/{technology_id}"

response = client.session.delete(url)

if response.status_code == 200:
    print("✅ Technology deleted")
else:
    print("❌ Failed")
    print(response.status_code, response.text)
