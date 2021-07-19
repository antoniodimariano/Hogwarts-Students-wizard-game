# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 2019-09-16


class MagicStuff:

    def __init__(self, **kwargs):
        self.price = kwargs.get('price')
        self.name = kwargs.get('name')
        self.magic_point = kwargs.get('magic_point')

    def use(self):
        return {"name": self.name,
                "magic_point": self.magic_point,
                "price":self.price}
    def get_item_info(self):
        return {"name":self.name,"price":self.price,"magic_point":self.magic_point}


class Wand(MagicStuff):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Broomstick(MagicStuff):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Pet(MagicStuff):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ability = kwargs.get('ability')

    def get_item_info(self):
        return {"name":self.name,"price":self.price,"magic_point":self.ability}
    def use(self):
        return {"name": self.name,
                "ability": self.ability,
                "price": self.price}
