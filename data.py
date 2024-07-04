from datasets import load_dataset

class dataloader():
    def __init__(self):
        self.valid_names = [
            'gsm8k',
            'gsm-hard',
        ]

        self.paths = {
            'gsm-hard': 'reasoning-machines/gsm-hard',
            'gsm8k': 'openai/gsm8k'
        }

    def get_datasets(self):
        return self.valid_names

    def load_data(self, name):
        if name not in self.valid_names:
            raise Exception("Invalid Dataset Name")
        
        if name == 'gsm8k':
            dataset = load_dataset(self.paths[name], 'main')
        else:
            dataset = load_dataset(self.paths[name])

        return dataset['train']

