import sys
question = input("math: ")

array = []

bidmas_Char = ["^", "/", "*", "+", "-"]
allowed_char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

char_allowed_at_start = allowed_char[0:len(allowed_char) - 1]
char_allowed_at_start.append("-")

def Check_Start_and_End_of_question(question):
    if question[0] not in char_allowed_at_start:
        sys.exit("Question can't start with this {}".format(question[0]));
    
    if question[len(question) - 1] not in allowed_char[0:len(allowed_char) - 1]:
        sys.exit("Question can't end with symbol")

Check_Start_and_End_of_question(question)


def formater(question_):
    formatArrayQ = []
    count = 0
    number = ""
    for x in question_:
        if count != len(question_)-1:
            if x not in bidmas_Char:
                if x in allowed_char:
                    number += x
            else:
                if number != "":
                    formatArrayQ.append(number)
                number = ""

                if count == 0 and x == bidmas_Char[len(bidmas_Char) - 1]:
                    number += x # adds - to number to make it negative
                else:
                    formatArrayQ.append(x)
        else:
            if x in allowed_char:
                number += x
                formatArrayQ.append(number)
            number = ""
        
        count += 1
    return formatArrayQ
array = formater(question)
#print(array)

bidCharPos = []

for i in range(len(array)):
    if array[i] in bidmas_Char:
        charPos = [
            array[i],
            i
        ]
        bidCharPos.append(charPos)


#print(bidCharPos)

b = bidCharPos


bidCharPos_action_track = []
#print(">>> Not Reversed bidCharPos: ", bidCharPos)

bidCharPos.reverse()
bidmas_Char = ["^", "/", "*", "+", "-"]
banned_char_combo = bidmas_Char[0:len(bidmas_Char) - 1]

def merge(i):
    global bidCharPos, bidCharPos_action_track
    while True:
        try:
            #print(">>> Reversed bidCharPos: ", bidCharPos, " bidCharPos Length: ", len(bidCharPos), " Index: ", i)
            x = bidCharPos[i][0]
            xx = bidCharPos[i][1]
            y = bidCharPos[i + 1][0]
            yy = bidCharPos[i + 1][1]
            if (xx - yy) == 1:
                if x == y and x == '-':
                    bidCharPos[i + 1] = ['+', bidCharPos[i + 1][1]]
                    #print(">>> Reversed bidCharPos: ", bidCharPos, " Change: ", bidCharPos[i + 1] , " Remove: ", bidCharPos[i])
                    bidCharPos_action_track.append(['del', bidCharPos[i][1]])
                    bidCharPos.pop(i)
                elif (x == '-' or x == '+') and (y == '-' or y == '+') and (x != y):
                    bidCharPos[i + 1] = ['-', bidCharPos[i + 1][1]]
                    #print(">>> Reversed bidCharPos: ", bidCharPos, " Change: ", bidCharPos[i + 1] , " Remove: ", bidCharPos[i])
                    bidCharPos_action_track.append(['del', bidCharPos[i][1]])
                    bidCharPos.pop(i)
                elif (x == y and x in banned_char_combo) or (x in banned_char_combo or y in banned_char_combo and x != y):
                    #print(">>> Error:  maths symbol error")
                    sys.exit()
                    break
            else:
                #print(">>> Increment Index By One.")
                i += 1
        except:
            break
        


merge(0)
#print(">>> Original bidCharPos: ", b, "\n>>> Fixed bidCharPos: ", bidCharPos, "\n>>> History bidCharPos: ", bidCharPos_action_track)


#print(">>> Question Array: ", array)
count = 0
for i in range(len(bidCharPos)):
    array[bidCharPos[i][1]] = bidCharPos[i][0]
    #print(array, bidCharPos[i][0], bidCharPos[i][1])

for i in range(len(bidCharPos_action_track)):
    array.pop(bidCharPos_action_track[i][1])

#10 ---10 + - 5 * 2 + 10^2 = 10 - 10 - 5 * 2 + 10 ^ 2
#print(">>> Question Array (Update): ", array)

"""
symbols are put in an array like this ['^', 4] symbol and how manytimes in question

"""

def symbol_location_note(symbols):
    ooo = []
    for i in range(len(bidmas_Char)):
        count = 0
        
        for j in range(len(symbols)):
            if bidmas_Char[i] == symbols[j]:
                ooo.append([bidmas_Char[i], count, j]) # ['^', 2, 10] symbol,
                count += 1 
    #print(ooo)
    return ooo


order_in_which_math_should_start = symbol_location_note(array)

#print(order_in_which_math_should_start)
#print(array)
def power(a, b):
    return float(a) ** float(b)

def division(a, b):
    return float(a) / float(b)

def multiplication(a, b):
    return float(a) * float(b)

def add(a, b):
    return float(a) + float(b)

def substruct(a, b):
    return float(a) - float(b)

def is_number(candidate_number):
    is_num = False
    z_count = 0
    allowed_char_ = allowed_char + ['-']
    #print(candidate_number)
    for z in str(candidate_number):
        if z in allowed_char_:
            z_count += 1
        
    if z_count == len(str(candidate_number)):
        is_num = True
    
    return is_num

def find_number_after_empty_space(index, dir):
    loop1 = True
    xi = 0
    x = ""
    FoundIndex = -69
    print(index)
    while loop1:
        if dir == '+':
            x = array[index + 1]
        elif dir == '-':
            x = array[index - 1]
        else:
            print("184")
            sys.exit()
        if is_number(x) and x != '':
            if dir == '+':
                FoundIndex = index + 1
            else:
                FoundIndex = index - 1
            loop1 = False
    return x, FoundIndex


count = 0
def do_math(count):
    global array, order_in_which_math_should_start
    i = order_in_which_math_should_start[count]
    print("\n\n================do_math================")
    print("Current I =", i)
    print("Symbol =",i[0])
    if len(order_in_which_math_should_start) != 0:
        print("\n\n=================Start=================\nArray: ", array, "\nOIWMSS: ", order_in_which_math_should_start)
        
        xx = find_number_after_empty_space(int(i[2]), "-")
        print("XX =", xx)
        x = xx[0]
        print("\n\n===================X===================\nArray: ", array, "\nOIWMSS: ", order_in_which_math_should_start)

        yy = find_number_after_empty_space(int(i[2]), "+")
        print("YY =", yy)
        y = yy[0]
        print("\n\n===================Y===================\nArray: ", array, "\nOIWMSS: ", order_in_which_math_should_start)

        if (i[0] == '^'):
            array[xx[1]] = power(x, y)
        elif (i[0] == '/'):
            array[xx[1]] = division(x, y)
        elif (i[0] == '*'):
            array[xx[1]] = multiplication(x, y)
        elif (i[0] == '+'):
            array[xx[1]] = add(x, y)
        elif (i[0] == '-'):
            array[xx[1]] = substruct(x, y)
        else:
            array[xx[1]] = add(x, y) # so if 10 -10 then the code will not detect the symbol but if i do this it will still minus 

        array[i[2]] = ""
        array[yy[1]] = ""

        print("\nCurrent math Done = ", x, i[0], y)
        s = ''
        for l in array:
            s += str(l)
        array = formater(s)

        order_in_which_math_should_start = symbol_location_note(array)
        print("\n\n==================End==================\nArray: ", array, "\nOIWMSS: ", order_in_which_math_should_start)
        if len(order_in_which_math_should_start) != 0 :
            count = 0
            do_math(count)

do_math(count)
print(array)