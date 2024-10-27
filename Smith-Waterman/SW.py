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

def show_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print("")


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
matrix = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
maximum=0
positionX=0
positionY=0
for i in range(1,rows+1):
    for j in range(1,columns+1):
        up=matrix[i-1][j] + gap
        left=matrix[i][j-1] + gap
        if sequences[0][i-1]==sequences[1][j-1]:
            diagonal = matrix[i - 1][j - 1] + match
        else:
            diagonal = matrix[i - 1][j - 1] + missmatch
        if max(up, left, diagonal) <= 0:
            matrix[i][j] = 0
        else:
            matrix[i][j] = max(up, left, diagonal)
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            positionX = i
            positionY = j
seq1=""
seq2=""
while matrix[positionX][positionY] != 0:
    up=matrix[positionX-1][positionY] + gap
    left=matrix[positionX][positionY-1] + gap
    if sequences[0][positionX-1]==sequences[1][positionY-1]:
        diagonal = matrix[positionX-1][positionY-1] + match
    else:
        diagonal = matrix[positionX-1][positionY-1] + missmatch
    if up < 0:
        up=0
    if left < 0:
        left=0
    if diagonal < 0:
        diagonal=0
    if matrix[positionX][positionY] == up:
        seq1=seq1+sequences[0][positionX-1]
        seq2=seq2+"-"
        positionX=positionX-1
        continue
    if matrix[positionX][positionY] == left:
        seq1=seq1+"-"
        seq2=seq2+sequences[1][positionY-1]
        positionY=positionY-1
        continue
    if matrix[positionX][positionY] == diagonal:
        seq1=seq1+sequences[0][positionX-1]
        seq2=seq2+sequences[1][positionY-1]
        positionX=positionX-1
        positionY=positionY-1
        continue
show_matrix(matrix)

with open("result.txt", "w") as file:
    file.write(seq1[::-1])
    file.write("\n")
    file.write(seq2[::-1])






