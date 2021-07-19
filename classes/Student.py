# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 2019-09-16

from utils import currency_converter


class Student:

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.balance_usd = kwargs.get('balance_usd', 0)
        self.balance_knuts = 0
        self.pet = kwargs.get('pet', 0)
        self.wand = kwargs.get('wand', 0)
        self.broomstick = kwargs.get('broomstick', 0)
        self.exchange_currency()

    def get_weapon_info(self, weapon_name):
        """
        this method first gets the attribute from the given weapon_name and then
        calls the use() method of the related MagicStuff class's  method
        :param weapon_name:
        :return:
        """
        try:
            return self.__getattribute__(weapon_name).use()
        except Exception as missing_value:
            print("EXCEPTION getting the attribute name:", missing_value, weapon_name)
            exit(-1)

    def exchange_currency(self):
        """
        it changes the money a student bring from home (USD) to magic money
        1 USD  = 2 sickles and 15 knuts, 1 galleons = 17 sickles, 1 sickle = 29 knuts
        :return:
        """

        self.balance_knuts = currency_converter.convert_currency_to_knuts(amount=self.balance_usd, currency='USD')

    def purchase_validation(func):
        """
        This function verifies if there is enough balance to buy the given item
        :return:
        """

        def check_and_update_my_balance(self, magic_item_instance, magic_item_name, magic_item_price):
            if self.balance_knuts >= magic_item_price:
                self.balance_knuts -= magic_item_price
                return func(self, magic_item_instance, magic_item_name, magic_item_price)

            else:
                return 0

        return check_and_update_my_balance

    @purchase_validation
    def buy(self, magic_item_instance, magic_item_name, magic_item_price):
        """
        this method buys magic stuff.
        Every magic stuff has its price, balance need to be adjusted after purchasing and student's property need to be updated.
        :return:
        """
        try:
            self.__setattr__(magic_item_name, magic_item_instance)
            return 1
        except Exception as missing_value:
            print("EXCEPTION setting the attribute name:", missing_value, magic_item_name)
            exit(-1)
