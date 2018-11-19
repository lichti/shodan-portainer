# Author: Gustavo Lichti
# E-mail: gustavo.lichti@gmail.com
# This script search at shodan for portainer poorly configured and vulnerable
#
# Usage: 
# export SHODAN_API_KEY=xxxxxxxxxxxxxxxxxxxxxxx
# python portainer.py 
#
# Output example:
# Country: US | ISP: Digital Ocean | http://142.x.y.158:9001/
# Country: CA | ISP: Atlantic.net | http://45.x.y.165:9000/
# Error: skipping 206.x.y.63

import shodan
import sys
import os
import requests

try:
   API_KEY=os.environ.get('SHODAN_API_KEY')
except KeyError: 
   print("Please set the environment variable SHODAN_API_KEY")
   sys.exit(1)

QUERY = 'portainer'
# Filters only work with paid accounts
# - export SHODAN_FILTER = 'country:"BR"'
FILTERS = os.getenv('SHODAN_FILTER', '')

try:
  # Setup the api
  api = shodan.Shodan(API_KEY)

  # Perform the search
  result = api.search('{} {}'.format(QUERY,FILTERS))

  # Loop through the matches and print each IP
  for service in result['matches']:

    # Verify if the the service is using https or http
    if 'ssl' in service:
      PROTO='https'
    else:
      PROTO='http'

    # Make full url to find if vulnerability exists
    full_url = '{}://{}:{}/api/users/admin/check'.format(PROTO,service['ip_str'],service['port'])
    try:
      # Make request
      r = requests.get(full_url, verify=False)
      # If the return status code is 404, the application is open for anyone to create an administrator password
      if r.status_code == 404:
        print('Country: {} \t| ISP: {} \t| {}://{}:{}/'.format(service['location']['country_code'], service['isp'],PROTO,service['ip_str'],service['port']))
    except Exception as e:
      print('Error: skipping {}'.format(service['ip_str']))

except Exception as e:
  print('Error: {}'.format(e))
