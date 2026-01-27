"""
delete_all_technologies.py
Delete ALL technologies
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

# ---------- GET ALL TECHNOLOGIES ----------
get_url = f"{client.base_url}/technology"
res = client.session.get(get_url)

if res.status_code != 200:
    print("❌ Failed to fetch technologies")
    exit()

technologies = res.json()

print(f"Found {len(technologies)} technologies")

# ---------- DELETE LOOP ----------
for tech in technologies:
    tech_id = tech["id"]
    del_url = f"{client.base_url}/technology/{tech_id}"

    delete_res = client.session.delete(del_url)

    if delete_res.status_code == 200:
        print(f"🗑️ Deleted {tech['technology']}")
    else:
        print(f"❌ Failed to delete {tech['technology']}")
