# Description 
AI Learning Program  - Wizard Game for Students of Hogwarts

This program helps the students of Hogwarts to choose their weapons.
The students of Hogwarts will be given some human currency and it has to be exchanged to wizard currency before they can purchase magic stuffs on the street.
Students also need to buy magic stuffs with the wizard currency they have on hand, and different stuff has its owned attribute which will impact to the result of competition. 


Inside the folder `configuration` there two JSON files
* students_list.json : This one is created at the bootstrap after the user chooses the number of students to have
* magic_items.json : This one is the predefined list of magic items to import at bootstrap.


# Purpose and background
After allocating students to four teams, it’s time to lead them to buy some magic things for coming wizard competition!
Before the student can actually attend the wizard competition, there are couple of things they need to do. 
The students of Hogwarts will be given some human currency and it has to be exchanged to wizard currency before they can purchase magic stuffs on the street.
Students also need to buy magic stuffs with the wizard currency they have on hand, and different stuff has its owned attribute which will impact to the result of competition. 
Some examples for magic stuff, wand, broomstick, and pet
The wizard game is hosted by school and there are certain rules to decide the winners. The game() function need to implement those rules.

**Step 1**
First, you need to create a class for student, and it has following properties and methods
Attributes:  balance, pet, wand, broomstick
this student class has following methods:
exchange_currency, change the money student bring from home in USD to magic money. (Note:  1 USD  = 2 sickles and 15 knuts, 1 galleons = 17 sickles, 1 sickle = 29 knuts)
buy, this method is call when student need to buy magic stuffs, every magic stuff has its price, balance need to be adjusted after purchasing and student's property need to be updated.
**Step 2**
A magic_stuff class need to be created, and it has price and name property, a method called use().
3 type of sub-classes need to create by inheriting magic_stuff. They are wand, pet, and broomstick respectively. 
After those instances are created, print their content (properties).

| Name of Wand | Price                           | Magic Point |
|--------------|---------------------------------|-------------|
| Redwood Wand | 3 galleons 15 sickles 7 knuts   | 9 points    |
| Oak wand     | 13 galleons 9 sickles 23 knuts  | 13 points   |
| Holly wand   | 45  galleons 9 sickles 28 knuts | 17 points   |


| Name of Broomstick | Price                            | Magic Point |
|--------------------|----------------------------------|-------------|
| Cleansweep         | 4 galleons 11 sickles 3 knuts    | 3 points    |
| Nimbus 2000        | 11 galleons 5 sickles 9 knuts    | 8 points    |
| Firebolt           | 47  galleons 13 sickles 19 knuts | 11 points   |


| Name of Pet | Price                           | Ability       | Magic Point                                                        |
|-------------|---------------------------------|---------------|--------------------------------------------------------------------|
| Rat         | 2 galleons 15 sickles 7 knuts   | Rat beats Own | The winner gets 10 points. If even, both players get 5 points each |
| Cat         | 12 galleons 7 sickles 9 knuts   | Cat beats Rat |                                                                    |
| Owl         | 50  galleons 8 sickles 20 knuts | Owl beats Cat |                                                                    |


**Step 3**
Run the program and create several instances of student class, each student has 600 USD.
Exchange the money the student has to magic currency.
Buy 3 type of magic stuffs the student want to have and modify the balance of student.

**Step 4**
create a game() function which has 2 arguments (student instances), and decide the winner by following rules.
Randomly pick 2 of magic stuffs
Call use() method that each magic stuff has to get magic point
score = summary of magic points
the student has higher score win 

# Requirements 
* Python 3.6 or higher

# How to run 

```
python main.py 
```
