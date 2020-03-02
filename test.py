import config
import socket
from shodan import Shodan

api = Shodan(config.api_key)

# Lookup an IP
# ipinfo = api.host('217.76.128.8')
# print(ipinfo)

# Search for websites that have been "hacked"
# for banner in api.search_cursor('http.title:"hacked by"'):
#     print(banner)

# Get the total number of industrial control systems services on the Internet
# ics_services = api.count('tag:ics')
# print('Industrial Control Systems: {}'.format(ics_services['total']))

# list hosts for port
query = 'port:8009 asn:AS8560 country:es'
result = api.count(query)
print("Results: {}".format(result['total']))
print("\n")

result = api.search(query)
print(result)

for data in result['matches']:
    print("{:15}: {}".format(data['ip_str'], data['hostnames']))
    
# for data in result['matches']:
#    ip_address = data['ip_str']
#    try:
#        hostname = socket.gethostbyaddr(ip_address)
#        print("{:15}: {}".format(ip_address, hostname[0]))
#    except:
#        print("{:15}: <unknown>".format(ip_address))



