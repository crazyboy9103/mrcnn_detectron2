""" from SSD import *
dataset = CustomDataset("temp")
labels = dataset.labels

for idx, label in labels.items():
    temp_labels = label['labels']
    for i, temp_label in enumerate(temp_labels):
        if temp_label % 3 == 0:
            temp_labels[i] = temp_label - 2

            continue
        if temp_label % 3 == 1:
            temp_labels[i] = temp_label + 2
            continue
    labels[idx] = temp_labels

dataset.labels = labels
dataset.save()
 """
import json
labels = json.load(open("labels.json", "r"))
for k, v in labels.items():
    if v % 3 == 0:
        labels[k] = v - 2
        continue
    if v % 3 == 1:
        labels[k] = v + 2
        continue
json.dump(labels, open("labels.json", "w"))