# HUGGINGFACE-HUB LIST DATASETS: 163.963 datasets
- From: Mr.Jack
- Date: 17 Jun 2024

```
from datasets import list_datasets

huggingface_hub_list_datasets = list_datasets()

print("\n","huggingface_hub_list_datasets:",len(huggingface_hub_list_datasets),"datasets")

# huggingface_hub_list_datasets: 163.963 datasets

for dataset_path in huggingface_hub_list_datasets:
    print(dataset_path)

# ... 163.963 datasets
```


## HUGGINGFACE_HUB LOAD DATASET
- From: Mr.Jack
- Date: 17 Jun 2024

```
from datasets import load_dataset
from datasets import get_dataset_config_names

dataset_path = 'Salesforce/wikitext'

configs = get_dataset_config_names(dataset_path)

print("\n","Subset:",configs)

# Subset: ['wikitext-103-raw-v1', 'wikitext-103-v1', 'wikitext-2-raw-v1', 'wikitext-2-v1']

for subset in configs:
	dataset = load_dataset(path=dataset_path, name=subset) 
	print(dataset)

"""
Downloading data: 100%|███████████████████████████████████████████████| 733k/733k [00:00<00:00, 1.27MB/s]
Downloading data: 100%|███████████████████████████████████████████████| 157M/157M [00:09<00:00, 15.8MB/s]
Downloading data: 100%|███████████████████████████████████████████████| 157M/157M [00:10<00:00, 15.6MB/s]
Downloading data: 100%|███████████████████████████████████████████████| 657k/657k [00:00<00:00, 2.19MB/s]
Generating test split: 100%|██████████████████████████████| 4358/4358 [00:00<00:00, 125060.91 examples/s]
Generating train split: 100%|██████████████████████| 1801350/1801350 [00:00<00:00, 2960200.88 examples/s]
Generating validation split: 100%|████████████████████████| 3760/3760 [00:00<00:00, 711765.27 examples/s]
DatasetDict({
    test: Dataset({
        features: ['text'],
        num_rows: 4358
    })
    train: Dataset({
        features: ['text'],
        num_rows: 1801350
    })
    validation: Dataset({
        features: ['text'],
        num_rows: 3760
    })
})
Downloading data: 100%|███████████████████████████████████████████████| 722k/722k [00:00<00:00, 1.26MB/s]
Downloading data: 100%|███████████████████████████████████████████████| 156M/156M [00:10<00:00, 15.2MB/s]
Downloading data: 100%|███████████████████████████████████████████████| 156M/156M [00:09<00:00, 16.4MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 655k/655k [00:01<00:00, 414kB/s]
Generating test split: 100%|██████████████████████████████| 4358/4358 [00:00<00:00, 611575.78 examples/s]
Generating train split: 100%|██████████████████████| 1801350/1801350 [00:00<00:00, 3011198.22 examples/s]
Generating validation split: 100%|███████████████████████| 3760/3760 [00:00<00:00, 1349066.13 examples/s]
DatasetDict({
    test: Dataset({
        features: ['text'],
        num_rows: 4358
    })
    train: Dataset({
        features: ['text'],
        num_rows: 1801350
    })
    validation: Dataset({
        features: ['text'],
        num_rows: 3760
    })
})
Downloading data: 100%|███████████████████████████████████████████████| 733k/733k [00:00<00:00, 2.03MB/s]
Downloading data: 100%|█████████████████████████████████████████████| 6.36M/6.36M [00:00<00:00, 11.6MB/s]
Downloading data: 100%|███████████████████████████████████████████████| 657k/657k [00:00<00:00, 1.93MB/s]
Generating test split: 100%|██████████████████████████████| 4358/4358 [00:00<00:00, 715972.46 examples/s]
Generating train split: 100%|██████████████████████████| 36718/36718 [00:00<00:00, 1399575.19 examples/s]
Generating validation split: 100%|███████████████████████| 3760/3760 [00:00<00:00, 1436693.36 examples/s]
DatasetDict({
    test: Dataset({
        features: ['text'],
        num_rows: 4358
    })
    train: Dataset({
        features: ['text'],
        num_rows: 36718
    })
    validation: Dataset({
        features: ['text'],
        num_rows: 3760
    })
})
Downloading data: 100%|███████████████████████████████████████████████| 685k/685k [00:00<00:00, 2.26MB/s]
Downloading data: 100%|█████████████████████████████████████████████| 6.07M/6.07M [00:00<00:00, 13.4MB/s]
Downloading data: 100%|███████████████████████████████████████████████| 618k/618k [00:00<00:00, 2.08MB/s]
Generating test split: 100%|██████████████████████████████| 4358/4358 [00:00<00:00, 795871.33 examples/s]
Generating train split: 100%|██████████████████████████| 36718/36718 [00:00<00:00, 1388846.89 examples/s]
Generating validation split: 100%|███████████████████████| 3760/3760 [00:00<00:00, 1436693.36 examples/s]
DatasetDict({
    test: Dataset({
        features: ['text'],
        num_rows: 4358
    })
    train: Dataset({
        features: ['text'],
        num_rows: 36718
    })
    validation: Dataset({
        features: ['text'],
        num_rows: 3760
    })
})

"""
```
