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

certificate_id = "6978ac77553c467de729bb1d"

url = f"{client.base_url}/certificate/{certificate_id}"
res = client.session.delete(url)

if res.status_code == 200:
    print("🗑️ Certificate deleted")
else:
    print("❌ Failed")
    print(res.status_code, res.text)
