from  argparse import ArgumentParser
from data_manager import read_data

parser = ArgumentParser(prog="hungry")
parser.add_argument("type", type=str, choices=['view', 'message'])
parser.add_argument('-id','--user_id', type=int)
parser.add_argument('-e','--email', type=str)

args = parser.parse_args()

#print(args)
#print(args.user_id)
if args.type == "view":
	print(read_data(user_id=args.user_id))
	print(read_data(email=args.email))
elif args.type == "message":
	print("sent message")

#to use in cmd - /c/pythonTest python py-module view -id 2