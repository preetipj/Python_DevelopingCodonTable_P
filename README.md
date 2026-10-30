# Python Project: Development of a Codon Table Generator

## 1. Project Overview

The **Codon Table Generator** is a Python-based project developed to understand the relationship between nucleotide sequences and amino acids during protein synthesis.

The program uses the standard genetic code to translate DNA and RNA sequences into their corresponding amino acids. It contains a dictionary of all 64 possible codons and their associated amino acids.

The program also identifies start and stop codons, divides nucleotide sequences into groups of three bases (codons), validates user input, and handles incomplete codons at the end of a sequence.

This project demonstrates the application of basic Python programming concepts in biological sequence analysis.

## 2. Project Objective

The main objectives of this project are:

- To create a Python dictionary containing all 64 possible codons and their corresponding amino acids.
- To accept DNA or RNA sequences as input from the user.
- To validate nucleotide sequences to ensure that they contain only valid nucleotide bases.
- To divide the input sequence into codons consisting of three nucleotides each.
- To translate each codon into its corresponding amino acid using the standard genetic code.
- To identify start codons and stop codons.
- To detect and handle incomplete codons at the end of a sequence.
- To display the complete codon table and the translated amino acid sequence.

## 3. Biological Background

### What is a codon?

A codon is a sequence of three consecutive nucleotides in DNA or RNA that specifies a particular amino acid or a stop signal during protein synthesis.

There are four different nucleotides in DNA:

- Adenine (A)
- Thymine (T)
- Guanine (G)
- Cytosine (C)

In RNA, thymine (T) is replaced by uracil (U).

Since there are four possible nucleotides and each codon contains three nucleotides, the total number of possible codons is:

**4 × 4 × 4 = 64 codons**

These 64 codons include:
- 61 codons that specify amino acids.
- 3 stop codons that signal the termination of translation.

### Start and Stop Codons

A start codon signals the beginning of translation.

- **ATG (DNA) / AUG (RNA):** Codes for Methionine and acts as the standard start codon.

Stop codons signal the termination of translation.

| DNA codon | RNA codon | Function |
|---|---|---|
| TAA | UAA | Stop |
| TAG | UAG | Stop |
| TGA | UGA | Stop |

### What is a genetic code?

The genetic code is the set of rules that determines how nucleotide codons correspond to amino acids during protein synthesis.

The standard genetic code is used in this project to establish the relationship between all 64 codons and their corresponding amino acids.

## 4. Tools and Technologies Used

| Tool / Technology | Application |
|---|---|
| Python 3 | Programming language |
| Python Dictionary | Storing the 64 codons and amino acids |
| Python Lists | Storing codons and translated amino acids |
| For loops | Iterating through nucleotide sequences and codons |
| Conditional statements | Input validation and identification of start/stop codons |
| String manipulation | Converting input to uppercase and processing DNA/RNA sequences |
| GitHub | Hosting and maintaining the project repository |

**External libraries:** None. The project uses Python's built-in features and does not require additional packages.

## 5. Methodology and Program Workflow

The project is divided into the following steps:

### Step 1: Creation of the Codon Dictionary

A Python dictionary named `Codon_Table` is created containing all 64 possible DNA codons and their corresponding amino acids.

Each codon is used as a key, while its corresponding amino acid is stored as the value.

Example:

```python
Codon_Table = {
    "ATG": "Methionine",
    "GCT": "Alanine",
    "TTT": "Phenylalanine",
    "TAA": "Stop"
}
```

The complete dictionary contains all 64 codons.

### Step 2: Displaying the Codon Table

A function named `display_Codon_Table()` is developed to display each codon and its corresponding amino acid.

The `len()` function is also used to determine the total number of codons stored in the dictionary.

### Step 3: Input Validation

A function named `validate_sequence()` checks whether the input sequence contains valid nucleotide bases.

The program accepts:

- DNA: A, T, G, C
- RNA: A, U, G, C

If an invalid nucleotide is detected, the function returns `False`.

### Step 4: Dividing the Sequence into Codons

The input nucleotide sequence is divided into groups of three bases using a `for` loop and string slicing.

The `range()` function is used with a step size of three to move through the sequence.

The resulting codons are stored in a Python list.

### Step 5: Translation of Codons

Each codon is compared with the keys in the `Codon_Table` dictionary.

The corresponding amino acid is retrieved using dictionary indexing and stored in an amino acid list.

For RNA sequences, uracil (U) is replaced with thymine (T) before dictionary lookup so that the same codon table can be used.

### Step 6: Identification of Start and Stop Codons

The program checks each codon against predefined start and stop codon lists.

- ATG/AUG is identified as the start codon.
- TAA/UAA, TAG/UAG and TGA/UGA are identified as stop codons.

### Step 7: Handling Incomplete Codons

Since a codon must contain exactly three nucleotides, the program checks the length of each codon.

If the final group contains fewer than three nucleotides, it is identified as an incomplete codon and is not translated.

### Step 8: Displaying the Final Results

The program displays:

- The complete codon table.
- The divided codon sequence.
- The corresponding amino acid sequence.
- Identified start and stop codons.
- Incomplete codons, if present.

## 6. Sample Input and Output

### Example 1: DNA Sequence

**Input:**

```text
ATGGCTTTTTAA
```

**Output:**

| Codon | Amino Acid |
|---|---|
| ATG | Methionine |
| GCT | Alanine |
| TTT | Phenylalanine |
| TAA | Stop |

**Translated amino acid sequence:**

```text
Methionine - Alanine - Phenylalanine - Stop
```

**Start codon:** ATG

**Stop codon:** TAA

### Example 2: RNA Sequence

**Input:**

```text
AUGGCUUUUUAA
```

**Output:**

| Codon | Amino Acid |
|---|---|
| AUG | Methionine |
| GCU | Alanine |
| UUU | Phenylalanine |
| UAA | Stop |

### Example 3: Incomplete Codon

**Input:**

```text
ATGGCTTTTA
```

**Output:**

| Codon | Result |
|---|---|
| ATG | Methionine |
| GCT | Alanine |
| TTT | Phenylalanine |
| A | Incomplete codon |

The final nucleotide group contains only one base and therefore cannot be translated.

### Example 4: Invalid Input

**Input:**

```text
ATGXGCT
```

**Output:**

```text
Invalid sequence! Enter only A, T, G, C or U.
```

## 7. Comparison with Existing GitHub Codon Table Repositories

To compare the codon table developed in this project with existing implementations, the following public GitHub repository was referred to:

**Reference Repository:**

[GitHub – linsalrob/genetic_codes](https://github.com/linsalrob/genetic_codes)

This repository provides Python-based tools for translating DNA sequences using genetic code tables, including the standard genetic code.

### Comparison

| Feature | This Project | Reference Repository |
|---|---|---|
| Standard genetic code | Yes | Yes |
| 64 possible codons | Yes | Yes |
| Codon-to-amino-acid mapping | Python dictionary | Genetic code library |
| DNA sequence translation | Yes | Yes |
| RNA codon support | Yes | Yes |
| Start and stop codon identification | Yes | Supported through genetic code information |
| Multiple genetic codes | No | Yes |

### Comparison Findings

The codon assignments in this project follow the standard genetic code and are consistent with the standard translation table used by the reference repository.

Both implementations establish the relationship between nucleotide triplets and their corresponding amino acids.

However, the reference repository provides additional functionality, including support for alternative genetic codes and different translation tables.

The present project focuses on implementing the standard genetic code using basic Python programming concepts, making it suitable for understanding the fundamentals of codon translation.

## 8. Python Concepts Demonstrated

The project applies the following fundamental Python concepts:

1. **Dictionaries:** Used to store codons and their corresponding amino acids.
2. **Functions:** Used to organize operations such as displaying the codon table, validating sequences and translating sequences.
3. **Lists:** Used to store codons and amino acids.
4. **For loops:** Used to iterate through nucleotide sequences and dictionaries.
5. **Conditional statements:** Used for input validation and identifying start and stop codons.
6. **String slicing:** Used to divide nucleotide sequences into groups of three.
7. **String methods:** Used for uppercase conversion and replacing RNA uracil with DNA thymine.
8. **User input:** Used to accept nucleotide sequences from the user.

## 9. Limitations

- The program uses only the standard genetic code and does not include alternative genetic codes.
- Translation is performed from the first nucleotide in the input sequence, without searching for a reading frame or automatically locating a start codon.
- The program identifies start and stop codons but does not enforce translation termination at the first stop codon.
- The program does not perform biological sequence alignment or predict complete protein structures.

## 10. Conclusion

The Codon Table Generator successfully demonstrates how Python programming can be applied to basic biological sequence analysis.

By creating a dictionary of 64 codons and implementing sequence validation, codon division and amino acid translation, the project provides an understanding of the relationship between nucleotide sequences and protein synthesis.

The project also demonstrates how fundamental Python concepts such as dictionaries, lists, loops, functions and conditional statements can be used to solve a biological problem.

The additional RNA translation feature extends the functionality of the program and provides a basic understanding of DNA and RNA codon equivalence.

Overall, this project helped develop practical programming skills and an understanding of the standard genetic code and its application in bioinformatics.

## 11. How to Run the Project

### Requirements

- Python 3 installed on your computer.
- A Python editor such as VS Code, IDLE or Jupyter Notebook.

### Steps

1. Clone or download this repository.
2. Open the project folder in your Python editor.
3. Run the Python file:

```bash
python codon_table_generator.py
```

4. Enter a DNA or RNA sequence when prompted.
5. View the translated amino acid sequence and other results.

### Repository Structure

```text
Codon-Table-Generator/
│
├── codon_table_generator.py
│
└── README.md
```

## 12. Author

**Project:** Python Assessment 2 – Codon Table Generator

**Course:** Bioinformatics and Biotechnology

**Language:** Python

**Repository:** [Add your GitHub repository link here]

---

**End of Project**
