from utilities import Helper
from calculation import Calculation

#taking input from user.
while True:
    exp_val=input("enter your expression:-").replace("off","X")
    #calling utilities file, so that we could convert it into valid tokens.
    Helper_obj=Helper()
    #splitting into tokens.
    exp_lst=Helper_obj.My_split(exp_val,{"X","[","]","+","-","(",")","*","%","^","/","{","}"})
    #removing extra spaces,that created during splitting the exp_val.
    exp_lst=Helper_obj.remove_all_occur_ele(exp_lst,"")
    #uniary minus(-) handling.
    exp_lst=Helper_obj.unary_minus_handling(exp_lst)
    #calling our calculation file,that will calculate our expression.
    cal_obj=Calculation()
    #Handling error.
    try:
        val=cal_obj.solve_parentheses(exp_lst)
    except ZeroDivisionError:
        print("division by zero is not possible.")
        print("try,another valid expression.")
        continue
    #showing result to the user.
    final_val=val[0]
    if ("n" in final_val):
        final_val=("-"+final_val[1:])
    print(final_val)
    #asking user, whether he is wanted to continue solving expression or not.
    check=input("Do you want exit(type:- yes or no):")
    if (check == "yes"):
        break
    elif (check == "no"):
        continue
    else:
        print("you write something wrong")
        break

        


     

