from my_modules.mesageuser import MessageUser

obj = MessageUser()
obj.add_user("justin", 122.22, email='hello@get.com')
obj.add_user("justin", 172.72, email='paluki.konto@gmail.com')	
obj.add_user("justin", 192.92, email='rafal.konto@wp.pl')			
print(obj.get_details())

print(obj.make_messages())