#Guessing number game using while loop
secret_number=10
guess_limit=3
guess_count=0
while guess_count<guess_limit:
    guess=int(input("Enter guess: ")) #15,20,30
    guess_count=guess_count+1 #guess_coun=0+1=1,2,3
    if guess==secret_number:
        print("You win!")
        break
else:
    print("You loose!")