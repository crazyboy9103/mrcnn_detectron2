from SSD import *
import json
#dic = json.load(open("dic.json","r"))
label_map = json.load(open("labels.json", "r"))

decode = {}
for k, v in label_map.items():
    decode[v] = k

dataset = CustomDataset("temp_data_path") # temp_data_path ignored if dataset.pt exists

counts = {label:0 for label in label_map}

labels = dataset.labels
for i in range(len(labels)):
    for label in labels[i]['labels']:
        counts[decode[label]] += 1


print("bbox count", counts)
