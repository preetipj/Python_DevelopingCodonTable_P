# Python Project: Development of a Codon Table Generator

1. Project Overview

The Codon Table Generator is a Python project to study the relation of amino acid formation from the required nucleotides in the amino acid codon table.

The program uses the standard genetic code to translate DNA and RNA sequences into amino acids. It includes a dictionary of all 64 possible codons and their associated amino acids.

The program also recognises the start and stop codons, groups the nucleotide sequences into groups of three bases (codons), checks user input and manages incomplete codons at the end of the sequence.

The simple python code used to compare the sequences in this project highlights the power of basic python programming for biological sequence analysis.

2. Project Objective

Objectives for this project include:

- Aims: To construct a Python dictionary with each of the 64 possible codons and the corresponding amino acid.
- Allow for DNA or RNA sequences to be input by the user.
- To check nucleotide sequences to verify they contain only valid nucleotide bases.
- To break input sequence into codons of three nucleotides each.
- In order to convert each codon to the matching amino acid according to the standard genetic code.
- For the recognition of start codons and stop codons.
- Purpose To identify and remove incomplete codons present at the end of a sequence.
- Press for print mode to view full page codon table and translated amino acid sequence.

3. Biological Background

# What is a Codon?

A codon is three adjacent nucleotides in a mRNA (or DNA) molecule that codes for a specific amino acid in the synthesis of a protein.

DNA contains four distinct nucleotides:

- Adenine (A)
- Thymine (T)
- Guanine (G)
- Cytosine (C)

In RNA, T is replaced with U.

Because there are four nucleotides and each codon consists of three nucleotides then the possible codons will be:

4 × 4 × 4 = 64 set of codons

These 64 codons include:

- 61 codons that specify amino acids.
- 3 stop codons that mean translation is complete.

# Start and Stop Codons

The start codon indicates the beginning of translation.

- ATG (DNA) / AUG (RNA): Methionine- the start codon.

Stop codons signal the termination of translation.

| DNA codon | RNA codon | Function |

|---|---|---|

| TAA | UAA | Stop |

| TAG | UAG | Stop |

| TGA | UGA | Stop |

# What is a Genetic Code?

Genetic code: the rule that maps from nucleotide sequences (codons) to amino acids during translation.

This project uses the standard genetic code to set the relationship for each of the 64 possible codons and the amino acids they code for.

4. Tools and Technologies Used

| Tool / Technology | Usage |

|---|---|

| Python 3 | Programming language |
| Python Dictionary | storing the 64 codons and amino acids |
| Python Lists | Storing the actual codons as they are, with the translated amino acids |
| Looping through nucleotide sequences and codons |
| Conditional statements | Input validation and start/stop codon identification |
| String handling | Upper case conversion and processing of input and seq input data |
| GitHub | host & manage the project repository |

External libraries: None. The code relies on Python's internal features and imports no extra packages.

5. Methodology and Program Workflow

The project can be divided into these steps:

# Initial step: creation of the codon reference dictionary

Python dictionary Codon_Table is created and it includes all the 64 codons and the amino acids associated with the codons.

Use each codon as the key and the matching amino acid as the value.

Example:

``python

Codon_Table = {

"ATG": "Methionine",
 "GCT": "Alanine",
 "TTT": "Phenylalanine",

"TAA": "Stop"

}

`

The complete dictionary contains all 64 codons.

# Step 2: Showing off the Codon Table

We develop a function displayCodonTable() to show each of the codon and the corresponding amino acid.

The total number of codons stored in the dictionary is also found using the len().

# Step 3: Input Validation

The function validate_sequence() verifies that the sequence input has valid bases.

The program accepts:

- DNA: A, T, G, C
- RNA: A, U, G, C

If an invalid base is found, the function returns False.

# Step 4: Break Up the Sequence into Codons

The input DNA sequence is chopped into three bases using a for` loop and string slicing.

Use a step size of three to iterate through the sequence with the range() function.

The final codons are also stored in a list, in Python.

# Step 5: Translation of Codons

I then compare the codon with the options in the Codon_Table dictionary.

The amino acid is obtained by dictionary indexing and then stored in the amino acid list.

In the case of RNA sequences, uracil (U) is substituted with thymine (T) prior to dictionary lookup in order to be able to use the same codon table.

# Step 6: Identification of Start and Stop Codons

If it is a start or stop codon, the program compares it to the appropriate list.

- The start codon is ATG/AUG.
- Stop Codons: TAA/ UAA, TAG/ UAG, TGA/ UGA.

# Step 7: Handling Incomplete Codons

Because a codon is composed of three nucleotides, the program inspects the lengths of the codons.

An incomplete codon is any group of fewer than three nucleotides in the final reading group. As a result, incomplete codons are never translated.

# Step 8: Displaying the Final Results

The program displays:

- The complete codon table.
- The divided codon sequence.
- The corresponding amino acid sequence.
- Identified start and stop codons.
- Incomplete codons, if present.

  6. Sample Input and Output

# Example 1: Sequence of DNA

Input:

``text

ATGGCTTTTTAA

`

Output:

| Codon | Amino Acid |

|---|---|

| ATG | Methionine |

| GCT | Alanine |

| TTT | Phenylalanine |

| TAA | Stop |

Translated amino acid sequence:

`text

Methionine - Alanine - Phenylalanine - Stop

`

Start codon: ATG

Stop codon: TAA

# Example 2: RNA Sequence

Input:

`text

AUGGCUUUUUAA

`

Output:

| Codon | Amino Acid |

|---|---|

| AUG | Methionine |

GCU | Alanine |

| UUU | Phenylalanine |

| UAA | Stop |

# Example 3: Incomplete Codon

Input:

`text

ATGGCTTTTA

`

Output:

|Codon |Result |

|---|---|

| ATG | Methionine |

| GCT | Alanine |

| TTT | Phenylalanine |

| A | Incomplete codon |

The last group of nucleotides has only one base left and thus cannot be translated.

# Example 4: Invalid Input

Input:

`text

ATGXGCT

`

Output:

`text

Invalid sequence! Please enter only A, T, G, C or U.

`

7. Comparison with Existing GitHub Codon Table Repositories

The public GitHub page that has been used as reference for comparing the codon table built in this project to other implementations is:

Reference Repository:

GitHub - linsalrob/geneticcodes

This repo contains Python code for translating DNA sequences by way of genetic code tables (the Standard genetic code).

# Comparison

| Feature | This Project | Reference Repository |

|---|---|---|

| Standard genetic code | Yes | Yes |
| 64 possible codons | Yes | Yes |
| Mapping of each codon to amino acid | Python dictionary | Genetic code library |
| Traslation of DNA seqence | Yes | Yes |
| RNA codon support | Yes | Yes |
| ATG/ATC start codon | Yes | Based on genetic code information. |
| Multiple genetic codes | No | Yes |

# Comparison Findings

The codon table for this project is set according to the standard genetic code and always remaps to the 'Standard translation table' of the reference library.

Both implementations define the link between the triplet of nucleotides and the amino acid it codes for.

The source code repository has more features, namely the alternative genetic codes and support for translation tables.

This project is designed to implement the standard genetic code in simplistic Python programming, and can thus be used to provide the foundations of codon translation.

8. Python Concepts Demonstrated

The project utilizes the key concepts of Python:

1. For storing codons and amino acids.
2. Functions: Used to arrange operations like show the codon table, check the sequence and translate sequences.
3. Lists: Used to store a list of codons or amino acids.
4. For loops: utilized to traverse nucleotide sequences and dictionaries.
5. It is used to ensure the validity of the input and to find the start and stop codon.
6. String slicing: Used to convert the nucleotide sequence into groups of three.
7. For uppercase conversion and replacing RNA uracil with DNA thymine.
8. User input: Accepts a nucleotide sequence from user.

9. Limitations

- The program uses only the standard genetic code and does not use alternative genetic codes.
- Translation occurs from the first nucleotide in the input sequence, and does not look for a reading frame or find a start codon automatically.
- The program searches for start and stop codons, but does not require translation to end at the first stop codon.
- The tool does not provide biological sequence alignment or polyprotein structure prediction.

10. Conclusion

The code Table Generator is an effective example of how basic biological data can be analyzed using Python programming.

Providing an understanding of the correlation between nucleotide sequences and protein synthesis, this project used a dictionary of 64 codons and implemented sequence validation, codon splitting and amino acid translation.

This project also shows how simply Python key concepts dictionaries, lists, for loops, functions and if statements can be employed to address a biological problem.

The explanation of the extra feature of RNA translation expands the capacity of program as well as an initial information about the equivalence of DNA and RNA codons.

In general, the project resulted in both the acquiring of the skills of programming and practical knowledge of the standard genetic code.

11. How to Run the Project

# Requirements

- Python 3 installed on your computer.
- A Python editor like VS Code, IDLE or Jupyter Notebook.

# Steps

1. Clone or download this repository.
2. Open the project folder on your Python editor.
3. Run the Python file:

`bash

python codontablegenerator.py

`

4. When asked to do so.
5. See translated amino acid sequence and other results.

# Repository Structure

`text

Codon-Table-Generator/

codontablegenerator.py

README_Part1.md

README_Part2.md

``

12. Author

Project: Python Assessment 2 - Codon Table Generator

Course: Bioinformatics and Biotechnology

Programming Language: Python

Repository: Add your GitHub repository link here.
