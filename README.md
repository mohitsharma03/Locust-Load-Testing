
Step1: Install locust on your system:
pip3 install locust

Step2: Start your flask app wherever its deployed:

python3 app.py

Step3.1: Create locustfile.py and run as:

locust --users 1 --spawn-rate 10 --host https://myalb.cmfaoncloud.me

OR, Step3.2: Instead of creating one locust file we can create separate files: one for creating users ‘create_users.py’ and one for log-in ‘login_users.py' & then
run below commands to run the two locust files on your local machine or on some other instance, pointing it to your Flask app's endpoint:

locust -f create_users.py --users 1 --spawn-rate 10 --run-time 1m --host https://myalb.cmfaoncloud.me

locust -f login_users.py --users 10 --spawn-rate 1 --run-time 1m --host https://myalb.cmfaoncloud.me

Step4: Access the Locust web interface by navigating to http://localhost:8089 in your web browser. From here, you can start and stop the load test, monitor the progress, and view the results.

Step5: Once you're done with the load test, stop Locust and shut down your Flask app on the EC2 instance.
