import pickle

split = 'val'
data_path = f'class_attr_data_10/{split}.pkl'

with open(data_path, 'rb') as f:
    data = pickle.load(f)
print('number of data:', len(data))
print(data[-1])

# remove the path prefix
prefix = '/juice/scr/scr102/scr/thaonguyen/CUB_supervision/datasets/'

for d in data:
    d['img_path'] = d['img_path'].replace(prefix, '')
    
print(data[-1]['img_path']) # CUB_200_2011/images/063.Ivory_Gull/Ivory_Gull_0005_49021.jpg

save_path = f'CUB_processed/{split}.pkl'
with open(save_path, 'wb') as f:
    pickle.dump(data, f)
print(f'saved to {save_path}')