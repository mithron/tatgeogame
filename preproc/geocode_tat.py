import geocoder
import csv, json
from tqdm import tqdm

def main():
    data = []
    with open('ttt.csv') as csvfile:
        ttt = csv.DictReader(csvfile)
        for row in ttt:
            data.append(row)
    print(len(data))
    
    for item in tqdm(data):
        if not item['address']:
            data.remove(item)
    
    print(len(data))
            
    for item in tqdm(data):
        geo = geocoder.yandex(item['address'])
        if geo.ok:
            
            print(geo.lat)
            item['lat'] = geo.lat
            item['lng'] = geo.lng
        else:
            print("addr %s not ok" % str(item['address']))
            data.remove(item)
    
    for item in tqdm(data):
        
        if "lat" not in item.keys():
            geo = geocoder.yandex(item['address'])
            if geo.ok:
                print(geo.lat)
                item['lat'] = geo.lat
                item['lng'] = geo.lng
            else:
                print("addr %s not ok" % str(item['address']))
                data.remove(item)
    
    
        
    with open('ttt2.json', 'w') as jsonfile:
        json.dump(data, jsonfile)