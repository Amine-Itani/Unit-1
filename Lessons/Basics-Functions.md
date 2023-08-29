# Functions
# Squaring machine
"""
def square (in_number:int)->int:
    return in_number**2

# Don't forget to call the function

test = square(8494)
print(test)
"""

# Parrot
"""
def repeater(reps:int,word:str)->str:
    output = reps * word
    return output

parrot = repeater(word="hi",reps=4)
print(parrot)
"""
"""
# Pythagorem Theorem

def pythagoras (A:int,B:int)->int:
    output = ((A**2) + (B**2) )**(1/2)
    return output

hypothenuse = pythagoras(3,4)
print(hypothenuse)

"""

def DNAtranslator(in_protein:str)->str:

    if in_protein in "ATGC":
        if in_protein == "A":
            out_protein = "T"
        if in_protein == "G":
            out_protein = "C"
        if in_protein == "T":
            out_protein = "A"
        if in_protein == "C":
            out_protein = "G"
    else:
        out_protein = "[ERROR] Input protein is not one of ATGC"

    return out_protein
"""
# Calling the function
case1 = DNAtranslator(in_protein="Z")
print(case1)
"""
# Translate "ATTTGGGCACGTGAC"
def translateSequence(sequence:str)->str:

    output_sequence = ""
    for p in sequence:
        print(f"Translating protein {p}")
        t = DNAtranslator(in_protein=p)
        if t in 'ATGC':
            output_sequence += t
        else:
            print(f"[ERROR] Protein {p} skipped")

    return output_sequence

case2 = translateSequence("ATTTGKJEIHAFFGTCGGCACHGTGAC")
print(case2)
