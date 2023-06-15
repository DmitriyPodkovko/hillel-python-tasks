filds = ['name', 'email']

class Card:

    def __init__(self, **kwargs):

        for key in kwargs.keys():
            if key in filds:
                self[key] = kwargs[key]

    def __setitem__(self, key, value):

    def __init__(self, name, phone=None, email=None, link=None, comment=None):



        # self._name = Validator.name(name)

        if name and isinstance(name, str):
            self._name = name
        else:
            raise Exception

        self._name = name

        self._phone = phone

        self._email = email

        # self._email =Validator.email(email)

        self._link = link

        self._comment = comment

        print('Created!')

    def update(self, upd_dict):
        if not isinstance(upd_dict, dict):
            raise Exception

        if 'name' in upd_dict.keys():
            self._name = upd_dict['name']


    # self._name = Validator.name(name)
    def __str__(self):
        # resp = f'Name:{self._name}, phone:{self._phone}, email:{self._email}, '\
        #        f'link:{self._link}, comment:{self._comment}'

        resp = f'Name:{self._name}, phone:{self._phone}, email:{self._email}, '\
               f'link:{self._link}, comment:{self._comment}'

        return resp

    # name = ''
    # phone = []
    # email = ''
    # link = ''
    # comment = ''

 c = Card(name='Some name', phone='+380671234567', email='123@123.123')
print(c)
