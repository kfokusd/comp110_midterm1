import turtle

PropertyList = [ "San Diego", 
                 "Oceanside", 
                 "La Jolla", 
                 "La Mesa", 
                 "Chula Vista"]

###############################################
# PLEASE DO NOT change anything above this line
###############################################

############################
# TODO: Write your code here
############################


############################################################
# For renderGraph(), just add code in the TODO section below
############################################################
def renderGraph(filename):
    # Turtle for Expenses
    exp_turtle = turtle.Turtle()
    exp_turtle.pencolor("Red")
    exp_turtle.pensize(20)                      # HINT: Check out the width of the turtle

    # Turtle for Income
    inc_turtle = turtle.Turtle()
    inc_turtle.pencolor("Green")
    inc_turtle.pensize(20)                      # HINT: Check out the width of the turtle

    # Turtle for Text
    txt_turtle = turtle.Turtle()

    for i in range(len(PropertyList)):
        site = PropertyList[i] 
        totalIncome = findTotalIncome(filename, site)
        totalExpense = findTotalExpenses(filename, site)
        txt_turtle.up()
        txt_turtle.setpos(i*100, 5000//10)      # HINT: Check out the calculation for x & y coordinate
        txt_turtle.down()
        txt_turtle.write(site)

        ############################
        # TODO: Write your code here
        ############################

    wn = turtle.Screen()
    wn.exitonclick()
# End of renderGraph()


###############################################
# PLEASE DO NOT change anything below this line
################################################
def main():

    print("======   Largest Income   ======")
    for i in range(len(PropertyList)):
        site = PropertyList[i] 
        print("{:15}: ${:.2f}".format(site, findLargestIncome("E1_expenses.csv", site)))
    print("================================\n\n")

    print("====  Largest Expenses Site ====")
    print(findLargestExpensesSite("E1_expenses.csv"))
    print("================================\n\n")

    print("======     Net Profit     ======")
    print("${:.2f}".format(findNetProfit("E1_expenses.csv")))
    print("================================\n\n")

    #renderGraph("E1_expenses.csv")

if __name__ == "__main__":
    main()

# Expected Output:
#======   Largest Income   ======
#San Diego      : $2860.00
#Oceanside      : $3130.00
#La Jolla       : $3680.00
#La Mesa        : $1500.00
#Chula Vista    : $1200.00
#================================
#
#
#====  Largest Expenses Site ====
#Oceanside
#================================
#
#
#======     Net Profit     ======
#$9160.70
#================================
