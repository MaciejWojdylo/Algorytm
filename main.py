sequences = []
tmp = ""
with open("seq1.fasta" , "r") as f:
    for l in f:
        if(l.startswith(">")):
            if(tmp == ""):
                continue
            else:
                sequences.append(tmp)
                tmp = ""
        else:
            tmp+=l.strip().upper()
if(tmp):
    sequences.append(tmp)

matrix = [[0]*len(sequences[0])]*len(sequences[1])
print(matrix)
print(sequences)