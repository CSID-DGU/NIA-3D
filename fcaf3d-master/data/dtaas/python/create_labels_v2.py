import os
import numpy as np
import open3d as o3d

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

def search_bbox_dir(bbox_dir, laber_path):
    bbox_dir_names = os.listdir(bbox_dir)
    bbox_dir_names.sort()

    labels = []
    for bbox_dir_name in bbox_dir_names:
        key = bbox_dir_name.split("_")[0].split(".")[0]
        if key not in label2cat:
            print(key," skip\n")
            continue

        label = []
        bbox_name = f"{bbox_dir}/{bbox_dir_name}"
        print(bbox_dir_name)
        with open(bbox_name, "rt", encoding = 'utf-8') as fr:
            points = []
             # fr.readline() # Skip a header.
            while True:
                line = fr.readline()
                if not line:
                    break
                if '/' not in line:
                    print(line)
                    points.append(list(map(float, line.strip().split(" "))))
                    print("points: ", points)
            npPoints = np.array(points)
            print("npPoints: ",npPoints, "\nnpPoints[0]: ", npPoints[0], "\nnpPoints[1]: ", npPoints[1])
            cx, cy, cz = np.round((npPoints[0] + npPoints[1]) / 2, 6)
            print(cx, " ", cy, " ", cz, "\n")
            w, l, h = np.round(npPoints[1] - npPoints[0], 6)

            cat_name = label2cat[key]
            label.append(cat_name)
            label.extend([cx, cy, cz])
            label.extend([w, l, h])
            label.extend([0.0, 0.0]) # Orientation

        labels.append(label)

    return labels

def main(dir_root):
    print(dir_root)

    label_path = "data/dtaas/dtaas_trainval/label"
    if not os.path.exists(label_path):
        os.makedirs(label_path)

    dir_names = os.listdir(dir_root)
    dir_names.sort()
    for idx, dir_name in enumerate(dir_names):
        bbox_dir = f"{dir_root}/{dir_name}/bbox" # 아래 if에서 참일 때 bbox 위치
        labels = []

        if os.path.isdir(bbox_dir):
            print(bbox_dir)
            labels = search_bbox_dir(bbox_dir, label_path)

            print(labels)
            with open(f"{label_path}/{idx+1:06d}.txt", "w") as fw:
                for l in labels:
                    fw.write("%s\n" % " ".join(map(str, l)))
        else:
            dir2_names = os.listdir(f"{dir_root}/{dir_name}")
            dir2_names.sort()
            for idx2, dir2_name in enumerate(dir2_names):
                bbox_dir = f"{dir_root}/{dir_name}/{dir2_name}/bbox" # else에서 사용하는 bbox 위치
                print(bbox_dir)
                labels = search_bbox_dir(bbox_dir, label_path)

                print(labels)
                with open(f"{label_path}/{idx+1:06d}.txt", "w") as fw:
                    for l in labels:
                        fw.write("%s\n" % " ".join(map(str, l)))

if __name__ == '__main__':
    dir_root = 'data/dtaas/DTAAS'
    main(dir_root=dir_root)
