import os
import numpy as np
from scipy.io import loadmat


def main():
    base_path = 'data/sunrgbd/sunrgbd_trainval/depth'

    mat_names = os.listdir(base_path)
    mat_names.sort()

    nums = []
    idx = 0
    for mat_name in mat_names:
        print(mat_name)
        mat = loadmat(f"{base_path}/{mat_name}")['instance']
        nums.append(mat.shape[0])
        print(mat)
        if idx == 50:
            break
        idx +=1

    print(np.mean(nums))


if __name__ == '__main__':
    main()
