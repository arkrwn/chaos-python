import requests
import argparse
import os

parser = argparse.ArgumentParser(description='Python client to communicate with Chaos API', add_help=True)
required = parser.add_argument_group('Required arguments')
required.add_argument('--domain', metavar='example.com', help='Domain to find subdomains for', required=True)
required.add_argument('--key', metavar='xxxxxxxxxxx', help='Chaos key for API', required=True)
chaos_opt = parser.add_argument_group('Optional arguments')
_ = chaos_opt.add_argument('--count', action='store_true', help='Show statistics for the specified domain')
args = parser.parse_args()

def chaos_api():
	url = f"https://dns.projectdiscovery.io/dns/{args.domain}/subdomains"
	headers = {'Authorization': args.key}
	response = requests.request("GET", url, headers=headers).json()
	return response
	
def main():
	chaos = chaos_api()
	domain = chaos['domain']
	subdomains = chaos['subdomains']

	if args.count:
		print(len(subdomains))
	else:
		for subdomain in subdomains:
			print(f"{subdomain}.{domain}")

if __name__ == "__main__":
	main()