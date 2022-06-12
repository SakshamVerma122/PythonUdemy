# Python doesn't have Block scope

if 3>2:
    a_variable = 10
    # It's have a same strength as it's enclosing or if it's not enclosed then
    # it have global scope (for_loop/while_loop, if_else conditions .......)

print(a_variable) # Global variable


########################################

game_level = 3

enemies =["Skeleton","Zombies","Alien"]

if game_level<5:
    new_enemy = enemies[0]
    
print(new_enemy)

# as new_enemy is not enclosed inside a function it's scope is global

########################################

game_level = 3

def create_enemies():
    enemies =["Skeleton","Zombies","Alien"]
    
    if game_level<5:
        new_enemy_inside_function = enemies[0]
        
 # print(new_enemy_inside_function) --> Erroe as new_enemy_inside_function 
 # is enclosed inside the function