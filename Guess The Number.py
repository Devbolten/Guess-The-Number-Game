import random
print ("INSTRUCTIONS:\nThere is a random number chosen from 1-100, and you have to try and guess it.\nYou will have 10 tries to guess the number.\nIf you do not guess it within the 10 tries, You lose.\n")

number = random.randint(1,100)
print (number)

i=10

number_guessed = int(input("Please enter your first number:"))
if number_guessed == number :
    print("Number",number,"is correct! YOU GUESSED IT FIRST TRY, WELL DONE!")
    

while number_guessed != number and number_guessed > number:
    if i == 1 and number_guessed != number:
        print("Number was",number,".\nYou have ran out of tries :( GAME OVER!")
        break
    if i == 1 and number_guessed > number:
        print("Number was",number,".\nYou have ran out of tries :( GAME OVER!")
        break
    i = i - 1
    print("TOO HIGH! Enter a lower number.")
    print ("(",i,"ATTEMPTS LEFT )")
    number_guessed = int(input("INCORRECT! Please enter your number again:"))
    if number_guessed == number :
        print ("Number",number,"is correct! WELL DONE!")
        break
    while i == 2:
        i = i - 1
        if number_guessed > number:
                print("TOO HIGH! Enter a lower number.")
        elif number_guessed < number:
                print("TOO LOW! Enter a higher number.")
        print ("( 1 ATTEMPT LEFT )")
        number_guessed = int(input("INCORRECT! Please enter your last number:")) 
        
        if i == 1 and number_guessed == number:
            print("Number",number,"is correct! WELL DONE!")
            break
        


    else:
         while number_guessed != number and number_guessed < number:
                if i == 1 and number_guessed > number:
                   print("Number was",number,".\nYou have ran out of tries :( GAME OVER!")
                   break
                if i == 1 and number_guessed != number:
                   print("Number was",number,".\nYou have ran out of tries :( GAME OVER!")
                   break
                i = i - 1
                print("TOO LOW! Enter a higher number.")
                print ("(",i,"ATTEMPTS LEFT )")
                number_guessed = int(input("INCORRECT! Please enter your number again:"))
                if number_guessed == number :
                   print ("Number",number,"is correct! WELL DONE!")
                   break
                while i == 2:
                    i = i - 1
                    if number_guessed > number:
                        print("TOO HIGH! Enter a lower number.")
                    elif number_guessed < number:
                        print("TOO LOW! Enter a higher number.")
                    print ("( 1 ATTEMPT LEFT )")
                    last_number_guessed = int(input("INCORRECT! Please enter your last number:"))
 
                    if i == 1 and number_guessed == number:
                        print("Number",number,"is correct! WELL DONE!")
                        break
                 



    
while number_guessed != number and number_guessed < number:
    if i == 1 and number_guessed > number:
        print("Number was",number,".\nYou have ran out of tries :( GAME OVER!")
        break
    if i == 1 and number_guessed != number:
        print("Number was",number,".\nYou have ran out of tries :( GAME OVER!")
        break
    i = i - 1
    print("TOO LOW! Enter a higher number.")
    print ("(",i,"ATTEMPTS LEFT )")
    number_guessed = int(input("INCORRECT! Please enter your number again:"))
    if number_guessed == number :
        print("Number",number,"is correct! WELL DONE!")
        break
    while i == 2:
        i = i - 1
        if number_guessed > number:
                print("TOO HIGH! Enter a lower number.")
        elif number_guessed < number:
                print("TOO LOW! Enter a higher number.")
        print ("( 1 ATTEMPT LEFT )")
        number_guessed = int(input("INCORRECT! Please enter your last number:"))

        if i == 1 and number_guessed == number :
            print("Number",number,"is correct! WELL DONE!")
        
  
    else:
        while number_guessed != number and number_guessed > number:
                if i == 1 and number_guessed > number:
                    print("Number was",number,".\nYou have ran out of tries :( GAME OVER!")
                    break
                if i == 1 and number_guessed != number:
                    print("Number was",number,".\nYou have ran out of tries :( GAME OVER!")
                    break
                i = i - 1
                print("TOO HIGH! Enter a higher number.")
                print ("(",i,"ATTEMPTS LEFT )")
                number_guessed = int(input("INCORRECT! Please enter your number again:"))
                if number_guessed == number :
                    print ("Number",number,"is correct! WELL DONE!")
                    break
                while i == 2:
                    i = i - 1
                    if number_guessed > number:
                         print("TOO HIGH! Enter a lower number.")
                    elif number_guessed < number:
                         print("TOO LOW! Enter a higher number.")
                    print ("( 1 ATTEMPT LEFT )")
                    number_guessed = int(input("INCORRECT! Please enter your last number:"))
                   
                    if i == 1 and number_guessed == number:
                         print("Number",number,"is correct! WELL DONE!")
                         break
               

                   
    

        
        

            
    

   
    
    

    



    
 
