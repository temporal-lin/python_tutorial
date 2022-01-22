#!/usr/bin/env python3

import subprocess

svc = input("Check a service: ")

check_cmd = ["ps", "-C", svc]

service_check = subprocess.call(check_cmd)

if service_check == 0:
    print("The service is running.")
else:
    print("The service is not running.")
    print("Starting {}...".format(svc))
    try:
        subprocess.check_output(["systemctl", "start", svc])
    except subprocess.CalledProcessError as err:
        print("There was an error starting the process.\n")
        print(err)
        exit(69)    # Nice..
    subprocess.call(check_cmd)
