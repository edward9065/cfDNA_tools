import os
import gzip
from tqdm import tqdm
import json

directory = "./data"
files = os.listdir(directory)
bed_gz_files = [file for file in files if file.endswith('.bed.gz')]

chr_files = {}

for file in tqdm(bed_gz_files):
    with gzip.open(os.path.join(directory, file), "rt") as f:
        for line in f:
            chr, start, stop, methylation = line.split()
            if chr in chr_dict:
                chr_dict[chr].append((float(start) + float(stop)) / 2)
            else:
                chr_dict[chr] = [((float(start) + float(stop)) / 2)]

with open("./data/data.txt", 'w') as file:
    file.write(json.dumps(chr_dict))