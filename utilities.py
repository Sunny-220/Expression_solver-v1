class Helper:
    #remove all occurance of a speacific element.
    def remove_all_occur_ele(self,arr,remove_val):
        slow=0
        for fast in range(len(arr)):
            if (arr[fast] != remove_val):
                arr[slow]=arr[fast]
                slow+=1
        return arr[:slow]
    
    #It can find last occurance index of an element.
    def find_last_occur_index(self,arr,ele_set):
        for idx in range(len(arr)-1,-1,-1):
            if (arr[idx] in ele_set):
                return idx
            
    #It find first occurance index of an element.
    def find_first_occur_index(self,arr,ele_set):
        for idx in range(len(arr)):
            if (arr[idx] in ele_set):
                return idx
    
    #It can split on the bases of multiple thing at a one time.
    def My_split(self,exp,set_opr,lst=None):
        if (lst == None):
            lst=[]
        slow=0 #valid elements.
        for fast in range(len(exp)):
            if (exp[fast] in set_opr):
                lst.append(exp[slow:fast])
                lst.append(exp[fast])
                slow=fast+1
        lst.append(exp[slow:])
        return lst
    
    #finding operands in expression.
    def find_operands(self,exp,opr_idx):
        exp_lst=[]
        start_end_idx_opr=[]
        #checking operands whether,it is valid or not.
        try:
            if ("n" not in exp[opr_idx+1]):
                opr_right_val=float(exp[opr_idx+1])
            else:
                opr_right_val=float("-"+(exp[opr_idx+1][1:]))

            try:
                if ("n" not in exp[opr_idx-1]):
                    opr_left_val=float(exp[opr_idx-1])
                else:
                    opr_left_val=float("-"+(exp[opr_idx-1][1:]))
            except ValueError:
                opr_left_val=None #represent non-numeric-value.
            
        except (ValueError,IndexError):
            opr_right_val=None #represent non-numeric value.
            opr_left_val=None #represent non-numeric-value.
        
        #if operands are present,return it    
        if (opr_right_val != None) and (opr_left_val != None):
            if (opr_idx-2 >= 0):
                if (exp[opr_idx-2] == "/"):
                    opr_left_val2=exp[opr_idx-3]
                    if ("n" in opr_left_val2):
                        opr_left_val2="-"+(opr_left_val2[1:])
                    exp_lst.append([float(opr_left_val2),opr_left_val])
                    start_end_idx_opr.append(opr_idx-3)
                else:
                    exp_lst.append([opr_left_val])
                    start_end_idx_opr.append(opr_idx-1)
            else:
                exp_lst.append([opr_left_val])
                start_end_idx_opr.append(opr_idx-1)

            if (opr_idx+2 < len(exp)):
                if (exp[opr_idx+2] == "/"):
                    opr_right_val2=exp[opr_idx+3]
                    if ("n" in opr_right_val2):
                        opr_right_val2="-"+(opr_right_val2[1:])
                    exp_lst.append([opr_right_val,float(opr_right_val2)])
                    start_end_idx_opr.append(opr_idx+3)
                
                else:
                    exp_lst.append([opr_right_val])
                    start_end_idx_opr.append(opr_idx+1)
                return (exp_lst,start_end_idx_opr)
            else:
                exp_lst.append([opr_right_val])
                start_end_idx_opr.append(opr_idx+1)
            return (exp_lst,start_end_idx_opr)   
        else:
            return None
        
    #uniary minus handling.
    def unary_minus_handling(self,arr,token_lst=None,lookup_set={")","]","}"}):
        token_lst=[]
        for idx in range(len(arr)):
            if (arr[idx] == "-"):
                try:
                    after_neg_val=float(arr[idx+1]) #represent numeric value.
                    try:
                        if (idx != 0):
                            if (arr[idx-1] not in lookup_set):
                                before_neg_val=float(arr[idx-1]) #represent numeric value.
                            else:
                                before_neg_val=True
                        else:
                            before_neg_val=None #represent non-numeric-value.
                    except ValueError:
                        before_neg_val=None #represent non-numeric-value.       
                except ValueError:
                    after_neg_val=None #represent non-numeric-value.
                    before_neg_val=None #represent non numberic value.
                
                if (after_neg_val != None) and (before_neg_val == None):
                    arr[idx]="n" #n-->represent uniary minus.
        curr_itr=0
        while curr_itr < len(arr):
            if (arr[curr_itr] == "n"):
                try:
                    val=float(arr[curr_itr+1])
                except ValueError:
                    val=None
                if (val):
                    token_lst.append(("n"+str(val)))
                    curr_itr+=1
                else:
                    token_lst.append(arr[curr_itr])
            else:
                token_lst.append(arr[curr_itr])
            curr_itr+=1

        return token_lst
    def fix_multiplication(self,exp):
        exp_lst=[]
        Numeric=None
        for idx,ele in enumerate(exp):
            if (ele == "(" or ele == "[" or ele == "{") and (idx > 0):
                try:
                    if ("n" in exp[idx-1]):
                        Numeric=True
                    else:
                        int(exp[idx-1])
                        Numeric=True
                except ValueError:
                    Numeric=None
                if (Numeric):
                    exp_lst.extend(["*",ele])
                else:
                    exp_lst.append(ele)
            elif (ele == ")" or ele == "]" or ele == "}") and (idx < len(exp)-1):
                try:
                    if ("n" in exp[idx+1]):
                        Numeric=True
                    else:
                        int(exp[idx+1])
                        Numeric=True
                except ValueError:
                    Numeric=None
                if (Numeric):
                    exp_lst.extend([ele,"*"])
                else:
                    exp_lst.append(ele)
            else:
                exp_lst.append(ele)
        return exp_lst
        
    