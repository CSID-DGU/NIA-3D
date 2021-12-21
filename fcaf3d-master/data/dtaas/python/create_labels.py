import os
import numpy as np
import open3d as o3d

def main(dir_root):
    label2cat = {
        'Lighting': 'lighting',
        'TV': 'tv',
        'Storage closet': 'storage_closet',
        'Chair': 'chair',
        'Sofa': 'sofa',
        'Computer': 'computer',
        'Table': 'table',
        'Bed': 'bed',
        'Desk': 'desk'
    }

    label_path = "data/dtaas/dtaas_trainval/label"
    if not os.path.exists(label_path):
        os.makedirs(label_path)

    dir_names = os.listdir(dir_root)
    dir_names.sort()
    for idx, dir_name in enumerate(dir_names):
        bbox_dir = f"{dir_root}/{dir_name}/bbox"

        bbox_dir_names = os.listdir(bbox_dir)
        bbox_dir_names.sort()

        labels = []
        for bbox_dir_name in bbox_dir_names:
            label = []
            bbox_name = f"{dir_root}/{dir_name}/bbox/{bbox_dir_name}"
            with open(bbox_name, "rt", encoding = 'utf-8') as fr:
                points = []
                fr.readline() # Skip a header.
                while True:
                    line = fr.readline()
                    if not line:
                        break;
                    points.append(list(map(float, line.strip().split(" "))))
                npPoints = np.array(points)
                cx, cy, cz = np.round((npPoints[0] + npPoints[1]) / 2, 6)
                w, l, h = np.round(npPoints[1] - npPoints[0], 6)
                cat_name = label2cat[bbox_dir_name.split("_")[0]]
                label.append(cat_name)
                label.extend([cx, cy, cz])
                label.extend([w, l, h])
                label.extend([0.0, 0.0]) # Orientation
            
            labels.append(label)
   
        print(labels) 
        with open(f"{label_path}/{idx+1:06d}.txt", "w") as fw:
             for l in labels:
                fw.write("%s\n" % " ".join(map(str, l)))

if __name__ == '__main__':
    dir_root = 'data/dtaas/DTAAS'
    main(
        dir_root=dir_root
    )
