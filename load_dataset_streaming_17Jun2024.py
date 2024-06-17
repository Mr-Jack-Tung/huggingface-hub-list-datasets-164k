"""
# https://huggingface.co/docs/datasets/v1.10.1/dataset_streaming.html
File: load_dataset_streaming_17Jun2024.py
- From: Mr.Jack
- Date: 17 Jun 2024
"""

from datasets import load_dataset

dataset_path = 'Salesforce/wikitext'
subset = 'wikitext-2-v1'

dataset = load_dataset(path=dataset_path, name=subset, split="train", streaming=True)

# print("\n",dataset.features)
# {'text': Value(dtype='string', id=None)}

# print(next(iter(dataset)))

# get_5_items = dataset.take(5)
# print(list(get_5_items))

"""
[{'text': ''}, {'text': ' = Valkyria Chronicles III = \n'}, {'text': ''}, {'text': ' Senjō no Valkyria 3 : <unk> Chronicles ( Japanese : 戦場のヴァルキュリア3 , lit . Valkyria of the Battlefield 3 ) , commonly referred to as Valkyria Chronicles III outside Japan , is a tactical role @-@ playing video game developed by Sega and Media.Vision for the PlayStation Portable . Released in January 2011 in Japan , it is the third game in the Valkyria series . <unk> the same fusion of tactical and real @-@ time gameplay as its predecessors , the story runs parallel to the first game and follows the " Nameless " , a penal military unit serving the nation of Gallia during the Second Europan War who perform secret black operations and are pitted against the Imperial unit " <unk> Raven " . \n'}, {'text': " The game began development in 2010 , carrying over a large portion of the work done on Valkyria Chronicles II . While it retained the standard features of the series , it also underwent multiple adjustments , such as making the game more <unk> for series newcomers . Character designer <unk> Honjou and composer Hitoshi Sakimoto both returned from previous entries , along with Valkyria Chronicles II director Takeshi Ozawa . A large team of writers handled the script . The game 's opening theme was sung by May 'n . \n"}]
"""

# shuffled_dataset = dataset.shuffle(seed=42, buffer_size=100)

i = 0
for item in iter(dataset):
    print("\n",item)
    i+=1
    if i >= 5:
        break

"""
 {'text': ''}

 {'text': ' = Valkyria Chronicles III = \n'}

 {'text': ''}

 {'text': ' Senjō no Valkyria 3 : <unk> Chronicles ( Japanese : 戦場のヴァルキュリア3 , lit . Valkyria of the Battlefield 3 ) , commonly referred to as Valkyria Chronicles III outside Japan , is a tactical role @-@ playing video game developed by Sega and Media.Vision for the PlayStation Portable . Released in January 2011 in Japan , it is the third game in the Valkyria series . <unk> the same fusion of tactical and real @-@ time gameplay as its predecessors , the story runs parallel to the first game and follows the " Nameless " , a penal military unit serving the nation of Gallia during the Second Europan War who perform secret black operations and are pitted against the Imperial unit " <unk> Raven " . \n'}

 {'text': " The game began development in 2010 , carrying over a large portion of the work done on Valkyria Chronicles II . While it retained the standard features of the series , it also underwent multiple adjustments , such as making the game more <unk> for series newcomers . Character designer <unk> Honjou and composer Hitoshi Sakimoto both returned from previous entries , along with Valkyria Chronicles II director Takeshi Ozawa . A large team of writers handled the script . The game 's opening theme was sung by May 'n . \n"}
 """
