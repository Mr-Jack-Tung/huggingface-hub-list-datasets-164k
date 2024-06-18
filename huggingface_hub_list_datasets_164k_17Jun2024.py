# HUGGINGFACE-HUB LIST DATASETS
"""
File: huggingface_hub_list_datasets_164k_17Jun2024.py
- From: Mr.Jack
- Date: 17 Jun 2024
"""

# % pip install datasets
import asyncio
from datasets import list_datasets

huggingface_hub_list_datasets = list_datasets()

print("\n","HUGGINGFACE-HUB LIST DATASETS:",len(huggingface_hub_list_datasets),"datasets")

# (17/06) HUGGINGFACE-HUB LIST DATASETS: 163.963 datasets
# (18/06) HUGGINGFACE-HUB LIST DATASETS: 164.588 datasets

# async def main():
#     for dataset_path in huggingface_hub_list_datasets:
#         print(dataset_path)
#         await asyncio.sleep(0.1)

from datasets import get_dataset_config_names
from datasets import load_dataset_builder

async def main(): 
    # for dataset_path in huggingface_hub_list_datasets:
    for dataset_path in huggingface_hub_list_datasets[:5]:
        print("\n","="*60)
        print("Dataset path:",dataset_path)
    
        configs = get_dataset_config_names(dataset_path)
        print("Subset:",configs)

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

            await asyncio.sleep(0.5)

asyncio.run(main())

# ... 164.588 datasets
