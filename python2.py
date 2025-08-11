first_start=8
for row in range(8):
 num_hash=(row*2)-1
 for col in range(16):
    if col==first_start:
     for x in range(num_hash):
      print("#", end='')
    else:
       print(" ", end='')
 first_start=first_start-1
 print()

for x in range(3):
  print("       H")