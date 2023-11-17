from datasets import load_dataset
from chatbot import constants
from alutils import alos

data_name = 'daily_dialog'
data_dir = alos.gen_dir(f"{constants.DATA_PATH}{data_name}")
dataset = load_dataset(data_name, cache_dir=data_dir)

for id, sample in enumerate(dataset['train']):
    if id > 10: break
    dialogs = sample['dialog']
    for dialog in dialogs:
        print (dialog)
        # print (dialog['text'])
    print ('------------------------------------------')