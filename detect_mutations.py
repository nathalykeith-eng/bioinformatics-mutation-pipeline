import os
from Bio import SeqIO
import csv

BASE_DIR = "."
PATIENTS_DIR = os.path.join(BASE_DIR, "patients")
REFERENCES_DIR = os.path.join(BASE_DIR, "references")

def load_reference(gene):
    ref_path = os.path.join(REFERENCES_DIR, f"{gene}_ref.fasta")
    if not os.path.exists(ref_path):
        print(f"[ERRO] Referência não encontrada para {gene}: {ref_path}")
        return None
    
    record = SeqIO.read(ref_path, "fasta")
    return str(record.seq)

def load_patient_sequence(patient_path):
    record = SeqIO.read(patient_path, "fasta")
    return str(record.seq)

def compare_sequences(ref, seq):
    mutations = []
    min_len = min(len(ref), len(seq))

    for i in range(min_len):
        if ref[i] != seq[i]:
            mutations.append((i+1, ref[i], seq[i]))  # (posição, ref, paciente)

    if len(seq) > len(ref):
        mutations.append(("EXTRA_BASES", "-", seq[len(ref):]))

    return mutations

def main():
    results = []

    print("### INICIANDO DETECÇÃO DE MUTAÇÕES ###\n")

    for patient in sorted(os.listdir(PATIENTS_DIR)):
        patient_folder = os.path.join(PATIENTS_DIR, patient)

        if not os.path.isdir(patient_folder):
            continue

        print(f"Paciente: {patient}")

        for fasta_file in os.listdir(patient_folder):
            if not fasta_file.endswith(".fasta"):
                continue

            gene = fasta_file.replace(".fasta", "")
            ref_seq = load_reference(gene)

            if ref_seq is None:
                continue

            patient_fasta_path = os.path.join(patient_folder, fasta_file)
            patient_seq = load_patient_sequence(patient_fasta_path)

            mutations = compare_sequences(ref_seq, patient_seq)

            for pos, ref_base, alt_base in mutations:
                results.append([patient, gene, pos, ref_base, alt_base])

            print(f"  - {gene}: {len(mutations)} mutações detectadas")

        print()

    out_file = "mutations_results.csv"
    with open(out_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Paciente", "Gene", "Posição", "Ref", "Alt"])
        writer.writerows(results)

    print(f"\n### FINALIZADO ###")
    print(f"Arquivo gerado: {out_file}")

if __name__ == "__main__":
    main()
