"""
File: huggingface_hub_load_dataset_17Jun2024.py
- From: Mr.Jack
- Date: 17 Jun 2024
"""

from datasets import load_dataset
from datasets import get_dataset_config_names

dataset_path = 'Salesforce/wikitext'

configs = get_dataset_config_names(dataset_path)

print("\n","Subset:",configs)

# Subset: ['wikitext-103-raw-v1', 'wikitext-103-v1', 'wikitext-2-raw-v1', 'wikitext-2-v1']

for subset in configs:
    dataset = load_dataset(path=dataset_path, name=subset) 
    print("\n",dataset)
    
    # dataset_path = "./huggingface_datasets/" + dataset_path + "/" + subset
    # dataset.save_to_disk(dataset_path=dataset_path)
    # print("Save dataset to:",dataset_path)

from datasets import load_dataset_builder
for subset in configs:
    ds_builder = load_dataset_builder(path=dataset_path,name=subset)
    print("\n",ds_builder.info)

# from datasets import load_from_disk
# dataset_path = "./huggingface_datasets/" + dataset_path + "/" + subset
# dataset = load_from_disk(dataset_path=dataset_path)
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

 DatasetInfo(description='', citation='', homepage='', license='', features={'text': Value(dtype='string', id=None)}, post_processed=None, supervised_keys=None, task_templates=None, builder_name='parquet', dataset_name='wikitext', config_name='wikitext-103-raw-v1', version=0.0.0, splits={'test': SplitInfo(name='test', num_bytes=1305088, num_examples=4358, shard_lengths=None, dataset_name='wikitext'), 'train': SplitInfo(name='train', num_bytes=546500949, num_examples=1801350, shard_lengths=[1648675, 152675], dataset_name='wikitext'), 'validation': SplitInfo(name='validation', num_bytes=1159288, num_examples=3760, shard_lengths=None, dataset_name='wikitext')}, download_checksums={'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-103-raw-v1/test-00000-of-00001.parquet': {'num_bytes': 732610, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-103-raw-v1/train-00000-of-00002.parquet': {'num_bytes': 156987808, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-103-raw-v1/train-00001-of-00002.parquet': {'num_bytes': 157088770, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-103-raw-v1/validation-00000-of-00001.parquet': {'num_bytes': 657209, 'checksum': None}}, download_size=315466397, post_processing_size=None, dataset_size=548965325, size_in_bytes=864431722)

 DatasetInfo(description='', citation='', homepage='', license='', features={'text': Value(dtype='string', id=None)}, post_processed=None, supervised_keys=None, task_templates=None, builder_name='parquet', dataset_name='wikitext', config_name='wikitext-103-v1', version=0.0.0, splits={'test': SplitInfo(name='test', num_bytes=1295575, num_examples=4358, shard_lengths=None, dataset_name='wikitext'), 'train': SplitInfo(name='train', num_bytes=545141915, num_examples=1801350, shard_lengths=[1652675, 148675], dataset_name='wikitext'), 'validation': SplitInfo(name='validation', num_bytes=1154751, num_examples=3760, shard_lengths=None, dataset_name='wikitext')}, download_checksums={'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-103-v1/test-00000-of-00001.parquet': {'num_bytes': 721735, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-103-v1/train-00000-of-00002.parquet': {'num_bytes': 155788327, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-103-v1/train-00001-of-00002.parquet': {'num_bytes': 155928670, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-103-v1/validation-00000-of-00001.parquet': {'num_bytes': 655106, 'checksum': None}}, download_size=313093838, post_processing_size=None, dataset_size=547592241, size_in_bytes=860686079)

 DatasetInfo(description='', citation='', homepage='', license='', features={'text': Value(dtype='string', id=None)}, post_processed=None, supervised_keys=None, task_templates=None, builder_name='parquet', dataset_name='wikitext', config_name='wikitext-2-raw-v1', version=0.0.0, splits={'test': SplitInfo(name='test', num_bytes=1305088, num_examples=4358, shard_lengths=None, dataset_name='wikitext'), 'train': SplitInfo(name='train', num_bytes=11061717, num_examples=36718, shard_lengths=None, dataset_name='wikitext'), 'validation': SplitInfo(name='validation', num_bytes=1159288, num_examples=3760, shard_lengths=None, dataset_name='wikitext')}, download_checksums={'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-2-raw-v1/test-00000-of-00001.parquet': {'num_bytes': 732610, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-2-raw-v1/train-00000-of-00001.parquet': {'num_bytes': 6357543, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-2-raw-v1/validation-00000-of-00001.parquet': {'num_bytes': 657209, 'checksum': None}}, download_size=7747362, post_processing_size=None, dataset_size=13526093, size_in_bytes=21273455)

 DatasetInfo(description='', citation='', homepage='', license='', features={'text': Value(dtype='string', id=None)}, post_processed=None, supervised_keys=None, task_templates=None, builder_name='parquet', dataset_name='wikitext', config_name='wikitext-2-v1', version=0.0.0, splits={'test': SplitInfo(name='test', num_bytes=1270947, num_examples=4358, shard_lengths=None, dataset_name='wikitext'), 'train': SplitInfo(name='train', num_bytes=10918118, num_examples=36718, shard_lengths=None, dataset_name='wikitext'), 'validation': SplitInfo(name='validation', num_bytes=1134123, num_examples=3760, shard_lengths=None, dataset_name='wikitext')}, download_checksums={'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-2-v1/test-00000-of-00001.parquet': {'num_bytes': 685430, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-2-v1/train-00000-of-00001.parquet': {'num_bytes': 6068114, 'checksum': None}, 'hf://datasets/Salesforce/wikitext@b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-2-v1/validation-00000-of-00001.parquet': {'num_bytes': 617738, 'checksum': None}}, download_size=7371282, post_processing_size=None, dataset_size=13323188, size_in_bytes=20694470)
"""
