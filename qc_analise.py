import os

BASE_FOLDER = "patients"
RESULTS_FOLDER = "qc_results"
os.makedirs(RESULTS_FOLDER, exist_ok=True)

def ler_fasta(caminho):
    seq = ""
    with open(caminho, "r") as f:
        for linha in f:
            if not linha.startswith(">"):
                seq += linha.strip().upper()
    return seq

def contar_nucleotideos(seq):
    contagem = {n: seq.count(n) for n in "ATGC"}
    contagem["outros"] = len(seq) - sum(contagem.values())
    contagem["total"] = len(seq)
    return contagem

relatorio = []

for paciente in sorted(os.listdir(BASE_FOLDER)):
    pasta = os.path.join(BASE_FOLDER, paciente)
    if not os.path.isdir(pasta):
        continue
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".fasta"):
            caminho = os.path.join(pasta, arquivo)
            seq = ler_fasta(caminho)
            qc = contar_nucleotideos(seq)
            status = "OK" if qc["outros"] == 0 else "ERRO"
            relatorio.append(f"{paciente}/{arquivo}: {status} | {qc}")

# Salvar resultado
with open(os.path.join(RESULTS_FOLDER, "qc_relatorio.txt"), "w") as f:
    for linha in relatorio:
        f.write(linha + "\n")

print("QC completo! Relatório salvo em qc_results/qc_relatorio.txt")
