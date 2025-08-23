import json

class Database:
    def insert(self,email,name,password):
        try:
            with open('user.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}
        if email in users:
            return False
        users[email] = [name,password]
        with open('user.json', 'w+') as file:
            json.dump(users, file,indent=4)
            return True