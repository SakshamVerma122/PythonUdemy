

enemies = 1 #Global scope

def increase_enimies():
    enemies = 2 #Local scope
    print(f"enimies inside function: {enemies}")

increase_enimies()
print(f"Enemies outside the function: {enemies}")

def drink_potion():
    potion_strength = 2
    print(f"potion_strength inside function :{potion_strength}")

# potion_strength -->NameError

def scope_outer_function():
    def scope_inner_function():
        print("hi")
# scope_inner_function()  -->Error