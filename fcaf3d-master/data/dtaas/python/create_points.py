import os
import numpy as np
import open3d as o3d
from scipy.io import savemat 

def main(dir_root):
    depth_path = "data/dtaas/dtaas_trainval/depth"
    if not os.path.exists(depth_path):
        os.makedirs(depth_path)

    dir_names = os.listdir(dir_root)
    dir_names.sort()
    for idx, dir_name in enumerate(dir_names):
        pts_name = f"{dir_root}/{dir_name}/{dir_name}.pts"

        with open(pts_name, "rt", encoding = 'utf-8') as fr:
            points = []
            fr.readline() # Skip a header.
            while True:
                line = fr.readline()
                if not line:
                    break;
                points.append(line.strip().split(" "))
            npPoints = np.array(points)
            print(npPoints.shape)
            floatPoint = npPoints[:, 0:3].astype(float)
            intPoint = npPoints[:, 3:6].astype(int)
            binPoint = np.concatenate((floatPoint, intPoint), axis=1)

            savemat(f"{depth_path}/{idx+1:06d}.mat", {'instance': binPoint})

if __name__ == '__main__':
    dir_root = 'data/dtaas/DTAAS'
    main(
        dir_root=dir_root
    )
