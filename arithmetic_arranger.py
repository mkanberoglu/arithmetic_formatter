
def arithmetic_arranger(list, bool=False):
    
    if len(list) > 5:
        return "Error: Too many problems."

    #Defining a list to store problems
    problem = [] * (len(list))

    #Splitting problems by whitespaces and inserting them into problem and checking length of digits
    for i in range(len(list)):
        temp = str(list[i])
        problem.insert(i, temp.split(" "))


    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    for i in range(len(problem)):

        if len(problem[i][0]) > 4 or len(problem[i][2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif len(problem) > 5:
            return "Error: Too many problems."
        elif problem[i][1] != "+" and problem[i][1] != "-":
            return "Error: Operator must be '+' or '-'."
        try:
            int(problem[i][0])
            int(problem[i][2])
        except:
            return "Error: Numbers must only contain digits."

        #Measuring the lenth of solution
        if len(problem[i][0]) >= len(problem[i][2]):
            lenn = len(problem[i][0]) + 2
        else:
            lenn = len(problem[i][2]) + 2

        #If we must return answer
        if bool:
            if problem[i][1] == "+":
                sol = str(int(problem[i][0]) + int(problem[i][2]))
                if i == len(problem)-1:
                    fourth_line += " " * (lenn - len(sol)) + sol
                else: 
                    fourth_line += " " * (lenn - len(sol)) + sol + "    "

            elif problem[i][1] == "-":
                sol = str(int(problem[i][0]) - int(problem[i][2]))
                if i == len(problem)-1:
                    fourth_line += " " * (lenn - len(sol)) + sol
                else:
                    fourth_line += " " * (lenn - len(sol)) + sol + "    "

        #Inserting parts to lines. If part is the last element we dont put whitespaces in end       
        if i == len(problem)-1:
            first_line += " " * (lenn - len(problem[i][0])) + problem[i][0]
            second_line += problem[i][1] + " " * (lenn - len(problem[i][2]) - 1) + problem[i][2]
            third_line += "-" * lenn
        else:
            first_line += " " * (lenn - len(problem[i][0])) + problem[i][0] + "    "    
            second_line += problem[i][1] + " " * (lenn - len(problem[i][2]) - 1) + problem[i][2] + "    "
            third_line += "-" * lenn + "    "
    

    if bool :
        return (first_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line)
    else:
        return (first_line + "\n" + second_line + "\n" + third_line)

