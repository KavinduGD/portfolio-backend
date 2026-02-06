import requests


class PortfolioClient:
    """
    Base API client.
    - Keeps session cookies (admin_token)
    - Handles admin login
    """

    def __init__(self, base_url="http://localhost:3000/api"):
        self.base_url = base_url
        self.session = requests.Session()

    def login(self, email, password):
        """
        Logs in as admin.
        Backend sets admin_token cookie.
        """
        url = f"{self.base_url}/admin/login"
        payload = {
            "email": email,
            "password": password
        }

        try:
            res = self.session.post(url, json=payload)
            res.raise_for_status()
            return True, res.json()
        except requests.exceptions.HTTPError:
            return False, {res.status_code: res.text}
