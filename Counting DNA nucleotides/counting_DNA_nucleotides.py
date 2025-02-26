"""
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that 
the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

def countDNAnuc(seq):
    A = 0
    C = 0
    G = 0
    T = 0
    for c in seq:
        if c == 'A':
            A += 1
        if c == 'C':
            C += 1
        if c == 'G':
            G += 1
        if c == 'T':
            T += 1
    return f'{A} {C} {G} {T}'

if __name__ == '__main__':
    with open('rosalind_dna.txt', 'r') as file:
        sequence = file.read().strip()
    print(countDNAnuc(sequence))
