
import random
inp_val = input("Say something: ")

splitin = inp_val.split(" ")

random.shuffle(splitin)

yo = " ".join(splitin)

print(f" \n {yo}")