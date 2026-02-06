from portfolio_client import PortfolioClient

client = PortfolioClient()

# ---------- LOGIN ----------
ok, _ = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)
if not ok:
    print("❌ Admin login failed")
    exit()

# ---------- GET ALL CERTIFICATES ----------
res = client.session.get(f"{client.base_url}/certificate")

if res.status_code != 200:
    print("❌ Failed to fetch certificates")
    exit()

certificates = res.json()
print(f"Found {len(certificates)} certificates")

# ---------- DELETE LOOP ----------
for cert in certificates:
    cert_id = cert["certificateID"]
    del_res = client.session.delete(
        f"{client.base_url}/certificate/{cert_id}"
    )

    if del_res.status_code == 200:
        print(f"🗑️ Deleted {cert['name']}")
    else:
        print(f"❌ Failed to delete {cert['name']}")
