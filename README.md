# 🧬 Bioinformatics Mutation Detection Pipeline

This project implements a simple and educational pipeline for detecting mutations in FASTA gene sequences, comparing patient samples against reference sequences, generating automated QC reports, and producing summary statistics and visualizations.

It was built as a practical exercise to simulate a small real-world genomic workflow using Python.

---

## 📁 Project Structure

```
Bio-projeto/
│
├── patients/                 # Patient FASTA files organized by patient ID
├── references/               # Reference FASTA sequences for each gene
├── qc_results/               # QC output files (ignored by Git)
├── check_files.py            # Validates folder structure and presence of files
├── detect_mutations.py       # Compares patient sequences with references and detects mutations
├── generate_report.py        # Creates summary CSVs and plots using matplotlib
├── mutations_results.csv     # Auto-generated mutation table (ignored by Git)
├── report_resumido_*.csv     # Summary mutation reports (ignored by Git)
├── grafico_*.png             # Charts generated (ignored by Git)
└── .gitignore                # Excludes auto-generated and temporary files
```

---

## 🧪 Features

### ✔ Mutation detection  
- Compares each patient's gene FASTA file with the corresponding reference sequence.  
- Detects mismatches and records:
  - Patient  
  - Gene  
  - Position  
  - Reference nucleotide  
  - Alternative nucleotide  

### ✔ Quality control  
- Ensures all patient folders and reference files exist.  
- Generates a QC report (`qc_relatorio.txt`).

### ✔ Summary reports  
The script `generate_report.py` produces:
- Total mutations per patient (CSV)
- Total mutations per gene (CSV)
- Mutation distribution plots (PNG)

### ✔ Fully automated pipeline  
Run the scripts in this order:

```bash
C:\Users\marcos\AppData\Local\Programs\Python\Python313\python.exe detect_mutations.py
C:\Users\marcos\AppData\Local\Programs\Python\Python313\python.exe generate_report.py
```

---

## 🛠 Requirements

- Python 3.10+
- pandas  
- matplotlib  
- Biopython

Install dependencies:

```bash
C:\Users\marcos\AppData\Local\Programs\Python\Python313\python.exe -m pip install pandas matplotlib biopython
```

---


## 📌 Notes

- Auto-generated files (plots, CSVs, QC logs) are excluded via `.gitignore`.
- FASTA sequences included in this repository are for educational use only.


