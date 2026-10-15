x = 1 # Step 1
y = 9 # Step 2

def externo(): # Step 4
    x = 2 # Step 5
    def interno(): # Step 7 
        x = 3 # Step 8
        print("x interno:", x) # Step 9
        print("global y:", y) # Step 10

    interno() # Step 6
    print("x externo:", x) # Step 11

externo() # Step 3
print("global x:", x) # Step 12