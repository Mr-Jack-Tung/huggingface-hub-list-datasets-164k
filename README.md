# HUGGINGFACE-HUB LIST DATASETS: 164k
Date: 17 Jun 2024
From: Mr.Jack

```
from datasets import list_datasets

huggingface_hub_list_datasets = list_datasets()

print("\n","huggingface_hub_list_datasets:",len(huggingface_hub_list_datasets),"datasets")

# huggingface_hub_list_datasets: 163.963 datasets

for dataset_path in huggingface_hub_list_datasets:
    print(dataset_path)
```
