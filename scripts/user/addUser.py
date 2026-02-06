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
    def create_user(self, user_data):
        try:
            url = f"{self.base_url}/user"
            response = self.session.post(url, json=user_data)
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

print("########### Create User ###########")


user_data = {
    "fullName": "Kavindu Gihan Dharmasiri",
    "shortname": "Kavindu",
    "email": "kavidudharmasiri90@gmail.com",
    "about": (
        "Software engineer specializing in DevOps, focused on automating infrastructure, optimizing CI/CD pipelines, improving system reliability, scalability, and performance through cloud technologies, containerization, monitoring, and best engineering practices."
    ),
    "age": 25,
    "address": "49/133 N, Thiththalapitigoda, Yakkala, Gampaha, Sri Lanka",
    "languages": ["Sinhala", "English"],
    "phone": "+94 703889630",
    "jobTitle": "Software Engineer",
    "education": [
        {
                "institution": "Ananda College",
                "degree": "Ordinary Level (O/L)",
                "startYear": "2011",
                "endYear": "2016",
                "results": "9 A's",
                "location": "Colombo"
        },
        {
            "institution": "Ananda College",
            "degree": "Advanced Level (A/L)",
            "startYear": "2016",
            "endYear": "2019",
            "results": "2 C's 1 S",
            "location": "Colombo"
        },
        {
            "institution": "Sri Lanka Institute of Information Technology (SLIIT)",
            "degree": "BSc (Hons) in Software Engineering",
            "startYear": "2021",
            "endYear": "present",
            "results": "3.1 GPA",
            "location": "Malabe"
        }
    ]
}


[isCreated, response] = client.create_user(user_data)

if isCreated:
    print("User created successfully")
else:
    print("Failed to create user")
    print("Response:", response)
