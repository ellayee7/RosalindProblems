"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
"""

def translate(s):
    ind = 0
    proteins = ''
    codon_dict = {'UUU': 'F', 'UUC': 'F', 
    'CUU': 'L', 'CUC': 'L', 'UUA': 'L', 'CUA': 'L', 'UUG': 'L', 'CUG': 'L', 
    'AUG': 'M', 
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 
    'UAU': 'Y', 'UAC': 'Y', 
    'CAU': 'H', 'CAC': 'H', 
    'AAU': 'N', 'AAC': 'N', 
    'GAU': 'D', 'GAC': 'D', 
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop', 
    'CAA': 'Q', 'CAG': 'Q', 
    'AAA': 'K', 'AAG': 'K', 
    'GAA': 'E', 'GAG': 'E', 
    'UGU': 'C', 'UGC': 'C', 
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 
    'UGG': 'W',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I'}

    while ind < len(s):
        if (ind+1) % 3 == 0 and ind != 0:
            codon = s[ind - 2: ind + 1]
            if codon in codon_dict:
                if codon_dict[codon] == 'Stop':
                    return proteins
                else:
                    proteins += codon_dict[codon]
            ind += 1
        else:
            ind += 1
    return proteins

if __name__ == '__main__':
    with open('rosalind_prot.txt', 'r') as file:
        sequence = file.read().strip()
        result = translate(sequence)
    with open('results.txt', 'w') as file:
        file.write(result)