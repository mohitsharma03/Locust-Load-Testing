import csv
import random
import sys
from locust import HttpUser, task, between

class CreateUserBehavior(HttpUser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_data = []

    def on_start(self):
        self.create_users()

    def create_users(self):
        url = "https://myalb.cmfaoncloud.me/signup"

        for i in range(500):
            username = f"user_{i}"
            email = f"{username}@example.com"
            password = "password"
            image_path = "profile.jpeg"

            with open(image_path, "rb") as f:
                files = {'image': f}
                data = {'name': username, 'email': email, 'password': password}

                response = self.client.post(url, data=data, files=files)

                print(f"Sending POST request to: {url}")
                print(f"Request data: {data}")
                print(f"Request files: {files}")
                print(f"Response status code: {response.status_code}")
                print(f"Response content: {response.content}")

                if response.status_code != 200:
                    print(f"Failed to create user {username}")
                    sys.exit()

                self.user_data.append((username, email, password))
                print(f"User {username} created successfully!")
                with open("user_data.csv", "a", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([username, email, password])
