# Start Code Here
naam = input("Wat is je naam :")
stemming = input("Hoi "+naam+". Hoe gaat het met je? :")
print("Het gaat dus "+stemming+" met je.")
leeftijd = input("Hoe oud ben je? :")
if int(leeftijd) < 18:
  print("Je bent nog niet volwassen.")
else:
  print("Je bent volwassen.")
