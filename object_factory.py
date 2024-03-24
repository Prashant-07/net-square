from user import User

class UserObjectFactory:
    def __init__(self):
        self.usernames = []
        self.username_obj_map = dict()
    
    def get_user_obj(self,username):
        if username in self.username_obj_map: return self.username_obj_map[username]
        # print(username)
        self.username_obj_map[username] = User(username)
        self.usernames.append(username)
        return self.username_obj_map[username]
    
    def get_ordered_username_list(self):
        return self.usernames
