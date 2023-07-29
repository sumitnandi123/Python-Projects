game_list=[1,2,3]

def display(game_list):
    print("here is the current list:")
    print(game_list)
    
def position_choice():
    choice='wrong'
    while choice not in ['1','2','3']:
        choice=input("Pick a position(1,2,3):")
        
        if choice not in['1','2','3']:
            print("Sorry invalid choice")
            
            
                
            
def replacement(game_list,choice):
    newitem=input("type a string to place at choice position:")
    game_list[choice]=newitem
    print(game_list)
    return game_list          
display(game_list)
position_choice()
replacement(game_list,1)
