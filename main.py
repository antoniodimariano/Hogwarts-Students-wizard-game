# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 2019-09-16

from classes.GameController import GameController
import time
t0 = time.time()
game_ctrl = GameController()
game_ctrl.init_magic_stuff(file_path="./configuration/magic_items.json")
game_ctrl.init_students()
print("Let the BATTLE begin")
game_ctrl.game()
t1=time.time()
print("time took :",t1-t0)
print("[**]FINAL RESULTS. WINNER(S) IS (ARE) :", game_ctrl.get_the_winner())
