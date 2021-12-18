from scipy.io import loadmat

def main():
    mat_path = 'data/sunrgbd/OFFICIAL_SUNRGBD/SUNRGBDMeta2DBB_v2.mat'

    mat = loadmat(mat_path)

    print(mat.keys())
    # [('sequenceName', 'O'),
    #  ('groundtruth2DBB', 'O'),
    #  ('depthpath', 'O'),
    #  ('rgbpath', 'O'),
    #  ('depthname', 'O'),
    #  ('rgbname', 'O'),
    #  ('sensorType', 'O')]
    print(mat['SUNRGBDMeta2DBB'][0].dtype)
    # print(len(mat['SUNRGBDMeta']))
    # print(len(mat['SUNRGBDMeta'][0]))
    # print(len(mat['SUNRGBDMeta'][0][0]))
    # print(mat['SUNRGBDMeta'][0][0])
    # print(mat['SUNRGBDMeta'][0][0][4])


if __name__ == '__main__':
    main()
