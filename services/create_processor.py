class UserRecord():

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.email = kwargs['email']
        self.password = kwargs['password']
        self.age = kwargs['age']
