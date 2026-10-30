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

dna_sequence = "ATGGCTTTTTAC"

codons = []

for i in range(0, len(dna_sequence), 3):

    codon = dna_sequence[i:i+3]

    codons.append(codon)

print("Codons:", codons)

## 5. Translate each codon into its corresponding amino acid using the codon table.
amino_acids = []

for codon in codons:

    if codon in Codon_Table:

        amino_acid = Codon_Table[codon]

        amino_acids.append(amino_acid)

print("Amino Acids:", amino_acids)

## 6. Identify start codons and stop codons
start_codons = ["ATG"]

stop_codons = ["TAA", "TAG", "TGA"]

print("\nStart Codons:")

for codon in codons:

    if codon in start_codons:

        print(codon, "- Start Codon")


print("\nStop Codons:")

for codon in codons:

    if codon in stop_codons:

        print(codon, "- Stop Codon")
## 7. Handle incomplete codons at the end of the sequence.
print("\nChecking Incomplete Codons:")

for codon in codons:

    if len(codon) < 3:

        print(codon, "- Incomplete Codon")

    else:

        print(codon, "- Complete Codon")
## 8. Display the codon table and the translated amino acid sequence
print("\nComplete Codon Table:")

display_Codon_Table()


print("\nFinal Codon Sequence:")

print(" - ".join(codons))


print("\nFinal Amino Acid Sequence:")

print(" - ".join(amino_acids))

# Accept DNA or RNA sequence from the user
def translate_sequence(sequence):

    codons = []

    amino_acids = []

    for i in range(0, len(sequence), 3):

        codon = sequence[i:i+3]

        codons.append(codon)

        if len(codon) == 3:

            if "U" in codon:
                codon = codon.replace("U", "T")

            amino_acid = Codon_Table[codon]

            amino_acids.append(amino_acid)

        else:

            print(codon, "- Incomplete Codon")


    print("\nCodons:", codons)

    print("\nAmino Acid Sequence:", amino_acids)


    print("\nStart and Stop Codons:")

    for codon in codons:

        if codon == "ATG" or codon == "AUG":

            print(codon, "- Start Codon")

        elif codon in ["TAA", "TAG", "TGA", "UAA", "UAG", "UGA"]:

            print(codon, "- Stop Codon")

sequence = input("\nEnter your DNA or RNA sequence: ")

sequence = sequence.upper()

if validate_sequence(sequence):

    translate_sequence(sequence)

else:

    print("Invalid sequence! Enter only A, T, G, C or U.")
