from scipy.io import loadmat

def main():
    mat_path = 'data/sunrgbd/OFFICIAL_SUNRGBD/SUNRGBDMeta3DBB_v2.mat'

    mat = loadmat(mat_path)

    print(mat.keys())
    # [('sequenceName', 'O'),
    #  ('Rtilt', 'O'),
    #  ('K', 'O'),
    #  ('depthpath', 'O'),
    #  ('rgbpath', 'O'),
    #  ('anno_extrinsics', 'O'),
    #  ('depthname', 'O'),
    #  ('rgbname', 'O'),
    #  ('sensorType', 'O'),
    #  ('valid', 'O'),
    #  ('groundtruth3DBB', 'O')]
    print(mat['SUNRGBDMeta'][0][16]['groundtruth3DBB'].shape)
    print(mat['SUNRGBDMeta'][0][16]['groundtruth3DBB'][:, 0])
    print(mat['SUNRGBDMeta'][0][16]['groundtruth3DBB'][:, 2].dtype)
    # print(len(mat['SUNRGBDMeta']))
    # print(len(mat['SUNRGBDMeta'][0]))
    # print(len(mat['SUNRGBDMeta'][0][0]))
    # print(mat['SUNRGBDMeta'][0][0])
    # print(mat['SUNRGBDMeta'][0][0][4])


if __name__ == '__main__':
    main()
