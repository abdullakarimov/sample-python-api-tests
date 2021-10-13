from helpers.sender import sender
import random
import string
import time

username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
firstnames = ['Yvonne', 'Blanche', 'Oliver', 'Estelle', 'Kirk']
lastnames = ['Pineda', 'Simmons', 'Slater', 'Monaghan', 'Davenport']
firstname = random.choice(firstnames)
lastname = random.choice(lastnames)
email = username + '@test.com'
phone = ''.join(random.choices(string.digits, k=9))

post_data = {
  "id": 0,
  "username": username,
  "firstName": firstname,
  "lastName": lastname,
  "email": email,
  "password": username,
  "phone": phone,
  "userStatus": 0
}

# create a user
createUserReq = sender.send('post', '', post_data)
assert createUserReq.status_code == 200
time.sleep(3)

# verify the user is created
readUserReq = sender.send('get', username)
print(readUserReq.json()) # for some reason this needs to be printed or else the assertion fails occasionally
assert readUserReq.json()['username'] == username
time.sleep(3)

# delete the user
deleteUserReq = sender.send('del', username)
assert deleteUserReq.status_code == 200
time.sleep(3)

# verify the user is deleted
readUserReq = sender.send('get', username)
assert readUserReq.status_code == 404

