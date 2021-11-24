Nama_TD = input("Siapakah nama Tactical Dollmu? ")
Firepower = int(input("Besar kekuatan firepower = "))
RateOfFire = int(input("Besar kekuatan rate of fire = "))
Accuracy = int(input("Besar accuracy = "))
Evasion = int(input("Besar kemampuan evasion = "))

DamagePerSecond = (Firepower+RateOfFire)/60
CombatEffectiveness = (30 * Firepower + 40 * ((RateOfFire**2)/120)) + 15 * (Accuracy + Evasion)

print()
print("Nama Tactical Dollmu adalah " + Nama_TD)
print("Besar kekuatan fire power " + Nama_TD + " adalah " + str(Firepower))
print("Besar kekuatan rate of fire " + Nama_TD + " adalah " + str(RateOfFire))
print("Besar accuracy " + Nama_TD + " adalah " + str(Accuracy))
print("Besar kemampuan evasion " + Nama_TD + " adalah " + str(Evasion))

print()
print("Damage per second " + Nama_TD + " adalah " + str(round(DamagePerSecond,2)))
print("Combat effectiveness " + Nama_TD + " adalah " + str(round(CombatEffectiveness)))