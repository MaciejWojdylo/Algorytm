import argparse

sequences = []
nameseq = []


def main(file_path):
    try:
        with open(file_path, "r") as f:
            tmp = ""
            for l in f:
                if l.startswith(">"):
                    nameseq.append(l.strip().replace(">", ""))
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
        exit(1)

def printMatrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end="\t")
        print("")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program do odczytu pliku FASTA")
    parser.add_argument("-i", "--input", default="seq1.fasta",help="Ścieżka do pliku FASTA")
    parser.add_argument("-g", "--gap", default=-2)
    parser.add_argument("-m", "--match", default=1)
    parser.add_argument("-mm", "--missmatch", default=-1)
    args = parser.parse_args()
    main(args.input)
gap = args.gap
match = args.match
missmatch = args.missmatch
rows = len(sequences[0])
columns = len(sequences[1])
matrix = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
for i in range(1,rows+1):
    matrix[i][0] = matrix[i-1][0]+gap
for j in range(1,columns+1):
    matrix[0][j] = matrix[0][j-1]+gap
for i in range(1,rows+1):
    for j in range(1,columns+1):
        up= matrix[i-1][j]+gap
        left = matrix[i][j-1]+gap
        if sequences[0][i-1] == sequences[1][j-1]:
            diagonal = matrix[i-1][j-1] + match
        else:
            diagonal = matrix[i-1][j-1] + missmatch
        matrix[i][j] = max(up,left,diagonal)
seq1 = ""
seq2 = ""
i = rows
j = columns
while i >= 1 and j >= 1:
    up = matrix[i-1][j]+gap
    left = matrix[i][j-1]+gap
    if(sequences[0][i-1] == sequences[1][j-1]):
        diagonal = matrix[i-1][j-1] + match
    else:
        diagonal = matrix[i-1][j-1] + missmatch
    if up == matrix[i][j]:
        seq1 += sequences[0][i - 1]
        seq2 += "-"
        i = i-1
    if left == matrix[i][j]:
        seq1 += "-"
        seq2 += sequences[1][j - 1]
        j = j-1
    if diagonal == matrix[i][j]:
        seq1 += sequences[0][i - 1]
        seq2 += sequences[1][j - 1]
        i = i-1
        j = j-1
if(i!=0):
    seq1 += sequences[0][i - 1]
else :
    seq1 += "-"
if(j!=0):
    seq2 += sequences[1][j - 1]
else:
    seq2 += "-"
with open("output", "w") as f:
    f.write("Result:")
    f.write("\n")
    f.write(seq1[::-1])
    f.write("\n")
    f.write(seq2[::-1])