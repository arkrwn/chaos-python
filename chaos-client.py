import argparse
from chaos_python.client import chaosAPI as chaosapi
	
def main():
	if args.count: 
		print(chaosapi(args.domain, args.key, 'count'))
	elif args.json:
		print(chaosapi(args.domain, args.key, 'json'))
	else:
		chaos = chaosapi(args.domain, args.key, 'default')
		for subdomain in chaos:
			print(f"{subdomain}")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Python client to communicate with Chaos API', add_help=True)
	
	required = parser.add_argument_group('Required arguments')
	required.add_argument('--domain', metavar='example.com', help='Domain to find subdomains for', required=True)
	required.add_argument('--key', metavar='xxxxxxxxxxx', help='Chaos key for API', required=True)
	
	chaos_opt = parser.add_argument_group('Optional arguments')
	chaos_opt.add_argument('--count', action='store_true', help='Show statistics for the specified domain')
	chaos_opt.add_argument('--json', action='store_true', help='Show statistics for the specified domain')
	
	args = parser.parse_args()
	main()