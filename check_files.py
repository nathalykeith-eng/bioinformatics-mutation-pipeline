# check_files.py
import os

BASE_FOLDER = "bioinfo_projeto"
REF_FOLDER = "references"   # nome da pasta onde você colocará os refs (pode ser 'referencias' se preferir)

def find_fastas(base):
    result = {}
    if not os.path.isdir(base):
        return None, f"ERROR: base folder '{base}' not found."
    for patient in sorted(os.listdir(base)):
        ppath = os.path.join(base, patient)
        if not os.path.isdir(ppath):
            continue
        files = [f for f in sorted(os.listdir(ppath)) if f.lower().endswith(".fasta") or f.lower().endswith(".fa")]
        result[patient] = files
    return result, None

def find_references(ref_folder):
    if not os.path.isdir(ref_folder):
        return None, f"WARNING: reference folder '{ref_folder}' not found."
    refs = [f for f in sorted(os.listdir(ref_folder)) if f.lower().endswith(".fasta") or f.lower().endswith(".fa")]
    return refs, None

def main():
    print("CHECK: scanning project structure...\n")
    fastas, err = find_fastas(BASE_FOLDER)
    if err:
        print(err)
        return
    refs, rerr = find_references(REF_FOLDER)
    if rerr:
        print(rerr)
        refs = []
    # print summary
    total_files = 0
    for p, files in fastas.items():
        print(f"Patient: {p} -> {len(files)} fasta file(s)")
        for f in files:
            print("   -", f)
            total_files += 1
    print(f"\nTotal patients: {len(fastas)} | Total fasta files found: {total_files}\n")
    if refs:
        print("Reference FASTA files found in '{}':".format(REF_FOLDER))
        for r in refs:
            print("   -", r)
    else:
        print("No reference FASTA files found in '{}'. You should add files like ACTC1_ref.fasta, MYH7_ref.fasta, etc.".format(REF_FOLDER))
    # cross-check which genes need refs
    needed = set()
    for files in fastas.values():
        for f in files:
            # try extract gene name from filename: e.g. MYH7.fasta or paciente01_MYH7.fasta
            name = f
            if "_" in name:
                # if file named pacienteXX_gene.fasta, take after underscore
                parts = name.rsplit("_", 1)
                if len(parts) == 2:
                    name = parts[1]
            gene = name.replace(".fasta", "").replace(".fa", "")
            needed.add(gene)
    print("\nGenes detected across patients:")
    for g in sorted(needed):
        refname1 = f"{g}_ref.fasta"
        refname2 = f"{g}__ref.fasta"  # in case naming differences
        has_ref = (refname1 in refs) or (refname2 in refs) or (g + ".fasta" in refs)
        print(f"  {g}  -> reference present? {'YES' if has_ref else 'NO'}")
    print("\nCheck complete. If any reference is missing, create a file named <GENE>_ref.fasta inside the '{}' folder.".format(REF_FOLDER))

if __name__ == "__main__":
    main()
