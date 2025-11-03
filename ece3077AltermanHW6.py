from scipy.io import loadmat
import numpy as n

## PART A 
#bring the data in the program
da = loadmat('characterFreqs.mat')
freq = da['characterFreqs'][0] #27 probs summing 1

#entropy
e = -n.sum(freq * n.log2(freq))
print (f'entropy is {e} bits/char')

##PART B 
import huffman as h
import string as s
import heapq

sym = list(s.ascii_lowercase)
sym += [' ']

code = h.codebook(zip(sym, freq))
avgLen = sum(len(code[s]) * freq[i] for i,s in enumerate (sym))

print(f'expected bits {avgLen} bits/char')
print("Huffman codebook:")
for s in sym:
    if s == ' ':
        print(f"' ' : {code[s]}")
    else:
        print(f"{s} : {code[s]}")

