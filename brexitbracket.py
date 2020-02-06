print("First, the round of 16! Choose your EU exit names!")
bracket1 = input("Country 1: ")
bracket2 = input("Country 2: ")
print("Bracket 1 Complete!")
bracket3 = input("Country 3: ")
bracket4 = input("Country 4: ")
print("Bracket 2 Complete!")
bracket5 = input("Country 5: ")
bracket6 = input("Country 6: ")
print("Bracket 3 Complete!")
bracket7 = input("Country 7: ")
bracket8 = input("Country 8: ")
print("Bracket 4 Complete!")
bracket9 = input("Country 9: ")
bracket10 = input("Country 10: ")
print("Bracket 5 Complete!")
bracket11 = input("Country 11: ")
bracket12 = input("Country 12: ")
print("Bracket 6 Complete!")
bracket13 = input("Country 13: ")
bracket14 = input("Country 14: ")
print("Bracket 7 Complete!")
bracket15 = input("Country 15: ")
bracket16 = input("Country 16: ")
print("Bracket 8 Complete!")
print("Let the tournament begin!")
print(f"Please choose between {bracket1} and {bracket2}!")
round1 = input("> ")
print(f"Please choose between {bracket3} and {bracket4}!")
round2 = input("> ")
print(f"Please choose between {bracket5} and {bracket6}!")
round3 = input("> ")
print(f"Please choose between {bracket7} and {bracket8}!")
round4 = input("> ")
print(f"Please choose between {bracket9} and {bracket10}!")
round5 = input("> ")
print(f"Please choose between {bracket11} and {bracket12}!")
round6 = input("> ")
print(f"Please choose between {bracket13} and {bracket14}!")
round7 = input("> ")
print(f"Please choose between {bracket15} and {bracket16}!")
round8= input("> ")
print("On to the quarterfinals!")
print(f"Please choose between {round1} and {round2}!")
quarter1 = input("> ")
print(f"Please choose between {round3} and {round4}!")
quarter2 = input("> ")
print(f"Please choose between {round5} and {round6}!")
quarter3 = input("> ")
print(f"Please choose between {round7} and {round8}!")
quarter4 = input("> ")
print("And now the semifinals!")
print(f"Please choose between {quarter1} and {quarter2}!")
semi1 = input("> ")
final1 = ""
final2 = ""
final3 = ""
final4 = ""
if semi1 == quarter1:
    final1 = quarter1
    final3 = quarter2
else:
    final1 = quarter2
    final3 = quarter1
print(f"Please choose between {quarter3} and {quarter4}!")
semi2 = input("> ")
if semi2 == quarter3:
    final2 = quarter3
    final4 = quarter4
else:
    final2 = quarter4
    final4 = quarter3
print("Final places! Let's select 3rd place now!")
print(f"Please choose between {final3} and {final4}!")
third = input("> ")
print(f"Third place is {third}!")
print("And now for the final round!!!")
print(f"Please choose between {final1} and {final2}!")
winner = input("> ")
if winner == final1:
    print("And the ultimate winner is...")
    print(f"{final1}!!!")
    print(f"Second place goes to {final2}, good try!")
else:
    print("And the ultimate winner is...")
    print(f"{final2}!!!")
    print(f"Second place goes to {final1}, good try!")
