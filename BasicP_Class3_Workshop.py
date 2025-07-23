# HP Monster
Monster_HP = 200

# Weapon Damage
Weapon1_Dmg = 20
Weapon2_Dmg = 50
Weapon3_Dmg = 80



while True:
   playerDecision = input("Do you want to play? : ")
   if playerDecision == "1":
        nRound = int(input("How many rounds do you want to play? : "))
        for i in range(nRound):
         WeaponChoice = input("Which Weapon will you choose? (1/2/3) : ")

         if WeaponChoice == "1":
            MonsterHP -= Weapon1_Dmg
         elif WeaponChoice == "2":
            MonsterHP -= Weapon2_Dmg
         elif WeaponChoice == "3":
            MonsterHP -= Weapon3_Dmg
         else:
            print("อาวุธไม่ถูกไอสัส")
            
         print("Monster HP Remaining : ", MonsterHP)
         print("Round Remaining : ", nRound - i - 1)
        
         if MonsterHP < 0:
            MonsterHP = 20
         if MonsterHP == 0:
            print("You Win!")
            print("Monster Respawned")
            break
         if i == nRound - 1:
            print("แพ้")
    
   else:
       print("ควย ไอกราก")
       break

