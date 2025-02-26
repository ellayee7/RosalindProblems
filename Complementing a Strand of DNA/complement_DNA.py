"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols
of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" 
is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

def complement(dna):
    reverse = dna[::-1]
    reverse_complement = ''
    for c in reverse:
        if c == 'C':
            reverse_complement += 'G'
        elif c == 'G':
            reverse_complement += 'C'
        elif c == 'A':
            reverse_complement += 'T'
        elif c == 'T':
            reverse_complement += 'A'
    return reverse_complement

if __name__ == '__main__':
    with open('rosalind_revc.txt', 'r') as file:
        sequence = file.read().strip()
    result = complement(sequence)
    with open('results.txt', 'w') as file:
        file.write(result)

