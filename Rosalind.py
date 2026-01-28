gen_code = {
    "UUU": "F", "UUC": "F",  # Phenylalanine
    "UUA": "L", "UUG": "L",  # Leucine
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",  # Serine
    "UAU": "Y", "UAC": "Y",  # Tyrosine
    "UAA": "*", "UAG": "*", "UGA": "*",  # Stop codons
    "UGU": "C", "UGC": "C",  # Cysteine
    "UGG": "W",  # Tryptophan
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",  # Leucine
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",  # Proline
    "CAU": "H", "CAC": "H",  # Histidine
    "CAA": "Q", "CAG": "Q",  # Glutamine
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",  # Arginine
    "AUU": "I", "AUC": "I", "AUA": "I",  # Isoleucine
    "AUG": "M",  # Methionine (Start)
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",  # Threonine
    "AAU": "N", "AAC": "N",  # Asparagine
    "AAA": "K", "AAG": "K",  # Lysine
    "AGU": "S", "AGC": "S",  # Serine
    "AGA": "R", "AGG": "R",  # Arginine
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",  # Valine
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",  # Alanine
    "GAU": "D", "GAC": "D",  # Aspartic acid
    "GAA": "E", "GAG": "E",  # Glutamic acid
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"  # Glycine
}

def orfs(rna_seq):
        orf_list = []  # List to store ORFs
        length = len(rna_seq)

        for j in range(length):
            if rna_seq[j:j + 3] == "AUG":  # Found start codon
                current_orf = []  # Start a new ORF
                for k in range(j, length, 3):
                    codon = rna_seq[k:k + 3]
                    if len(codon) < 3:  # Skip incomplete codons
                        break
                    aa = gen_code.get(codon, "x")
                    if aa == "*":  # Stop codon found
                        orf_list.append("".join(current_orf))
                        break  # Stop translation
                    current_orf.append(aa)

        return orf_list

dna = input("Enter your DNA sequence: ").strip()
rna = dna.replace("T", "U")
orf_result = orfs(rna)

for item in orf_result:
    print(item)
