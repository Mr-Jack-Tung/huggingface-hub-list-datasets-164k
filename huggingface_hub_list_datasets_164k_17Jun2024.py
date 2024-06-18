# HUGGINGFACE-HUB LIST DATASETS
"""
File: huggingface_hub_list_datasets_164k_17Jun2024.py
- From: Mr.Jack
- Date: 17 Jun 2024
"""
# % pip install datasets
from datasets import list_datasets

huggingface_hub_list_datasets = list_datasets()

print("\n","huggingface_hub_list_datasets:",len(huggingface_hub_list_datasets),"datasets")

# for dataset_path in huggingface_hub_list_datasets:
#     print(dataset_path)

# (17/06) huggingface_hub_list_datasets: 163.963 datasets
# (18/06) huggingface_hub_list_datasets: 164.588 datasets

for dataset_path in huggingface_hub_list_datasets[:5]:
    print("\n","="*60)
    print("Dataset path:",dataset_path)

    from datasets import get_dataset_config_names
    configs = get_dataset_config_names(dataset_path)
    print("Subset:",configs)

    from datasets import load_dataset_builder
    for subset in configs:
        ds_builder = load_dataset_builder(path=dataset_path, name=subset)
        dataset_info = ds_builder.info
        print("\n",subset,":",dataset_info)

        # print("\n","splits['test']:",dataset_info.splits['test'])
        # print("\n","splits['train']:",dataset_info.splits['train'])
        # print("\n","splits['validation']:",dataset_info.splits['validation'])

        # dataset = load_dataset(path=dataset_path, name=subset, split="train", trust_remote_code=True)
        # print("\n",dataset)

        # dataset_path = "./huggingface_datasets/" + dataset_path + "/" + subset
        # dataset.save_to_disk(dataset_path=dataset_path)
        # print("\n","Save dataset to:",dataset_path)
