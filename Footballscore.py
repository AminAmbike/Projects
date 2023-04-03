
def main():
    
    print("This program takes in the scores of two opposing football teams and outputs the optimal way in which the trailing team must score \nin order to tie the game in the minimial number of drives using modulo arithmetic (modulo divison).")
    lower_team = Team()
    lower_team.get_difference()
    lower_team.get_remainder_8()
    lower_team.get_TD_8()
    lower_team.get_remainder_7()
    lower_team.get_TD_7()
    

    if lower_team.difference == 18:
        print("\nyou need a touchdown with a two point conv., a touchdown with a PAT, and a Field Goal")
    elif (lower_team.remainder_8 == 0):
        print("\nyou need: ", lower_team.TD_8, " Touchdowns with two point conv.") 
    elif (lower_team.remainder_7 == 0):
        print("\nyou need: ", lower_team.TD_7, " Touchdowns with PAT")
    elif (0<lower_team.difference<=3):
        print ("\nyou need a field goal")
    elif (lower_team.remainder_8==3):
            print("\nyou need: ",lower_team.TD_8, " Touchdown(s) with two point conv. and one Field Goal.")     
    elif (lower_team.remainder_7==3):
            print("\nyou need: ",lower_team.TD_7," Touchdown(s) with PAT and a Field Goal.")
    else:
        if (lower_team.remainder_7<=8) and (lower_team.remainder_8<=7):
            if lower_team.remainder_7<=3 and lower_team.remainder_8<=3:
                print("\nyou need: ", lower_team.TD_7, " Touchdowns with PAT and a Field Goal")
            if (3<lower_team.remainder_7 and lower_team.remainder_8<=lower_team.remainder_7):
                print("\nyou need: ",lower_team.TD_7+1," Touchdown(s) with PAT")
            elif (3<lower_team.remainder_8 and lower_team.remainder_7<=lower_team.remainder_8):
                print("\nyou need: ",lower_team.TD_8, " Touchdown(s) with two point conv. and one Touchdown with PAT")
        

class Team():
    def __init__(self):
        self.difference = 0
        self.TD_8 = 0
        self.remainder_8 = 0 
        self.TD_7 = 0
        self.remainder_7 = 0
        self.num_drives = 0  
    
    def get_difference(self):
        usint = False
        while usint == False:
            try:
                a = int(input("\nEnter the first score: "))
                b = int(input("\nEnter the second score: "))
                if a>=0 and b>=0:
                    usint = True
                else:
                    usint = False
                    print("\nScores must be positive, try again")
            except:
                print("\nSorry, all scores must be positive integers, try again")
                usint = False

                
        if (a<b):
            self.difference = b-a
        else:
            self.difference = a-b

    def get_TD_8(self):
        self.TD_8 = (self.difference - self.remainder_8)/8
        
    def get_TD_7(self):
        self.TD_7 = (self.difference - self.remainder_7)/7

    def get_fg(self):
        return ((self.difference - (self.difference % 3))/3)

    def get_remainder_3(self):
        return (self.difference % 3)

    def get_remainder_7(self):
        self.remainder_7 = (self.difference % 7)

    def get_remainder_8(self):
        self.remainder_8 = (self.difference % 8)

main()





        

    