'''
Created on Nov 22, 2018

@author: mohanr

get all users and groups from hub
'''

import argparse
import csv
import sys
sys.path.append('/C/Users/mohanr/PycharmProjects/hub_rest_api_python/blackduck/')

from blackduck.HubRestApi import HubInstance


parser = argparse.ArgumentParser(description="A program to get all users from Hub")
parser.add_argument("file", help="The file to write the users details")
args = parser.parse_args()

hub = HubInstance()

users=hub.get_users()

if 'items' in users:
    with open(args.file, 'w', newline='') as csvfile:
        users_writer = csv.writer(csvfile)
        for user in users['items']:
                users_writer.writerow([
                user['userName'],
                user['firstName'],
                user['lastName'],
                user['email'],
                user['type'],
                user['active']
            ])
