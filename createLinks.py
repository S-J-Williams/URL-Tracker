import hashlib

server = input("Enter IP/Address or hostname of server: ")

user = input("Enter Username: ")
hash_object = hashlib.md5(user.encode())
hash = hash_object.hexdigest()

full_url = "https://" + server + "/" + hash
print(full_url)

with open('tokens.txt', 'a')as file:
    file.write('%s\n' % hash)
    
with open('users.txt', 'a')as file:
    file.write('%s\n' % user)