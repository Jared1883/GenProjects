#My Calculator Project
#Created by Jared Gudmundson

from tkinter import *

##### main:
window = Tk()
window.title("My Basic Calculator")
window.configure(background="blue")

##### create list for holding numbers:
math_list = []

#create label
Label (window, text="Calculator:", font="none 25 bold") .grid(row=0, column=0, sticky=W,columnspan=2)

#Create textbox for calculations
math_text = Text (window, width=27, height=5, wrap="char",bg="white", font="none 25 bold")
math_text.grid(row=1, column=0, sticky=W, columnspan=5)

#Create the check integer function
def check_int(num):
    x = int(num)
    temp1 = num - x
    if (temp1 > 0):
        return False
    else:
        return True


#Create the calculation function
def calculate():
    only_signs = True
    only_nums = True
    endCalculation = 0
    math_text.delete(0.0, END)
    #If the list has things other than strings it will make only_signs false
    if math_list:
        for x in math_list:
            if isinstance(x, int):
                only_signs = False
            
            elif isinstance(x, str):
                only_nums = False
        
        if only_nums:
            math_text.insert(END, " " + str(math_list[0]))
        elif only_signs:
            math_text.insert(END, "ERROR")
    
        #Only runs if there are numbers in math_list
        else:
            math_list_len = len(math_list)

            #Loop that takes all of the numbers and signs in the list and calculates them together
            try:
                in_loop_num = 0
                while len(math_list) > 1:
                    #Checks if there's a multiplication or division in math_list
                    if '*' in math_list or '/' in math_list:
                        #If there is, it checks to see if there's both
                        if '*' in math_list and '/' in math_list:
                            #If there's both then it checks which one is first
                            first_index = math_list.index('*')
                            second_index = math_list.index('/')
                            if first_index < second_index:
                                in_loop_num = math_list[first_index - 1] * math_list[first_index + 1]
                                math_list[first_index - 1] = in_loop_num
                                math_list.pop(first_index + 1)
                                math_list.pop(first_index)
                            elif second_index < first_index:
                                in_loop_num = math_list[second_index - 1] / math_list[second_index + 1]
                                math_list[second_index - 1] = in_loop_num
                                math_list.pop(second_index + 1)
                                math_list.pop(second_index)
                                    
                        else:
                            if '*' in math_list:
                                first_index = math_list.index('*')
                                in_loop_num = math_list[first_index - 1] * math_list[first_index + 1]
                                math_list[first_index - 1] = in_loop_num
                                math_list.pop(first_index + 1)
                                math_list.pop(first_index)
                            else:
                                first_index = math_list.index('/')
                                in_loop_num = math_list[first_index - 1] / math_list[first_index + 1]
                                math_list[first_index - 1] = in_loop_num
                                math_list.pop(first_index + 1)
                                math_list.pop(first_index)
                    
                    #Checks if there's an addition or subtraction in math_list
                    elif '+' in math_list or '-' in math_list:
                        #If there is, it checks to see if there's both
                        if '+' in math_list and '-' in math_list:
                            #If there's both then it checks which one is first
                            first_index = math_list.index('+')
                            second_index = math_list.index('-')
                            if first_index < second_index:
                                in_loop_num = math_list[first_index - 1] + math_list[first_index + 1]
                                math_list[first_index - 1] = in_loop_num
                                math_list.pop(first_index + 1)
                                math_list.pop(first_index)
                            elif second_index < first_index:
                                in_loop_num = math_list[second_index - 1] - math_list[second_index + 1]
                                math_list[second_index - 1] = in_loop_num
                                math_list.pop(second_index + 1)
                                math_list.pop(second_index)

                        else:
                            if '+' in math_list:
                                first_index = math_list.index('+')
                                in_loop_num = math_list[first_index - 1] + math_list[first_index + 1]
                                math_list[first_index - 1] = in_loop_num
                                math_list.pop(first_index + 1)
                                math_list.pop(first_index)
                            else:
                                first_index = math_list.index('-')
                                in_loop_num = math_list[first_index - 1] - math_list[first_index + 1]
                                math_list[first_index - 1] = in_loop_num
                                math_list.pop(first_index + 1)
                                math_list.pop(first_index)

                #End of the while loop, meaning all numbers were successfully calculated
                if check_int(math_list[0]):
                    math_list[0] = int(math_list[0])
                math_text.insert(END, " " + str(math_list[0]))
                            
            except:
                math_text.insert(END, "ERROR")
        
    
    #If there is nothing inside of math_list (the calculation list)
    else:
        math_text.insert(END, " 0")

#Create the clear function
def clear():
    math_text.delete(0.0,END)
    math_list.clear()

#Create the sign functions
def add():
    math_text.insert(END, " +")
    math_list.append("+")
def subtract():
    math_text.insert(END, " -")
    math_list.append("-")
def multiply():
    math_text.insert(END, " *")
    math_list.append("*")
def divide():
    math_text.insert(END, " ÷")
    math_list.append("/")

#Create the first row of numbers
def num1():
    if math_list and isinstance(math_list[len(math_list) -1], int):
        math_list.append(int(str(math_list.pop()) + "1"))
        math_text.insert(END, "1")
    
    elif math_list and isinstance(math_list[len(math_list) -1], float):
        math_list.append(float(str(math_list.pop()) + "1"))
        math_text.insert(END, "1")
    
    else:
        math_text.insert(END, " 1")
        math_list.append(1)
def num2():
    if math_list and isinstance(math_list[len(math_list) -1], int):
        math_list.append(int(str(math_list.pop()) + "2"))
        math_text.insert(END, "2")
    
    elif math_list and isinstance(math_list[len(math_list) -1], float):
        math_list.append(float(str(math_list.pop()) + "2"))
        math_text.insert(END, "2")
    
    else:
        math_text.insert(END, " 2")
        math_list.append(2)
def num3():
    if math_list and isinstance(math_list[len(math_list) -1], int):
        math_list.append(int(str(math_list.pop()) + "3"))
        math_text.insert(END, "3")
    
    elif math_list and isinstance(math_list[len(math_list) -1], float):
        math_list.append(float(str(math_list.pop()) + "3"))
        math_text.insert(END, "3")
    
    else:
        math_text.insert(END, " 3")
        math_list.append(3)
def num4():
    if math_list and isinstance(math_list[len(math_list) -1], int):
        math_list.append(int(str(math_list.pop()) + "4"))
        math_text.insert(END, "4")
    
    elif math_list and isinstance(math_list[len(math_list) -1], float):
        math_list.append(float(str(math_list.pop()) + "4"))
        math_text.insert(END, "4")
    
    else:
        math_text.insert(END, " 4")
        math_list.append(4)
        

#Create the first row of numbers
def num5():
    if math_list and isinstance(math_list[len(math_list) -1], int):
        math_list.append(int(str(math_list.pop()) + "5"))
        math_text.insert(END, "5")
    
    elif math_list and isinstance(math_list[len(math_list) -1], float):
        math_list.append(float(str(math_list.pop()) + "5"))
        math_text.insert(END, "5")
    
    else:
        math_text.insert(END, " 5")
        math_list.append(5)
def num6():
    if math_list and isinstance(math_list[len(math_list) -1], int):
        math_list.append(int(str(math_list.pop()) + "6"))
        math_text.insert(END, "6")
    
    elif math_list and isinstance(math_list[len(math_list) -1], float):
        math_list.append(float(str(math_list.pop()) + "6"))
        math_text.insert(END, "6")
    
    else:
        math_text.insert(END, " 6")
        math_list.append(6)
def num7():
    if math_list and isinstance(math_list[len(math_list) -1], int):
        math_list.append(int(str(math_list.pop()) + "7"))
        math_text.insert(END, "7")
    
    elif math_list and isinstance(math_list[len(math_list) -1], float):
        math_list.append(float(str(math_list.pop()) + "7"))
        math_text.insert(END, "7")
    
    else:
        math_text.insert(END, " 7")
        math_list.append(7)
def num8():
    if math_list and isinstance(math_list[len(math_list) -1], int):
        math_list.append(int(str(math_list.pop()) + "8"))
        math_text.insert(END, "8")
    
    elif math_list and isinstance(math_list[len(math_list) -1], float):
        math_list.append(float(str(math_list.pop()) + "8"))
        math_text.insert(END, "8")
    
    else:
        math_text.insert(END, " 8")
        math_list.append(8)

#Create the last row of numbers
def num9():
    if math_list and isinstance(math_list[len(math_list) -1], int):
        math_list.append(int(str(math_list.pop()) + "9"))
        math_text.insert(END, "9")
    
    elif math_list and isinstance(math_list[len(math_list) -1], float):
        math_list.append(float(str(math_list.pop()) + "9"))
        math_text.insert(END, "9")
    
    else:
        math_text.insert(END, " 9")
        math_list.append(9)
def num0():
    if math_list and isinstance(math_list[len(math_list) -1], int):
        math_list.append(int(str(math_list.pop()) + "0"))
        math_text.insert(END, "0")
    
    elif math_list and isinstance(math_list[len(math_list) -1], float):
        math_list.append(float(str(math_list.pop()) + "0"))
        math_text.insert(END, "0")
    
    else:
        math_text.insert(END, " 0")
        math_list.append(0)

#Create the equals button
Button (window, text="=", width=2,height=3,command=calculate,bg="green",fg="black",font="none 49 bold") .grid(row=3, column=4,sticky=W,padx=5,pady=5,rowspan=2)

#Create the clear button
Button (window, text="C", width=2,height=1,command=clear,bg="red",fg="black",font="none 50 bold") .grid(row=2, column=4,sticky=E,padx=2.5, pady=2.5)

#Create the sign buttons
Button (window, text="+", width=2,height=1,command=add,font="none 50 bold") .grid(row=2, column=0,sticky=W,padx=2.5, pady=2.5)
Button (window, text="-", width=2,height=1,command=subtract,font="none 50 bold") .grid(row=2, column=1,sticky=W,padx=2.5, pady=2.5)
Button (window, text="*", width=2,height=1,command=multiply,font="none 50 bold") .grid(row=2, column=2,sticky=W,padx=2.5, pady=2.5)
Button (window, text="÷", width=2,height=1,command=divide,font="none 50 bold") .grid(row=2, column=3,sticky=W,padx=2.5, pady=2.5)

#Create the first row of numbers
Button (window, text="1", width=2,height=1,command=num1,font="none 50 bold") .grid(row=3, column=0,sticky=W,padx=2.5, pady=2.5)
Button (window, text="2", width=2,height=1,command=num2,font="none 50 bold") .grid(row=3, column=1,sticky=W,padx=2.5, pady=2.5)
Button (window, text="3", width=2,height=1,command=num3,font="none 50 bold") .grid(row=3, column=2,sticky=W,padx=2.5, pady=2.5)
Button (window, text="4", width=2,height=1,command=num4,font="none 50 bold") .grid(row=3, column=3,sticky=W,padx=2.5, pady=2.5)

#Create the second row of numbers
Button (window, text="5", width=2,height=1,command=num5,font="none 50 bold") .grid(row=4, column=0,sticky=W,padx=2.5, pady=2.5)
Button (window, text="6", width=2,height=1,command=num6,font="none 50 bold") .grid(row=4, column=1,sticky=W,padx=2.5, pady=2.5)
Button (window, text="7", width=2,height=1,command=num7,font="none 50 bold") .grid(row=4, column=2,sticky=W,padx=2.5, pady=2.5)
Button (window, text="8", width=2,height=1,command=num8,font="none 50 bold") .grid(row=4, column=3,sticky=W,padx=2.5, pady=2.5)

#Create the last row of numbers
Button (window, text="9", width=4,height=1,command=num9,font="none 55 bold") .grid(row=5, column=0,sticky=W,padx=2, pady=2.5,columnspan=2)
Button (window, text="0", width=4,height=1,command=num0,font="none 55 bold") .grid(row=5, column=2,sticky=W,padx=2, pady=2.5,columnspan=2)


#Run the main loop
window.mainloop()