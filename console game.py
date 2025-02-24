#Bu o'yindagi maqsad yashirilgan sonni topish yani siz kompyuter tomonidan berilgan random sonni topishingiz kerak urinishlar soni cheksiz(100 ta)

import random

secret_number = random.randint(1, 100)
urinishlar=0

print("Men 1 dan 100 gacha son o'yladim uni toping")

while True:
    guess = int(input("Taxminingiz: "))
    urinishlar+=1
    
    if guess < secret_number:
        print("Juda kichik! Yana urinib ko‘ring")
    elif guess > secret_number:
        print("Juda katta! Yana urinib ko‘ring")
    else:
        print(f"Tabriklayman! Siz {urinishlar}ta urinishda topdingiz!")
        break
