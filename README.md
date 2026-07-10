# Expression_solver-v1
A Python CLI(command line interface) application that evaluates mathematical expressions safely.

## Overview
A command-line python application that evaluates mathematical expressions entered by the user.

## Features
->Handles mathematical expressions with multiple levels of nested brackets.
->correctly follow operator precedence(Bodmas).
->support deeply nested brackets.
->it support 3 brackets such as:-(),{},[]
->it also support override brackets operation,eg:-
(3+4(9-[5-{4+2}])).
->it support :-addition,subtraction,multiplication,division,off,power.
->it also support fraction operation such as :-1/2*3/4 etc.
->supports continuous input handling until the user exists.
->handle invalid expressions.
->Uses a modular Python code structure.
Note:-for divide operation you have to use "%" operator.
Note:-for fraction operation,you have to use "/" operator.

## Limitation
->Very large numerical inputs that exceed Python's processing limits are not supported.
->the tool cannot handle consecutive minus signs(eg: --5 or -(-5)),a minus
sign placed directly outside (eg:--[5-3]),or mathematical sign simplication(like converting minus-minus to plus),though it can successfuly process independent negative numbers being multiplied (eg:(-5)*-2[4])

## Technologies used
->Python

## project structure
->main.py
->calculation.py
->utilities.py

## How to use it
->just click on main.py file and enter your expression and get your answer.

## How it works internally?
->step 1(input taking and converting it according to our need).
-splitting into tokens on the bases of {"X","[","]","+","-","(",")","*","%","^","/","{","}"},and for this I have built my own split function that can split expression on the bases of multiples_things at a one time with o(n) time complexity and o(n) space complexity.

-after that,it goes to my remove_all_occur_ele function that is also created by me,which can remove multiples elements at a one time,it removes ""->it that is formed during the splitting of expression.

-after that ,it goes uniary_minus_handling function that convert negative numbers of negative sing into speacial symbol(which is n"),so that handling of negative numbers could be easy.

-after that,it goes to fixing_multiplication function that put "*" b/w brackets and numbers.eg:-2(3) here we know that 2 is in multiplication with 3,but my multiplication function don't knows,so my fixing_multiplication function put "*" b/w it,and after that expression becomes like this:-2*(3). 
step 2:-
now,the whole expression will go to parenthesis function,first it checks whether parenthesis is present or not and then it find index of bracket,and then it access the elements b/w indices,and then again check it whether a square or curly brackets present in it or not,if present call to that function with input what we had access b/w the indices and that function will evaluate the expression and returned it if not present it will call to power_operator function and power operator function calculate its part left it sends to off_operator function it will also calculate its expression and then send to another function,and this keeps happening,and when the expression reach to the last function first it calculate all its value and then return the value,and finally parenthesis have a numerical value,then it access all the elements bofore start_br_idx and then output what he found after solving the expression concatenate it and also concatenate the elements after end_br_idx,and again call to parenthesis function because there could be a lot of parenthesis in this,and again this process repeat.
Note:- same logic apply with curly and sqare braces.
step 3:-power_function logic
first it checks whether power operator present or not,if yes find its last index,after that it call to find_operands_function with expression as an input,and it retured list_operands and start_end_index_operands,access its base and exponent,if its base and exponent is in fraction it will convert into non_fraction_value,finally calculate the value and concatenate the value in the expression in place of operator expression,and again call to power operator function,it will again check and if power operator will not present then it will call off_function,and similarly all the function do and at the end when expression reach to addtion_and_subtraction function it calculate the expression and returned it.
Note:-same logic apply with off_function,division_function,multiplication_function and addition_subtraction function.




