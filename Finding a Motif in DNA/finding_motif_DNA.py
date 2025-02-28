"""
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

def find_motif(s, t):
    curr = 0
    ret = ''
    while curr < len(s) - len(t):
        found = s.find(t, curr)
        if found > -1:
            ret += str(found + 1) + ' '
            curr = found + 1
        curr += 1
    return ret

if __name__ == '__main__':
    s = 'GTATGATAGCTATGATACGGTATGATACTATGATATTATGATATATGATACTATGATAGTGTATGATAATATGATATATGATATATGATATATTGTATGATATATGATATTATGATAGTATGATATAGTTTATGATATATGATACCGCCTATGATAATATGATATAATCTAGCGATATGATAGGCTATGATATATGATATATGATATATGATATATGATAATCTGGCTATGATAATCGACACCTGTATGATAGCGTATGATAATATGATATATGATATATGATACTATGATAGCGATTTTATGATATATGATATATGATATGTATGATAGCTATGATATTATGATATGTATGATACGTATGATATATGATAGATGGACGTTATGATATCTATGATAGTGTATGATATGACTATGATACGTATGATATCATAGTCGTCGCATATGATACCATATGATATATGATAACCTGTATGATATGCCGCGGTATGATAGGGTATGATATATGATATATGATAGGCTATGATACTATGATAGGTATGATATAATCCCTAGAAGTATGATAGCAGTGGGACTTATGATAATCATTATGATAAACACTATGATATATGATATGCAGCGAAGTATGATACCGCTATGATACGTATGATACCTGTATGATATATGATAGCTTATGATAACTTGATATGATAATATGATAACTACTATGATATATGATATATGATATGTATGATATATGATAAGTATGATAGCTCCGTAATTTTATGATAATATGATATATGATATATGATAGTTATGATATATGATACGAATATGATATATGATAGATATGATACATATGATAGTATGATAAGTCAGTATGATACTATGATATCGCAGTATGATACGTATGATAGTATGATAAAGTATGATATATGATATGTATGATATAATTTATGATATTATGATA'
    t = 'TATGATATA'
    result = find_motif(s, t)
    with open('results.txt', 'w') as file:
        file.write(result)
            
    