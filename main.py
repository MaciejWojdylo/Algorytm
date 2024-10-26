import argparse
sequences = []
nameseq = []
def main(file_path):
    try:
        with open("seq1.fasta", "r") as f:
            tmp = ""
            for l in f:
                if l.startswith(">"):
                    nameseq.append(l.strip().replace(">",""))
                    if tmp == "":
                        continue
                    else:
                        sequences.append(tmp)
                        tmp = ""
                else:
                    tmp += l.strip().upper()
        if tmp:
            sequences.append(tmp)
    except FileNotFoundError:
        print(f"Plik {file_path} nie został znaleziony.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program do odczytu pliku FASTA")
    parser.add_argument("-i","--input", default="seq1.fasta" , help="Ścieżka do pliku FASTA") #required=True w miejsce default  default="seq1.fasta"
    args = parser.parse_args()
    main(args.input)
rows = len(sequences[0])
columns = len(sequences[1])
matrix = [[0 for _ in range(columns)] for _ in range(rows+1)]
