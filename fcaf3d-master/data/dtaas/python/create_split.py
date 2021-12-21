import os
import numpy as np

def main():
    num_total_data = 11
    num_train_data = 8
    base_path = "data/dtaas/dtaas_trainval"
    train_idx_file_name = "train_data_idx.txt"
    val_idx_file_name = "val_data_idx.txt"

    if not os.path.exists(base_path):
        os.makedirs(base_path)

    train_indices = list(np.arange(1, num_train_data + 1))
    val_indices = list(np.arange(num_train_data + 1, num_total_data + 1))

    # Create indices for training.
    with open(os.path.join(base_path, train_idx_file_name), 'w') as f:
        for i in train_indices:
            f.write("%s\n" % i)

    # Create indices for validation and test.
    with open(os.path.join(base_path, val_idx_file_name), 'w') as f:
        for i in val_indices:
            f.write("%s\n" % i)

if __name__ == '__main__':
    main()
