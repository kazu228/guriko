from random import *

string = "0:グー,1:チョキ,2:パー"

while True:
    my_number = int(input(string))

    machine_number = randint(0, 3)

    # my_numberが0から2までの数字か
    if my_number < 0 or 2 < my_number:
        print("数字を正しく入力してください。)
        continue

    
        
