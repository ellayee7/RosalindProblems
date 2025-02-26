"""
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u 
is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t
 having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

def transcribe(dna_seq):
    rna_seq = dna_seq.replace('T', 'U')
    return rna_seq

if __name__ == '__main__':
    with open('rosalind_rna.txt', 'r') as file:
        sequence = file.read().strip()
    result = transcribe(sequence)
    with open('results.txt', 'w') as file:
        file.write(result)


