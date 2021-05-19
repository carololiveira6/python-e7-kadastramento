class UserRecord():

    def __init__(self, **kwargs):
        self.call_id = kwargs['id']
        self.origin = kwargs['name']
        self.destination = kwargs['email']
        self.start = kwargs['password']
        self.end = kwargs['age']
