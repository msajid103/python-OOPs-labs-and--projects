class User:
    def __init__(self, name, user_name, password):
        self.name = name
        self.user_name = user_name
        self.password = password
        self.friend = None

    def add_friend(self, obj):
        self.friend = obj

    def show_profile(self):
        print(self.name, '\n', self.user_name)

    def edit_profile(self, name, user_name):
        self.name = name
        self.user_name = user_name

class Facebook:
    def __init__(self):
        self.user = None
        self.users = None

    def add_user(self, user):
        user.add_friend(self.users)
        self.users = user

    def login(self, name, password):
        first = self.users
        while first is not None:
            if first.name == name and first.password == password:
                self.user = first
                print('Successfully login')
            first = first.friend

    def send_request(self,name):
        first = self.users
        while first is not None:
            if first.name == name :
                self.user.add_friend(first)
                print('Sended')
                print(self.user.friend.name)
                break
            first = first.friend


    def show_profil(self):
        self.user.show_profile()

    def print_users(self):
        first = self.users
        while first is not None:
            print(first.name)
            first = first.friend


my_Facebook = Facebook()
my_Facebook.add_user(User('sajid', 'sa', 123))
my_Facebook.add_user(User('ali', 's', 123))
my_Facebook.add_user(User('sd', 's', 123))
my_Facebook.add_user(User('sd', 'sa', 123))
my_Facebook.login('ali',123)
my_Facebook.send_request('sajid')
print('*********************')
my_Facebook.login('sd',123)
my_Facebook.send_request('ali')


