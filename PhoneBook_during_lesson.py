
filds = ['name', 'email']

class Card:
    
    storage = {}
    
    def __init__(self, **kwargs):
        
        for key in kwargs.keys():
            if key in filds:
                self[key] = kwargs[key]
            
    def __setitem__(self, key, value):
        self.storage[key] = value
    
    def __getitem__(self, key):
        return self.storage[key]
    #
    # def __init__(self, name, phone=None, email=None, link=None, comment=None):
    #
    #     # self._name = Validator.name(name)
    #
    #     if name and isinstance(name, str):
    #         self._name = name
    #     else:
    #         raise Exception
    #
    #     self._phone = phone
    #
    #     self._email = email
    #
    #     # self._email = Validator.email(email)
    #
    #     self._link = link
    #
    #     self._comment = comment
    #
    #     print('Created!')

    def update(self, upd_dict):
        
        if not isinstance(upd_dict, dict):
            raise Exception
        
        if 'name' in upd_dict.keys():
            # self._name = Validator.name(upd_dict['name'])
            self._name = upd_dict['name']
    
    def __str__(self):

        # resp = f'Name:{self.name}, phone:{self.phone}, email:{self.email}, ' \
        #        f'link:{self._link}, comment:{self._comment}.'

        resp = f'Name:{self["name"]}, email:{self["email"]}.'

        return resp
    
    # _name = ''
    # _phone = []
    # _email = ''
    # _link = ''
    # _comment = ''
    
    
c = Card(name='Some name', phone='+380671234567', email='123@123.123')

print(c)

class Book:
    
    cards = []
    
    def add(self, **kwargs):
        
        card = Card(**kwargs)
        self.cards.append(card)
        
    def remove_card(self, question):
        
        rm_c = self.search(question)
        
        if rm_c:
            for c in rm_c:
                self.cards.remove(c)
    
    def edit_card(self, question, edit_dict):
    
        list_c = self.search(question)
        
        if len(list_c) != 1:
            print('Try again')
            return
        
        list_c[0].update(edit_dict)
        
        
    def amount(self):
        return len(self.cards)
    
    def search(self, question):
        
        res = []
        for card in self.cards:
            for val in card.storage.values():
                if val.find(question) != -1:
                    res.append(card)

        return res
