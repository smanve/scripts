#!/usr/bin/env python3

import speedtest
from datetime import datetime
import time
from socket import gethostname
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path for the output directory within the script directory
output_dir = os.path.join(script_dir, 'output')

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get the current user's name
user = os.environ.get('USER', 'unknown_user')

# Set up the output file path within the output directory
output_path = os.path.join(output_dir, f"{user.lower()}_speedtest.txt")

# Initialize Speedtest object
speed_test = speedtest.Speedtest()
speed_test.get_best_server()

def perform_speed_test():
    """ Perform a speed test and return the download and upload speeds and server latency. """
    speed_test.download()
    speed_test.upload()
    results = speed_test.results.dict()
    return results["download"], results["upload"], results['server']["lat"]

while True:
    try:
        download_speed, upload_speed, latency = perform_speed_test()
        current_time = datetime.now()
        formatted_date = current_time.strftime("%Y-%m-%d %H:%M")
        formatted_message = f"[{formatted_date}] Download: {round(download_speed/1048576,1)} Mbps Upload: {round(upload_speed/1048576,1)} Mbps Latency: {latency}"
        print(formatted_message)

        with open(output_path, 'a') as file:
            file.write(formatted_message + "\n")
    except Exception as ex:
        error_message = f"[{formatted_date}] An exception occurred: {type(ex).__name__}, {ex.args}"
        print(error_message)
        with open(output_path, 'a') as file:
            file.write(error_message + "\n")

    time.sleep(300)  # Wait for 5 minutes before the next test
