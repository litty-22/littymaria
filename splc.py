cod_tab = {
    'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUU': 'I',
    'AUC': 'I', 'AUA': 'I', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T',
    'ACG': 'T', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D',
    'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G',
    'GGA': 'G', 'GGG': 'G', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q',
    'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S',
    'UCG': 'S', 'GGG': 'G', 'UAU': 'Y', 'UAC': 'Y', 'UGU': 'C',
    'UGC': 'C', 'UGG': 'W', 'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}

def transcribe(dna):
    return dna.replace('T', 'U')
def translate(rna):
    protein = []
    for i in range(0, len(rna), 3):
        cod = rna[i:i+3]
        if cod in cod_tab:
            amino_acid = cod_tab[cod]
            if amino_acid == 'Stop': 
                break
            protein.append(amino_acid)
    return ''.join(protein)
def rem_introns(dna, introns):
    for int in introns:
        dna = dna.replace(int, '') 
    return dna
def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    
    dna = ""  
    introns = []  
    for line in lines:
        line = line.strip()  
        if line.startswith(">"): 
            continue
        else:
            if not dna:
                dna = line  
            else:
                introns.append(line) 
    exons = rem_introns(dna, introns)
    rna = transcribe(exons)
    protein = translate(rna)
    print(protein)

if __name__ == "__main__":
    main()
