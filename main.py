'''
first do naive test on two datasets and get number
correct over maybe 20 questions each

then run the mcts version and see how it is
finally compare the results
'''

from data import dataloader

dl = dataloader()

dl.load_data('gsm8k')