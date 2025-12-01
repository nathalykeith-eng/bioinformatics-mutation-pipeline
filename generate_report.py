import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("### GERANDO RELATÓRIO RESUMIDO ###")
    
    # Lendo o CSV com encoding compatível
    df = pd.read_csv("mutations_results.csv", encoding='latin1')

    # Total de mutações por paciente
    total_mutacoes_paciente = df.groupby('Paciente').size()
    print("\nTotal de mutações por paciente:")
    print(total_mutacoes_paciente)

    # Total de mutações por gene
    total_mutacoes_gene = df.groupby('Gene').size()
    print("\nTotal de mutações por gene:")
    print(total_mutacoes_gene)

    # Salvando relatório resumido
    resumo_paciente = total_mutacoes_paciente.reset_index(name='Total_Mutacoes')
    resumo_gene = total_mutacoes_gene.reset_index(name='Total_Mutacoes')
    resumo_paciente.to_csv("report_resumido_paciente.csv", index=False, encoding='latin1')
    resumo_gene.to_csv("report_resumido_gene.csv", index=False, encoding='latin1')
    print("\nRelatórios resumidos salvos como report_resumido_paciente.csv e report_resumido_gene.csv")

    # Criando gráfico de mutações por paciente
    plt.figure(figsize=(10,6))
    total_mutacoes_paciente.plot(kind='bar', color='skyblue')
    plt.title("Total de Mutações por Paciente")
    plt.xlabel("Paciente")
    plt.ylabel("Número de Mutações")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafico_mutacoes_paciente.png")
    print("Gráfico salvo como grafico_mutacoes_paciente.png")
    plt.show()

    # Criando gráfico de mutações por gene
    plt.figure(figsize=(8,6))
    total_mutacoes_gene.plot(kind='bar', color='lightgreen')
    plt.title("Total de Mutações por Gene")
    plt.xlabel("Gene")
    plt.ylabel("Número de Mutações")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafico_mutacoes_gene.png")
    print("Gráfico salvo como grafico_mutacoes_gene.png")
    plt.show()

if __name__ == "__main__":
    main()
