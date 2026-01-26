import requests


class PortfolioClient:
    def __init__(self, base_url="http://localhost:3000/api"):
        self.base_url = base_url
        self.session = requests.Session()  # keeps cookies (admin_token)

    # ---------- Admin Login ----------
    def login(self, email, password):

        url = f"{self.base_url}/admin/login"
        payload = {
            "email": email,
            "password": password
        }

        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            return [True, response.json()]
        except requests.exceptions.HTTPError:
            return [False, {response.status_code: response.text}]

    # ---------- User ----------

    def getUser(self):
        try:
            url = f"{self.base_url}/user"
            response = self.session.get(url)
            response.raise_for_status()
            return [True, response.json()]
        except requests.exceptions.HTTPError:
            return [False, {response.status_code: response.text}]


client = PortfolioClient()

[isLoggedIn, response] = client.login(
    email="kavidudharmasiri90@gmail.com",
    password="WinstonK123"
)

if not isLoggedIn:
    print("Failed to login as admin")
    print("Response:", response)
    exit()

print("########### Get User ###########")

[isFetched, response] = client.getUser()
if isFetched:
    print("Users fetched successfully")
    print("Response:", response)
else:
    print("Failed to fetch users")
    print("Response:", response)
