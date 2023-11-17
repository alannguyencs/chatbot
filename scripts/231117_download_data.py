from datasets import load_dataset
from chatbot import constants
from alutils import alos


data_dir = alos.gen_dir(f"{constants.DATA_PATH}conv_ai_2")
dataset = load_dataset('conv_ai_2', cache_dir=data_dir)

for id, sample in enumerate(dataset['train']):
    if id > 10: break
    dialogs = sample['dialog']
    for dialog in dialogs:
        print (dialog)
        # print (dialog['text'])
    print ('------------------------------------------')