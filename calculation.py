from utilities import Helper

class Calculation:

    # it solve parenthesis expression.
    def solve_parentheses(self,exp):
        if ("(" in exp):
            round_br_start_idx=Helper().find_last_occur_index(exp,{"("})
            round_br_end_idx=exp.index(")",round_br_start_idx+1,len(exp))
            exp_val=exp[round_br_start_idx+1:round_br_end_idx]

            #checking whether a another brackets present in exp_val or not.
            if ("{" in  exp_val) or ("[" in exp_val):
                start_idx=Helper().find_first_occur_index(exp_val,{"[","{"})
                end_idx=Helper().find_last_occur_index(exp_val,{"}","]"})
                if (exp_val[start_idx] == "{"):
                    new_val=self.solve_curly_braces(exp_val[start_idx:end_idx+1])
                else:
                    new_val=self.solve_square_braces(exp_val[start_idx:end_idx+1])
                exp_val=exp_val[:start_idx]+new_val+exp_val[end_idx+1:]

            new_val=self.solve_power_calc(exp_val)
            return self.solve_parentheses(exp[:round_br_start_idx]+new_val+exp[round_br_end_idx+1:])

        else:
            return self.solve_curly_braces(exp)
        
    #It solve curly braces expression.    
    def solve_curly_braces(self,exp):
        if ("{" in exp):
            curly_br_start_idx=Helper().find_last_occur_index(exp,"{")
            curly_br_end_idx=exp.index("}",curly_br_start_idx+1,len(exp))
            exp_val=exp[curly_br_start_idx+1:curly_br_end_idx]
            
            #checking whether a another bracket present in exp_val or not.
            if ("[" in exp_val) or ("(" in exp_val):
                start_idx=Helper().find_first_occur_index(exp_val,{"[","("})
                end_idx=Helper().find_last_occur_index(exp_val,{"]",")"})
                if (exp_val[start_idx] == "["):
                    new_val=self.solve_square_braces(exp_val[start_idx:end_idx+1])
                else:
                    new_val=self.solve_parentheses(exp_val[start_idx:end_idx+1])
                exp_val=exp_val[:start_idx]+new_val+exp_val[end_idx+1:]

            new_val=self.solve_power_calc(exp_val)
            return self.solve_curly_braces(exp[:curly_br_start_idx]+new_val+exp[curly_br_end_idx+1:])
           
        else:
            return self.solve_square_braces(exp)
        
    #It solve square braces expression.    
    def solve_square_braces(self,exp):
        if ("[" in exp):
            square_br_start_idx=Helper().find_last_occur_index(exp,"[")
            square_br_end_idx=exp.index("]",square_br_start_idx+1,len(exp))
            exp_val=exp[square_br_start_idx+1:square_br_end_idx]
            
            #checking whether a another bracket present in exp_val or not.
            if ("{" in exp_val) or ("(" in exp_val):
                start_idx=Helper().find_first_occur_index(exp_val,{"{","("})
                end_idx=Helper().find_last_occur_index(exp_val,{"}",")"})
                if (exp_val[start_idx] == "{"):
                    new_val=self.solve_curly_braces(exp_val[start_idx:end_idx+1])
                else:
                    new_val=self.solve_parentheses(exp_val[start_idx:end_idx+1])
                exp_val=exp_val[:start_idx]+new_val+exp_val[end_idx+1:]
            
            new_val=self.solve_power_calc(exp_val)
            return self.solve_square_braces(exp[:square_br_start_idx]+new_val+exp[square_br_end_idx+1:])

        else:
            return self.solve_power_calc(exp)
        
    #It solve power operator expression.    
    def solve_power_calc(self,exp):
        if ("^" in exp):
            power_opr_idx=Helper().find_last_occur_index(exp,{"^"})

            #finding base and exponent value.
            operands_lst=Helper().find_operands(exp,power_opr_idx)
            if (len(operands_lst[0][0]) > 1):
                p_val=operands_lst[0][0][0]
                q_val=operands_lst[0][0][1]

                #zero devision error handling
                try:
                    base_val=(p_val)/(q_val)
                except ZeroDivisionError:
                    raise ZeroDivisionError
            else:
                base_val=operands_lst[0][0][0]

            #finding exponent value.
            if (len(operands_lst[0][1]) > 1):
                p_val=operands_lst[0][1][0]
                q_val=operands_lst[0][1][1]

                #zero division error handling.
                try:
                    exponent_val=(p_val)/(q_val)
                except ZeroDivisionError:
                    raise ZeroDivisionError
            else:
                exponent_val=operands_lst[0][1][0]
            
            #calculating final value.
            final_val=str((base_val)**(exponent_val))
            if ("-" in final_val):
                final_val=("n"+(final_val[1:]))
            return self.solve_power_calc(exp[:operands_lst[1][0]]+[final_val]+exp[operands_lst[1][1]+1:])
            
        else:
            return self.solve_off_calc(exp)
    
    #It solve off operator expression.
    def solve_off_calc(self,exp):
        if ("X" in exp):
            off_opr_idx=exp.index("X")

            #findining operands.
            operands_lst=Helper().find_operands(exp,off_opr_idx)
            if (len(operands_lst[0][0]) > 1):
                p_val=operands_lst[0][0][0]
                q_val=operands_lst[0][0][1]

                #zero devision error handling
                try:
                    left_operands=(p_val)/(q_val)
                except ZeroDivisionError:
                    raise ZeroDivisionError
            else:
                left_operands=operands_lst[0][0][0]

            #finding right operands.
            if (len(operands_lst[0][1]) > 1):
                p_val=operands_lst[0][1][0]
                q_val=operands_lst[0][1][1]

                #Zero division error handling
                try:
                    right_operands=(p_val)/(q_val)
                except ZeroDivisionError:
                    raise ZeroDivisionError
            else:
                right_operands=operands_lst[0][1][0]
                    
            #final calculation.
            final_val=str((left_operands)*(right_operands))        
            if ("-" in final_val):
                final_val=("n"+(final_val[1:]))
            return self.solve_off_calc(exp[:operands_lst[1][0]]+[final_val]+exp[operands_lst[1][1]+1:])
        else:
            return self.solve_division_calc(exp)
        
    #It solve division operator expression.
    def solve_division_calc(self,exp):
        if ("%" in exp):
            div_opr_idx=exp.index("%")

            #findining operands.
            operands_lst=Helper().find_operands(exp,div_opr_idx)
            if (len(operands_lst[0][0]) > 1):
                p_val=operands_lst[0][0][0]
                q_val=operands_lst[0][0][1]

                #zero division error handling
                try:
                    left_operands=(p_val)/(q_val)
                except ZeroDivisionError:
                    raise ZeroDivisionError
            else:
                left_operands=operands_lst[0][0][0]

            #finding right operands.
            if (len(operands_lst[0][1]) > 1):
                p_val=operands_lst[0][1][0]
                q_val=operands_lst[0][1][1]

                #Zero division error handling
                try:
                    right_operands=(p_val)/(q_val)
                except ZeroDivisionError:
                    raise ZeroDivisionError
            else:
                right_operands=operands_lst[0][1][0]
            
            #final calculation.
            try:
                final_val=str((left_operands)/(right_operands))
                if ("-" in final_val):
                    final_val=("n"+final_val[1:])
                return self.solve_division_calc(exp[:operands_lst[1][0]]+[final_val]+exp[operands_lst[1][1]+1:])
            except ZeroDivisionError:
                raise ZeroDivisionError
        else:
            return self.solve_multiply_calc(exp)
    
    #It solve multiplication operator expression.
    def solve_multiply_calc(self,exp):
        if ("*" in exp):
            mul_opr_idx=exp.index("*")

            #findining operands.
            operands_lst=Helper().find_operands(exp,mul_opr_idx)
            if (len(operands_lst[0][0]) > 1):
                p_val=operands_lst[0][0][0]
                q_val=operands_lst[0][0][1]

                #zero division error handling
                try:
                    left_operands=(p_val)/(q_val)
                except ZeroDivisionError:
                    raise ZeroDivisionError
            else:
                left_operands=operands_lst[0][0][0]

            #finding right operands.
            if (len(operands_lst[0][1]) > 1):
                p_val=operands_lst[0][1][0]
                q_val=operands_lst[0][1][1]

                #zero division error handling.
                try:
                    right_operands=(p_val)/(q_val)
                except ZeroDivisionError:
                    raise ZeroDivisionError
            else:
                right_operands=operands_lst[0][1][0]

            #calculating final value.
            final_val=str((left_operands)*(right_operands))
            if ("-" in final_val):
                final_val=("n"+(final_val[1:]))
            return self.solve_multiply_calc(exp[:operands_lst[1][0]]+[final_val]+exp[operands_lst[1][1]+1:])
        else:
            return self.solve_addition_calc(exp)

    #It solve addition operator expression.    
    def solve_addition_calc(self,exp):
        if ("+" in exp) or ("-" in exp):
            opr_idx=Helper().find_first_occur_index(exp,{"+","-"})

            #findining operands.
            operands_lst=Helper().find_operands(exp,opr_idx)
            if (len(operands_lst[0][0]) > 1):
                p_val=operands_lst[0][0][0]
                q_val=operands_lst[0][0][1]

                #zero division error handling
                try:
                    left_operands=(p_val)/(q_val)
                except ZeroDivisionError:
                    raise ZeroDivisionError
            else:
                left_operands=operands_lst[0][0][0]

            #finding right operands.
            if (len(operands_lst[0][1]) > 1):
                p_val=operands_lst[0][1][0]
                q_val=operands_lst[0][1][1]

                #zero division error handling.
                try:
                    right_operands=(p_val)/(q_val)
                except ZeroDivisionError:
                    raise ZeroDivisionError
            else:
                right_operands=operands_lst[0][1][0]
                
            #calculating final value.
            if (exp[opr_idx] == "+"):
                final_val=str((left_operands)+(right_operands))
                if ("-" in final_val):
                    final_val=("n"+(final_val[1:]))
                return self.solve_addition_calc(exp[:operands_lst[1][0]]+[final_val]+exp[operands_lst[1][1]+1:])
            
            else:
                final_val=str((left_operands)-(right_operands))
                if ("-" in final_val):
                    final_val=("n"+(final_val[1:]))
                return self.solve_addition_calc(exp[:operands_lst[1][0]]+[final_val]+exp[operands_lst[1][1]+1:])
        else:
            return exp
        
    

             
        