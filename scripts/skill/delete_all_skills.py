"""
delete_all_skills.py
Delete ALL skills
"""

from portfolio_client import PortfolioClient

client = PortfolioClient()

ok, _ = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)

if not ok:
    print("❌ Admin login failed")
    exit()

# ---------- GET ALL SKILLS ----------
get_url = f"{client.base_url}/skill"
res = client.session.get(get_url)

if res.status_code != 200:
    print("❌ Failed to fetch skills")
    exit()

skills = res.json()
print(f"Found {len(skills)} skills")

# ---------- DELETE LOOP ----------
for skill in skills:
    skill_id = skill["skillID"]
    del_url = f"{client.base_url}/skill/{skill_id}"

    delete_res = client.session.delete(del_url)

    if delete_res.status_code == 200:
        print(f"🗑️ Deleted {skill['skill']}")
    else:
        print(f"❌ Failed to delete {skill['skill']}")
