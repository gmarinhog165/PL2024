import re
import sys


def get_queries(csv_data):
    # regex para dar split de linhas csv
    pattern = re.compile(r',')
    # inicializar data structs para as queries
    modalidades = set()
    apto = 0
    inapto = 0
    age_distribution = {}

    # processamento de dados do csv
    lines = csv_data.split('\n')
    # remover a primeira linha de cabeçalho
    lines = lines[1:]
    for line in lines:
        # de forma a passar caso haja empty lines, como no caso deste csv que tinha no fim
        if not line.strip():
            continue
        # remover o \n do ultimo elemento
        line = line.rstrip('\n')
        # guardar os elementos entre ',' numa lista
        fields = pattern.split(line)

        modalidades.add(fields[8])
        # verifica se o campo "resultado" é true ou false com regex
        if re.match(r'^true$', fields[12]):
            apto += 1
        elif re.match(r'^false$', fields[12]):
            inapto += 1

        # cast para inteiro
        age = int(fields[5])

        # determina o intervalo de idade com regex, // é divisao inteira, ou seja arredonda
        # para baixo e volta a multiplicar por 5 para obter o limite inferior
        # o limite superior é só somar 4
        interval = f"{(age // 5) * 5}-{((age // 5) * 5) + 4}"

        # guarda essa informação no dicionário
        if interval in age_distribution:
            age_distribution[interval] += 1
        else:
            age_distribution[interval] = 1

    # ordenação do set em lista e print como especie de <ol>
    modalidades_sorted = sorted(modalidades)
    print("Modalidades (Ordenadas Alfabeticamente):")
    for i, modalidade in enumerate(modalidades_sorted, start=1):
        print(f"{i}. {modalidade}")

    # calculo do total de aptos e inaptos e print das percentagens
    total_records = apto + inapto
    percentage_apto = float((apto / total_records) * 100)
    percentage_inapto = float((inapto / total_records) * 100)
    print(f"Percentagem de aptos: {percentage_apto:.2f}%")
    print(f"Percentagem de inaptos: {percentage_inapto:.2f}%")

    # imprime o dicionário ordenado pelo escalao etario, item[0] = key, item[1] = value
    print("Distribuição de atletas por escalão etário:")
    total_athletes = sum(age_distribution.values())
    for interval, count in sorted(age_distribution.items(), key=lambda item: item[0]):
        percentage = (count / total_athletes) * 100
        print(f"[{interval}]: {count} ({percentage:.2f}%)")


def main():
    csv_data = sys.stdin.read()
    get_queries(csv_data)


if __name__ == '__main__':
    main()
