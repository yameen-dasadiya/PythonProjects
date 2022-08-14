secret_number = 777
g_num=int(input("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+ \n"""))
while g_num != secret_number :
        print("Ha ha! You're stuck in my loop!")
        g_num=int(input("Enter Number again:"))
        
print("Well done, muggle! You are free now.")
         


