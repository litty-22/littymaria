def reverse_complement(dna):
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(comp[base] for base in reversed(dna))

def reverse_palindromes(dna):
    results = []
    length = len(dna)
    for l in range(4, 13):
        for i in range(length - l + 1):
            sub = dna[i:i + l]
            rev_complement = reverse_complement(sub)
            if sub == rev_complement:
                results.append((i + 1, l)) 
    return results
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        dna = "".join(line.strip() for line in file.readlines()[1:]) 
    reverse_palindromes = reverse_palindromes(dna)
    for position, length in reverse_palindromes:
        print(position, length)
