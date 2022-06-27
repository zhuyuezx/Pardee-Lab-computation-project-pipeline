import sys

argc = len(sys.argv)
amino_seq = "ACDEFGHIKLMNPQRSTVWY"

if argc < 2 or argc > 3:
    print("Usage1: python3 generate_mutation.py all -- generate all mutation combinations")
    print("Usage2: python3 generate_mutation.py [position] -- generate mutation at designated point")
    print("Usage3: python3 generate_mutation.py [start pos] [end pos] -- generate mutation at designated interval")
    exit()

with open("GFP11_template.txt", 'r') as f:
    heading = f.readline().strip()
    curr_line = f.readline().strip()
    body = curr_line
    while curr_line != "":
        curr_line = f.readline()
        body += curr_line
#print(heading)
#print(body)
if argc == 2 and sys.argv[1] == "all":
    start = 0
    end = len(body)
elif argc == 2 and sys.argv[1].isdigit():
    start = int(sys.argv[1])
    end = start + 1
    if start < 0 or start > len(body):
        print("Invalid point input")
        exit()
elif argc == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    if start < 0 or start >= end or end > len(body):
        print("Invalid interval input")
        exit()
else:
    print("Invalid no-digit input")
    exit()
#print(f"start:{start}, end:{end}")

for i in range(start, end):
    for j in range(len(amino_seq)):
        if body[i] == amino_seq[j]:
            continue
        name = f"mutate_amino{i}_to_{amino_seq[j]}.fasta"
        with open(name, 'w') as f:
            print(heading, file = f)
            print(body[0: i] + amino_seq[j] + body[i + 1:], file = f)


