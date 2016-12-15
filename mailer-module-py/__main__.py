from argparse import ArgumentParser
from data_class import UserManager
from utils.templates import get_template, render_context


parser = ArgumentParser(prog="hungry")
parser.add_argument("type", type=str, choices=['view', 'message'])
parser.add_argument('-id','--user_id', type=int)
parser.add_argument('-e','--email', type=str)

args = parser.parse_args()

#print(args)
#print(args.user_id)
if args.type == "view":
	print(UserManager().get_user_data(user_id=args.user_id, email=args.email))
elif args.type == "message":
	print("sent message")
	print(UserManager().message_user(user_id=args.user_id, email=args.email))


#to use in cmd - /c/pythonTest python py-module view -id 2