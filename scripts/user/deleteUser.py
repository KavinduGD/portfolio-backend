import requests


class PortfolioClient:
    def __init__(self, base_url="https://backend.kavindu-gihan.online/api"):
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
    def delete_user(self):
        try:
            url = f"{self.base_url}/user"
            response = self.session.delete(url)
            response.raise_for_status()
            return [True, response.json()]
        except requests.exceptions.HTTPError:
            print("Status Code:", response.status_code)
            print("Response:", response.text)
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

print("########### delete User ###########")

[isDeleted, response] = client.delete_user()

if isDeleted:
    print("User deleted successfully")
else:
    print("Failed to delete user")
    print("Response:", response)
