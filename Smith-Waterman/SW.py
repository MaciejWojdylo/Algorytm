import argparse

sequences = []

def main(file_path):
    seq = ""
    with open(file_path, "r") as file:
        for line in file:
            if not line.startswith(">"):
                seq = seq + line.strip().upper()
            else:
                if not seq =="":
                    sequences.append(seq)
                    seq=""
        sequences.append(seq)
        print(sequences)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program do odczytu pliku FASTA")
    parser.add_argument("-i", "--input", default="seq1.fasta", help="Ścieżka do pliku FASTA")
    parser.add_argument("-g", "--gap", default=-2)
    parser.add_argument("-m", "--match", default=1)
    parser.add_argument("-mm", "--missmatch", default=-1)
    args = parser.parse_args()
    main(args.input)

gap = args.gap
match = args.match
missmatch = args.missmatch
rows=len(sequences[0])
columns=len(sequences[1])

