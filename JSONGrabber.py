"""
Grabs info.json from pano directories
"""
import os, sys, json

def getIDs(dir):
    ids = []
    directory = os.fsencode(dir)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".png") and filename[:4] == "pano":
            ids.append(filename.split("-")[1])
    print(ids)
    return ids


def grabJSON(ids, dir):
    result = []
    for id in ids:
        with open(dir+"/pano-"+id+'/info.json') as json_file:
            print("Reading:"+dir+"/pano-"+id+'/info.json')
            data = json.load(json_file)
            d = {}
            d["id"] = id
            d["filename"] = "pano-" + id + "-mx.png"
            d["calibration"] = 0.0
            d["neighborhood"] = "" #TODO: make neighborhood auto obtainable
            d["coord"] = {"lat": float(data["latitude"]), "lng": float(data["longitude"])}
            result.append(d)
            print("Finished reading...")
    
    with open('./allPanoInfo.json', 'w') as outfile:
        json.dump(result, outfile)


if __name__ == "__main__":
    #in_dir = sys.argv[1]
    #source_dir = sys.argv[2]

    in_dir = "/Users/Billzhang/Desktop/smartIR/finished"
    source_dir = "/Volumes/NO NAME"

    pano_ids = getIDs(in_dir)
    grabJSON(pano_ids, source_dir)