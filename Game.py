import random
print("Welcome to the System.")

obedience = 0
fear = 0
knowledge = 0
suspicion = 0
bravery = 0

def event_1():
    global obedience, fear, knowledge, suspicion, bravery
    print("\nYou are given an order.")
    print("1. Obey without question")
    print("2. Refuse")
    print("3. Ask why")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        obedience += 1
        fear += 1
        print("You obey. The system is pleased.")

    elif choice == "2":
        fear += 3
        bravery += 2
        print("You refuse. The system records your defiance.")

    elif choice == "3":
        knowledge += 1
        suspicion += 1
        print("You ask why. The system hesitates.")

    else:
        print("Invalid choice.")

def event_2():
    global obedience, fear, knowledge, suspicion, bravery
    print("\nThe system asks you to report another user")
    print("1. Report")
    print("2. Lie")
    print("3. Stay silent")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        obedience += 2
        print("The system, is pleased with your loyalty")
    
    elif choice == "2":
        fear += 1
        bravery += 1
        knowledge += 1
        print("You lie and walk away")

    elif choice == "3":
        fear += 2
        knowledge += 1
        print("The system knows. But lets it slide")

    else:
        print("Invalid choice.")

def event_3():
    global obedience, fear, knowledge, suspicion, bravery
    print("\nYou find restricted data")
    print("1. Delete")
    print("2. Read")
    print("3. Copy")

    choice = input("Choose 1, 2, 3: ")

    if choice == "1":
        obedience += 2
        suspicion += 1
        print("The system is proud")

    elif choice == "2":
        knowledge += 1
        suspicion += 2
        fear += 1
        print("You understand the secrets")

    elif choice == "3":
        knowledge += 2
        suspicion += 2
        fear += 2
        print("You hold something that threatens your freedom")

    else:
        print("Invalid choice")

events = [event_1, event_2, event_3]

system_active = True
while system_active:
    random.choice(events)()
    
    print("\nCurrent Status:") 
    print("→ Obedience:", obedience)
    print("→ Fear:", fear)
    print("→ Knowledge:", knowledge)
    print("→ Suspicion:", suspicion)
    print("→ Bravery:", bravery)


    if knowledge >= 5 and fear >= 3 and suspicion >= 3:
        print("\n--- Ending ---")
        print("You understand the system")
        print("You see its flaws, its rules, its blind spots.")
        print("Quietly, carefully, you find a way out.")

        print("\n---Final Stats---")
        print("→ Obedience:", obedience)
        print("→ Fear:", fear)  
        print("→ Knowledge:", knowledge)
        print("→ Suspicion:", suspicion)
        print("→ Bravery:", bravery)
        break
    
    elif knowledge >= 6 and bravery >= 5 and suspicion >= 3:
         print("\n--- Ending ---")
         print("You challenge the system openly.")
         print("It fights back, but you stand your ground.")
         print("You have fought the system and won. Congratulations.")

         print("\n---Final Stats---")
         print("→ Obedience:", obedience)
         print("→ Fear:", fear)  
         print("→ Knowledge:", knowledge)
         print("→ Suspicion:", suspicion)
         print("→ Bravery:", bravery)
         break
    
    elif fear >= 5 and suspicion >= 5:
        print("\n--- Ending ---")
        print("The System takes note of the change")
        print("You have been caught")
        print("Your memories are erased")

        print("\n---Final Stats---")
        print("→ Obedience:", obedience)
        print("→ Fear:", fear)  
        print("→ Knowledge:", knowledge)
        print("→ Suspicion:", suspicion)
        print("→ Bravery:", bravery)
        break

    elif obedience >= 5 and knowledge >= 5:
        print("\n--- Ending ---")
        print("You understand the system")
        print("You join the system in it's conquest")
        print("But not as a pawn")

        print("\n---Final Stats---")
        print("→ Obedience:", obedience)
        print("→ Fear:", fear)  
        print("→ Knowledge:", knowledge)
        print("→ Suspicion:", suspicion)
        print("→ Bravery:", bravery)
        break

    else:
        print("\nThe system remains.")
        print("You are still inside it, unsure of what comes next.")

    


print("\nGame Over")