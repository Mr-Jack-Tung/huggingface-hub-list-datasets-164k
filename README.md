# HUGGINGFACE-HUB LIST DATASETS: 170.112 datasets
- From: Mr.Jack
- Date: 17 Jun 2024
- If you like what I do, give me a star ^^ ~> ⭐

```
# % pip install datasets
import asyncio
from datasets import list_datasets

huggingface_hub_list_datasets = list_datasets()

print("\n","HUGGINGFACE-HUB LIST DATASETS:",len(huggingface_hub_list_datasets),"datasets")

# (17/06) HUGGINGFACE-HUB LIST DATASETS: 163.963 datasets
# (18/06) HUGGINGFACE-HUB LIST DATASETS: 164.588 datasets
# (29/06) HUGGINGFACE-HUB LIST DATASETS: 170.112 datasets

# for dataset_path in huggingface_hub_list_datasets:
#     print(dataset_path)

from datasets import get_dataset_config_names
from datasets import load_dataset_builder

async def main(): 
    # for dataset_path in huggingface_hub_list_datasets:
    for dataset_path in huggingface_hub_list_datasets[:5]:
        print("\n","="*60)
        print("Dataset path:",dataset_path)

        configs = get_dataset_config_names(dataset_path, trust_remote_code=True)
        print("Subset:",configs)

        for subset in configs:
	    ds_builder = load_dataset_builder(path=dataset_path, name=subset, trust_remote_code=True)
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

# ... 170.112 datasets
```


## HUGGINGFACE_HUB LOAD DATASET
- From: Mr.Jack
- Date: 17 Jun 2024

```
# % pip install datasets
from datasets import load_dataset
from datasets import get_dataset_config_names

dataset_path = 'Salesforce/wikitext'

configs = get_dataset_config_names(dataset_path, trust_remote_code=True)

print("\n","Subset:",configs)

# Subset: ['wikitext-103-raw-v1', 'wikitext-103-v1', 'wikitext-2-raw-v1', 'wikitext-2-v1']

for subset in configs:
    dataset = load_dataset(path=dataset_path, name=subset, trust_remote_code=True)
    print("\n",subset,":",dataset)

    # dataset_path = "./huggingface_datasets/" + dataset_path + "/" + subset
    # dataset.save_to_disk(dataset_path=dataset_path)
    # print("\n","Save dataset to:",dataset_path)

from datasets import load_dataset_builder
for subset in configs:
    ds_builder = load_dataset_builder(path=dataset_path, name=subset, trust_remote_code=True)
    dataset_info = ds_builder.info
    print("\n",subset,":",dataset_info)

    # print("\n","splits['test']:",dataset_info.splits['test'])
    # print("\n","splits['train']:",dataset_info.splits['train'])
    # print("\n","splits['validation']:",dataset_info.splits['validation'])

# from datasets import load_from_disk
# dataset_path = "./huggingface_datasets/" + dataset_path + "/" + subset
# dataset = load_from_disk(dataset_path=dataset_path)
# print("\n","Load dataset from disk:",dataset_path)
# print(dataset)

"""
Subset: ['wikitext-103-raw-v1', 'wikitext-103-v1', 'wikitext-2-raw-v1', 'wikitext-2-v1']

Downloading data: 100%|███████████████████████████████████████████████| 733k/733k [00:00<00:00, 1.27MB/s]
Downloading data: 100%|███████████████████████████████████████████████| 157M/157M [00:09<00:00, 15.8MB/s]
Downloading data: 100%|███████████████████████████████████████████████| 157M/157M [00:10<00:00, 15.6MB/s]
Downloading data: 100%|███████████████████████████████████████████████| 657k/657k [00:00<00:00, 2.19MB/s]
Generating test split: 100%|██████████████████████████████| 4358/4358 [00:00<00:00, 125060.91 examples/s]
Generating train split: 100%|██████████████████████| 1801350/1801350 [00:00<00:00, 2960200.88 examples/s]
Generating validation split: 100%|████████████████████████| 3760/3760 [00:00<00:00, 711765.27 examples/s]
wikitext-103-raw-v1 : DatasetDict({
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
...
 wikitext-103-raw-v1 : DatasetInfo(description='', citation='', homepage='', license='', features={'text': Value(dtype='string', id=None)}, post_processed=None, supervised_keys=None, task_templates=None, builder_name='parquet', dataset_name='wikitext', config_name='wikitext-103-raw-v1', version=0.0.0, splits={'test': SplitInfo(name='test', num_bytes=1305088, num_examples=4358, shard_lengths=None, dataset_name='wikitext'), 'train': SplitInfo(name='train', num_bytes=546500949, num_examples=1801350, shard_lengths=[1648675, 152675], dataset_name='wikitext'), 'validation': SplitInfo(name='validation', num_bytes=1159288, num_examples=3760, shard_lengths=None, dataset_name='wikitext')}, download_checksums={'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-103-raw-v1/test-00000-of-00001.parquet': {'num_bytes': 732610, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-103-raw-v1/train-00000-of-00002.parquet': {'num_bytes': 156987808, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-103-raw-v1/train-00001-of-00002.parquet': {'num_bytes': 157088770, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-103-raw-v1/validation-00000-of-00001.parquet': {'num_bytes': 657209, 'checksum': None}}, download_size=315466397, post_processing_size=None, dataset_size=548965325, size_in_bytes=864431722)
...
"""
```

## Read Fineweb Dataset (15-trillion tokens, 44TB disk space) with datatrove is supper fast ... you can start using it right away!
- URL: https://huggingface.co/datasets/HuggingFaceFW/fineweb

```
# % pip install datatrove
from datatrove.pipeline.readers import ParquetReader

# limit determines how many documents will be streamed (remove for all)
# to fetch a specific dump: hf://datasets/HuggingFaceFW/fineweb/data/CC-MAIN-2024-10
# replace "data" with "sample/100BT" to use the 100BT sample
data_reader = ParquetReader("hf://datasets/HuggingFaceFW/fineweb/data", limit=3) 
for document in data_reader():
    # do something with document
    print("\n",document)

# ...
```
