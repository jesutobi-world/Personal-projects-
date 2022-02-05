import random
user_passcode = str(input("Enter your five pin passcode: "))
def new_hacking():
    trial=0
    guess=''
    while guess!=user_passcode:
        guess=''
        trial+=1
        print("Hacking")
        for num in range(5):
            guess+=str(random.randint(0,9))
    else:
        print(f'Passcode hacked in {trial} trials. The passcode is {guess}')

new_hacking()