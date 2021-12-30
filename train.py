# +
from SSD import *
import argparse
def main(parallel):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')     
    dataset = CustomDataset("/data/dataset/recsys/e8/data_1224")
    #dataset = CustomDataset("/dataset")
    model = Model(num_classes=dataset.num_classes, device = device, batch_size=64, parallel=parallel)
    model.fit(dataset, max_epochs=20)
    return dataset, model

parser = argparse.ArgumentParser()
# argument는 원하는 만큼 추가한다.
parser.add_argument('-p', type=int, default=0,
                            help='1 for parallel 0 otherwise')

args = parser.parse_args()

dataset, model = main(bool(args.p))
