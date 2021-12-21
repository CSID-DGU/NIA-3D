### Prepare the DTAAS dataset

1. Put DTAAS dataset to `DTAAS` directory.

2. Create a split of training and validation.
```bash
python data/dtaas/python/create_split.py
```

3. Create labels using the command below.
```bash
python data/dtaas/python/create_labels.py
```

4. Create depth data using the command below.
```bash
python data/dtaas/python/create_points.py
```

5. Create DTAAS data pickle using the command below.
```bash
python tools/create_data.py dtaas --root-path ./data/dtaas --out-dir ./data/dtaas --extra-tag dtaas
```

After pre-prossing, the directory structure will be like below.
```
dtaas
├── README.md
├── python
│   ├── create_labels.py
│   ├── create_points.py
├── DTAAS
│   ├── S_01_0008_1_I_40
│   │   ├── bbox
│   │   │   ├── Lighting_01.pts
│   │   │   ├── Lighting_02.pts
│   │   │   ├── ...
│   │   ├── S_01_0008_1_I_40.pts
│   ├── S_01_0008_1_I_41
│   │   ├── bbox
│   │   │   ├── Storage closet_01.pts
│   │   │   ├── Storage closet_02.pts
│   │   ├── S_01_0008_1_I_41.pts
│   ├── S_01_0008_1_I_42
│   │   ├── bbox
│   │   │   ├── Storage closet_01.pts
│   │   ├── S_01_0008_1_I_42.pts
│   ├── ...
├── dtaas_trainval
│   ├── depth
│   ├── label
│   ├── train_data_idx.txt
│   ├── val_data_idx.txt
├── points
│   ├── 000001.bin
│   ├── 000002.bin
│   ├── 000003.bin
│   ├── ...
├── dtaas_infos_train.pkl
├── dtaas_infos_val.pkl
```

### Train a model with the DTAAS dataset
```bash
bash tools/dist_train.sh configs/fcaf3d/fcaf3d_dtaas-3d-9class.py 2
```
