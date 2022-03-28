from pyopenie import OpenIE5
import json

extractor = OpenIE5('http://localhost:8000')

corpus_path = 'data/arc/ARC-V1-Feb2018-2/ARC_Corpus.txt'

with open(corpus_path) as f:
    text = f.read()

sentences = text.split('\n')

extractions = []

starting_index = 0

with open("count.txt", "r") as f:
    val = f.readline()
    starting_index = int(val)

for i, s in enumerate(sentences[starting_index:]):
    if s:
        try:
            es = extractor.extract(s)
            triplets = []
            for e in es:
                if e["confidence"] < 0.3:
                    continue

                if e["extraction"]["arg2s"]:
                    for x in e["extraction"]["arg2s"]:
                        t = []
                        t.append(e["extraction"]["rel"]["text"])
                        t.append(e["extraction"]["arg1"]["text"])
                        t.append(x["text"])
                        triplets.append(t)
                elif e["extraction"]["arg2"]:
                    t = []
                    t.append(e["extraction"]["rel"]["text"])
                    t.append(e["extraction"]["arg1"]["text"])
                    t.append(e["extraction"]["arg2"]["text"])
                    triplets.append(t)
                else:
                    continue
            for t in triplets:
                with open("triplets.txt", "a") as f:
                    string = ','.join(t)
                    f.write(string + '\n')
        except:
            print('uh oh')
            print('\n')

    with open('count.txt', 'w') as f:
        f.write(str(i+starting_index+1))

