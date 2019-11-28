
def kettle_Check(kettle):
    if kettle == True:
        print('The Kettle is avaibale')
    else:
        print('The Kettle is not avaibale')
        exit_program()

def waterLevel_Check(waterLevel):
    if waterLevel > 40:
        print('The Water Level is Okay')
    else:
        wc = 100 - waterLevel
        print('Not enough water. Add '+ str(wc) +' % Water in the Kettle')
        exit_program()

def teaLeaf_Check(teaLeaf):
    if teaLeaf == True:
        print('The Tea Leaves are available')
    else:
        print('The Tea Leafs are not avaibale')
        exit_program()

def sugar_Check(sugar):
    if sugar == True:
        print('The Sugar is avaibale')
    else:
        print('The Sugar is not avaibale')
        exit_program()

def milk_Check(milk):
    if milk == True:
        print('The Milk is avaiable')
    else:
        print('The Milk is not avaibale')
        exit_program()


def exit_program():
    exit()

if __name__ == '__main__':

    kettle = True
    waterLevel = 50
    teaLeaf = True
    sugar = True
    milk = True

    kettle_Check(kettle)
    waterLevel_Check(waterLevel)
    teaLeaf_Check(teaLeaf)
    sugar_Check(sugar)
    milk_Check(milk)
    # boil()
    # teaLeafInKettle()
    # cook()
    # pourTea()
    # addMilkSugar()
    # exit_program()