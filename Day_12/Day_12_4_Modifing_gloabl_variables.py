# Modifing Global Scope

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1 
    
    enemies = "Zombies"
    print(f"enemies inside function: {enemies}")