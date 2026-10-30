##Python Project: Development of a Codon Table Generator
## Codon Table Generator
## 1. Create a dictionary containing all 64 codons and their corresponding amino acids.

Codon_Table = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",

    "TCT": "Serine", "TCC": "Serine",
    "TCA": "Serine", "TCG": "Serine",

    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",

    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",

    "CTT": "Leucine", "CTC": "Leucine",
    "CTA": "Leucine", "CTG": "Leucine",

    "CCT": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",

    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",

    "CGT": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",

    "ATT": "Isoleucine", "ATC": "Isoleucine",
    "ATA": "Isoleucine", "ATG": "Methionine",

    "ACT": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",

    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",

    "AGT": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GTT": "Valine", "GTC": "Valine",
    "GTA": "Valine", "GTG": "Valine",

    "GCT": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",

    "GAT": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",

    "GGT": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}
## display the codon table

def display_Codon_Table():
    for codon in Codon_Table:
        print(codon, ":", Codon_Table[codon])
# # print(Codon_Table)
# print(Codon_Table["ATG"])
print(display_Codon_Table())
## length of codon table
print(len(Codon_Table))

## 2. Accept a DNA sequence from the user.
## 3. Validate the input to ensure that it contains only valid DNA nucleotides (A, T, G, and C).

def validate_sequence(sequence):

    valid = True

    for base in sequence:

        if base not in "ATGCU":
            valid = False

    return valid

## 4. Divide the sequence into codons in groups of three nucleotides.


## 5. Translate each codon into its corresponding amino acid using the codon table.
 

## 6. Identify start codons and stop codons
 
## 7. Handle incomplete codons at the end of the sequence.
 
## 8. Display the codon table and the translated amino acid sequence
   