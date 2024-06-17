# HUGGINGFACE-HUB LIST DATASETS
"""
File: huggingface_hub_list_datasets_164k_17Jun2024.py
- From: Mr.Jack
- Date: 17 Jun 2024
"""

from datasets import list_datasets

huggingface_hub_list_datasets = list_datasets()

print("\n","huggingface_hub_list_datasets:",len(huggingface_hub_list_datasets),"datasets")

# huggingface_hub_list_datasets: 163.963 datasets

# for dataset_path in huggingface_hub_list_datasets:
for dataset_path in huggingface_hub_list_datasets[:5]:
    print("\n","="*60)
    print("dataset path:",dataset_path)

    from datasets import get_dataset_config_names
    configs = get_dataset_config_names(dataset_path)
    print("Subset:",configs)

    from datasets import load_dataset_builder
    for subset in configs:
        ds_builder = load_dataset_builder(path=dataset_path,name=subset)
        print("\n",subset,":",ds_builder.info)

        # dataset = load_dataset(path=dataset_path, name=subset, split="train", trust_remote_code=True)
        # print("\n",dataset)

        # dataset.save_to_disk(dataset_path="./huggingface_datasets/" + dataset_path)

