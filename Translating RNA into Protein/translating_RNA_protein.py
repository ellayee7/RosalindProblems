"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
"""

def translate(s):
    codondict = {}
    ind = 0
    proteins = ''
    while ind < len(s):
        if (ind+1) % 3 == 0 and ind != 0:
            codon = s[ind - 2: ind + 1]
            if codon == 'UUU' or codon == 'UUC':
                proteins += 'F'
            elif codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
                proteins += 'L'
            elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' or codon == 'AGU' or codon == 'AGC':
                proteins += 'S'
            elif codon == 'UAU' or codon == 'UAC':
                proteins += 'Y'
            elif codon == 'UGU' or codon == 'UGC':
                proteins += 'C'
            elif codon == 'UGG':
                proteins += 'W'
            elif codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
                proteins += 'P'
            elif codon == 'CAU' or codon == 'CAC':
                proteins += 'H'
            elif codon == 'CAA' or codon == 'CAG':
                proteins += 'Q'
            elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
                proteins += 'R'
            elif codon =='AUU' or codon == 'AUC' or codon == 'AUA':
                proteins += 'I'
            elif codon == 'AUG':
                proteins += 'M'
            elif codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
                proteins += 'T'
            elif codon == 'AAU' or codon == 'AAC':
                proteins += 'N'
            elif codon == 'AAA' or codon == 'AAG':
                proteins += 'K'
            elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG':
                proteins += 'V'
            elif codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
                proteins += 'A'
            elif codon == 'GAU' or codon == 'GAC':
                proteins += 'D'
            elif codon == 'GAA' or codon == 'GAG':
                proteins += 'E'
            elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
                proteins += 'G'
            elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
                return proteins
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