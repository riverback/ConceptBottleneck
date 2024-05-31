import pickle, os

split = 'test'
data_path = f'class_attr_data_10/{split}.pkl'

with open(data_path, 'rb') as f:
    data = pickle.load(f)
print('number of data:', len(data))
print(data[-1])

# remove the path prefix
prefix = '/juice/scr/scr102/scr/thaonguyen/CUB_supervision/datasets/'
new_prefix = '/mnt/nasv3/hhz/Datasets/CUB200/'
for d in data:
    d['img_path'] = d['img_path'].replace(prefix, new_prefix)
    
print(data[-1]['img_path']) # CUB_200_2011/images/063.Ivory_Gull/Ivory_Gull_0005_49021.jpg

save_path = f'CUB_processed/class_attr_data_10/{split}.pkl'
with open(save_path, 'wb') as f:
    pickle.dump(data, f)
print(f'saved to {save_path}')

# check if the image exist
for d in data:
    if not os.path.exists(d['img_path']):
        print(d['img_path'])
        break