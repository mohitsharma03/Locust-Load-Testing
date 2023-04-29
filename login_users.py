import csv
import random
import sys
from locust import HttpUser, task, between

class LoginUserBehavior(HttpUser):

    def read_user_data(self):
        with open("user_data.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip the header row
            user_data = [row for row in reader]
        if not user_data:
            print("No user data found!")
        return user_data

    @task(1)
    def login(self):
        user_data = self.read_user_data()
        if not user_data:
            print("No user data found!")
            return

        username, email, password = random.choice(user_data)
        data = {'username': username, 'password': password}
        url = "/video_feed"
        print(f"Sending POST request to: {url}")
        print(f"Request data: {data}")
        response = self.client.post(url, data=data)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content}")

        if response.status_code == 200:
            print(f"User {username} logged in successfully!")
        else:
            print(f"Failed to log in user {username}")
