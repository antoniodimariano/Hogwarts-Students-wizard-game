# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 21/09/2019
import random
import json
import copy
from classes.Student import Student
from classes.MagicStuff import (Wand, Broomstick, Pet)
from utils import currency_converter
from utils import students_data_generator


class GameController:
    """
    This class is responsible to control all the game.
    It creates the magic items' and the students' instances and starts the battle
    """

    def __init__(self, **kwargs):
        self.magic_items_instances = {'wand': [], 'broomstick': [], "pet": []}
        self.students_instances = {}
        self.weapons_available = kwargs.get('weapons_available', {0: 'wand', 1: 'broomstick', 2: 'pet'})
        self.number_of_rounds = kwargs.get('number_of_rounds', 2)
        self.final_results = kwargs.get('final_results', {})

    def init_magic_stuff(self, file_path):
        """
        it first load the magic stuffs from the given file_path
        Once loaded, it provides to create instances for each of them, storing them to
        the self.magic_items_instance so as to be easily accessible later
        :param file_path:
        :return:
        """
        try:
            file_object = open(file_path, 'r')
            magic_items = json.load(file_object)
            wand_list = magic_items.get('wand')
            broomstick_list = magic_items.get('broomstick')
            pet_list = magic_items.get('pet')

            for item in wand_list:
                # each item's price is converted to knuts

                price_in_knuts = currency_converter.convert_g_s_k_price_to_knuts(galleons=item.get('price').get('galleons'),
                                                                                 sickles=item.get('price').get('sickles'))
                price_to_add = price_in_knuts + item.get('price').get('knuts')
                self.magic_items_instances['wand'].append(
                    Wand(name=item.get('name'), price=price_to_add, magic_point=item.get('magic_point')))

            for item in pet_list:
                price_in_knuts = currency_converter.convert_g_s_k_price_to_knuts(galleons=item.get('price').get('galleons'),
                                                                                 sickles=item.get('price').get('sickles'))
                price_to_add = price_in_knuts + item.get('price').get('knuts')
                self.magic_items_instances['pet'].append(
                    Pet(name=item.get('name'), price=price_to_add, ability=item.get('ability')))

            for item in broomstick_list:
                price_in_knuts = currency_converter.convert_g_s_k_price_to_knuts(galleons=item.get('price').get('galleons'),
                                                                                 sickles=item.get('price').get('sickles'))
                price_to_add = price_in_knuts + item.get('price').get('knuts')
                self.magic_items_instances['broomstick'].append(
                    Broomstick(name=item.get('name'), price=price_to_add, magic_point=item.get('magic_point')))
            print("[*]All magic items have been loaded\n")
            for magic_item_type in self.magic_items_instances:
                for magic_item in self.magic_items_instances[magic_item_type]:
                    print("Magic items:", magic_item.get_item_info())
            return self.magic_items_instances


        except Exception as error:
            print("EXCEPTION initialising the magic items:", error)
            exit(-1)

    def __init_scores_board(self):
        """
        this creates a scores board for each students.

        :return:
        """
        for student in self.students_instances:
            self.final_results[student] = 0

    def _load_students_and_create_instances(self, file_path):
        """
        This method loads the students from the given file_path and creates an instance of the Student class
        for record read from the file.
        At the end, it calls the __init_scores_board to create the initial empty scores board for all the students
        :param file_path:
        :return:
        """
        try:
            # Get a file object with write permission.
            file_object = open(file_path, 'r')
            # Load JSON file data to a list of python dict object.
            students_list = json.load(file_object)
            for each_student in students_list:
                self.students_instances[each_student.get('name')] = Student(name=each_student.get('name'),
                                                                            balance_usd=each_student.get('balance'))
            print("[*] All students have been converted to instances. However, they need weapons.")
            self.print_students_info()
            self.__init_scores_board()


            return 1
        except Exception as error:
            print("EXCEPTION loading students from file:", error)
            return 0

    def choose_a_magic_weapon_and_try_to_buy_it(self, magic_item, magic_items_instances, student,
                                                items_position=[0, 1, 2], upperbound=3):

        """
        This method is responsible to [auto] buy 3 magic items for each student.
        if the selected item cannot be bought because of its price exceeds the student's balance,
        it discards it and tries to buy another item of the same type. It will manage to buy 3 items eventually
        or raise an exception if it ran out of available items to buy.



        :param magic_item:
        :param magic_items_instances:
        :param student:
        :param items_position:
        :param upperbound:
        :return:
        """

        # here a random index is chosen and pop out from the items_position list. The initial upperbound is 3 because we have to buy 3 items.
        choosen_item_position = items_position.pop(random.randrange(0, upperbound))

        if not student.buy(magic_item_name=magic_item,
                           magic_item_instance=magic_items_instances[magic_item][choosen_item_position],
                           magic_item_price=magic_items_instances[magic_item][choosen_item_position].price):

            if len(items_position) == 0:
                # There are no more item to pop from the items_position list. So something went wrong :/
                raise Exception("Something went wrong with the given magic items to buy. Check your data and come back")

            # the current item cannot be bought. So it decrease the upperbound calls itself so as to try with another item
            new_upperbound = upperbound - 1
            self.choose_a_magic_weapon_and_try_to_buy_it(magic_item, magic_items_instances, student,
                                                         items_position=items_position,
                                                         upperbound=new_upperbound)

        else:
            # here the item has been bought!
            return 1

    def auto_pick_magic_items(self, magic_items_instances, student):
        """
        This method loops all the available magic items and for each of them calls the choose_a_magic_weapon_and_try_to_buy_it
        so to buy 3 magic items for each given student

        :param magic_items_instances:
        :param student:
        :param inc:
        :return:
        """
        magic_items = ['wand', 'broomstick', 'pet']
        for magic_item in magic_items:
            self.choose_a_magic_weapon_and_try_to_buy_it(magic_item=magic_item,
                                                         magic_items_instances=magic_items_instances,
                                                         student=student,
                                                         items_position=[0, 1, 2],
                                                         upperbound=3)

    def print_students_weapons(self):
        """
        Simply prints out the weapons each student owns
        :return:
        """
        for student in self.students_instances:
            print(
                "STUDENT NAME %s owns [== PET: %s == WAND: %s == BROOMSTICK: %s ==] and has [ %i knuts left [%s] and has spent %i knuts [%s] ]"
                % (self.students_instances[student].name,
                   self.students_instances[student].pet.name,
                   self.students_instances[student].wand.name,
                   self.students_instances[student].broomstick.name,
                   self.students_instances[student].balance_knuts,
                   currency_converter.convert_back_to_g_s_k(
                       initial_knuts=self.students_instances[student].balance_knuts),

                   (self.students_instances[student].pet.price + self.students_instances[student].broomstick.price +
                    self.students_instances[student].wand.price),
                   currency_converter.convert_back_to_g_s_k(
                       initial_knuts=self.students_instances[student].pet.price + self.students_instances[
                           student].broomstick.price +
                                     self.students_instances[student].wand.price))
            )

    def print_students_info(self):
        for student in self.students_instances:
            print(
                "STUDENT %s has initial budget of %i knuts [%s]"
                %(self.students_instances[student].name,
                  self.students_instances[student].balance_knuts,
                  currency_converter.convert_back_to_g_s_k(initial_knuts=self.students_instances[student].balance_knuts)
                  )
            )
    def init_students(self,file_path='./configuration/students_list.json'):
        """
        It starts generating the given number of students' data to persit to a JSON file.
        Secondly, it loads the content of the file and for each student's data it
        creates an instance of the Student class.
        After that, it call the auto_pick_magic_item to auto buy 3 magic items for each student.


        :return:
        """
        answer = input("\n\nHow many students do you want to create ?\n\n>")
        if int(answer) >1:
            if students_data_generator.write_list_to_file(
                    list_to_write=students_data_generator.students_generator(qty=int(answer)),
                    file_path=file_path):
                print("[*]Students data have been generated and stored on a file.")
                print("Giving them life....")

                if self._load_students_and_create_instances(file_path="./configuration/students_list.json"):
                    print("Going to to auto assign them weapons\n")
                    for student in self.students_instances:
                        self.auto_pick_magic_items(magic_items_instances=self.magic_items_instances,
                                                   student=self.students_instances[student])
                    print("[*]All students have been provided with 2 magic items and 1 pet")
                    answer = input("Do you want to view the students weapons?>(Y)es),(N)o\n")
                    if answer == 'Y' or answer == 'Yes':
                        self.print_students_weapons()
                    return 1

            else:
                print("Bye")
                exit(-1)
        else:
            print("Seriously? Wanna play?")
            exit(-1)


    def game(self):
        """
        This is the main routine which manages the battle game.
        From here each student fights vs each other.
        After each battle the scores board is updated.
        At the end the final results are returned.
        :return:
        """

        answer = input("Do you want to start the Auto Battle [each student vs each other]?>(Y)es),(N)o\n")
        if answer == 'Y' or answer == 'Yes':
            students_to_process = copy.deepcopy(self.students_instances)
            for challenger_student in self.students_instances:
                # temporary remove the challenger from the list of opponents
                students_to_process.pop(challenger_student)
                # here the challenger students has to fights against all the others
                for defender_student in students_to_process:
                    temp_winner = self.start_the_battle_rounds(challenger_student, defender_student)
                    print("END of the fight between %s VS %s" % (challenger_student, defender_student))
                    self.update_final_scores_board(battle_results=temp_winner, challenger_student=challenger_student,
                                                   defender_student=defender_student)
                print("%s Total points scored so far %i"
                      % (challenger_student, self.final_results[challenger_student]))
                # put the challenger student to the list again
                students_to_process = copy.deepcopy(self.students_instances)

                print("================================================")

            print("=========== END GAME ============")
            print("FINAL RESULTS", self.final_results)
            return 1
        else:
            return 0


    def start_the_battle_rounds(self, challenger_student, defender_student):
        """
        this method manages the battle between two students.
        It random chooses 2 weapons and use them to fight a 2 rounds battle..
        For each round, it stores the temporary scores and the winner.
        The temporary winner gets 2 points. In case of even, both students get 1 point (like in the football games)


        :param challenger_student:
        :param defender_student:
        :return: the temp_winner dictionary
        """

        temp_winner = {}
        battle_results = {}
        temp_winner[challenger_student] = 0
        temp_winner[defender_student] = 0
        print("Battle %s VS %s" % (challenger_student, defender_student))
        weapons_choosen = random.sample(range(0, len(self.weapons_available)), self.number_of_rounds)
        for weapon in weapons_choosen:
            battle_results = self.launch_attach(weapon_choosen=self.weapons_available[weapon],
                                                challenger_student=self.students_instances[challenger_student],
                                                defender_student=self.students_instances[defender_student])

            print("Winner:", battle_results.get('winner'))
            if battle_results.get('winner') == challenger_student:
                temp_winner[challenger_student] += 2

            elif battle_results.get('winner') == defender_student:
                temp_winner[defender_student] += 2

            else:
                temp_winner[challenger_student] += 1
                temp_winner[defender_student] += 1
        return temp_winner


    def launch_attach(self, weapon_choosen, challenger_student, defender_student):
        """
        This method is responsible for launching the attack and assign the scores


        :param weapon_choosen:
        :param challenger_student:
        :param defender_student:
        :return:
        """
        if weapon_choosen is 'pet':
            # PET VS PT
            challenger_student_pet = challenger_student.get_weapon_info(weapon_name=weapon_choosen).get(
                'name')

            defender_student_pet = defender_student.get_weapon_info(weapon_name=weapon_choosen).get(
                'name')
            print("WEAPON CHOSEN [%s] - [%s] attacks with %s and  [%s] defends  with [%s]:" % (
                weapon_choosen,
                challenger_student.name,
                challenger_student_pet,
                defender_student.name,
                defender_student_pet))

            if challenger_student_pet in challenger_student.get_weapon_info(weapon_name=weapon_choosen).get(
                    'ability').keys():
                return {'winner': challenger_student.name}
            elif defender_student_pet in defender_student.get_weapon_info(weapon_name=weapon_choosen).get(
                    'ability').keys():
                return {'winner': defender_student.name}
            else:
                return {'winner': 'Even'}


        else:
            # Magic Item VS Magic Item
            battle_point_challenger_student = challenger_student.get_weapon_info(weapon_name=weapon_choosen).get(
                'magic_point')
            battle_point_defender_student = defender_student.get_weapon_info(weapon_name=weapon_choosen).get(
                'magic_point')

            print("WEAPON CHOSEN [%s] - [%s] attacks with [%s %i points] and [%s] defends with [%s %i points]:" %
                  (weapon_choosen,
                   challenger_student.name,
                   challenger_student.get_weapon_info(weapon_name=weapon_choosen).get(
                       'name'),
                   battle_point_challenger_student,
                   defender_student.name,
                   defender_student.get_weapon_info(weapon_name=weapon_choosen).get(
                       'name'),
                   battle_point_defender_student))
            if battle_point_challenger_student > battle_point_defender_student:
                return {'winner': challenger_student.name}
            elif battle_point_challenger_student == battle_point_defender_student:
                return {'winner': 'Even'}
            else:
                return {'winner': defender_student.name}


    def update_final_scores_board(self, battle_results, challenger_student, defender_student):
        """
        This method updates the scores board for the given students
        :param battle_results:
        :param challenger_student:
        :param defender_student:
        :return:
        """

        winner_name =  max(battle_results, key=battle_results.get)
        winner_points = 10
        draft_points = 5

        if winner_name == challenger_student:
            self.final_results[challenger_student] += winner_points
        elif winner_name == defender_student:
            self.final_results[defender_student] += winner_points
        else:
            self.final_results[challenger_student] += draft_points
            self.final_results[defender_student] += draft_points
        return self.final_results


    def get_the_winner(self):
        """
        this method calculates the winner from  the scores board.
        If more than one student has scored the same result, it will be returned as well.
        :return:
        """
        top_scored = self.final_results[max(self.final_results, key=self.final_results.get)]
        # check if there are students with the same score value
        check_same_value = {key:value for key,value in self.final_results.items() if value == top_scored}
        return {"winner(s)": [student for student in check_same_value],
                "points_scored": self.final_results[max(self.final_results, key=self.final_results.get)]
                }
