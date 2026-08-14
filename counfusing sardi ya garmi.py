wheather = (0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0)
sunny_count = 0
rainy_count = 0
for i in range (0,17):
    if wheather[i] == 0:
        sunny_count += 1
    else:
        rainy_count += 1
print("Number of sunny days:", sunny_count)
print("Number of rainy days:", rainy_count)
if sunny_count > rainy_count:
    print("The weather is mostly sunny.")
elif sunny_count < rainy_count:
    print("The weather is mostly rainy.")
else:
    print("The weather is equally sunny and rainy.")