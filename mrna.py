MOD = 1000000
cod_map = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'C': ['UGU', 'UGC'],
    'D': ['GAU', 'GAC'],
    'E': ['GAA', 'GAG'],
    'F': ['UUU', 'UUC'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'H': ['CAU', 'CAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'K': ['AAA', 'AAG'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'M': ['AUG'],  
    'N': ['AAU', 'AAC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'Q': ['CAA', 'CAG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'W': ['UGG'],
    'Y': ['UAU', 'UAC'],
    'Stop': ['UAA', 'UAG', 'UGA'] 
}

def protein_to_rna(protein):
    dp = [0] * (len(protein) + 1)
    dp[0] = 1  
    for i in range(1, len(protein) + 1):
        aa = protein[i - 1]
        cod_aa = cod_map[aa] 
        num_cod = len(cod_aa)
        dp[i] = (dp[i - 1] * num_cod) % MOD
    return (dp[len(protein)] * 3) % MOD
def read_input(file_path):
    with open(file_path, 'r') as file:
        protein = file.readline().strip()
    return protein

def main():
    protein = read_input('input.txt')
    result = protein_to_rna(protein)
    print(result)

if __name__ == "__main__":
    main()
