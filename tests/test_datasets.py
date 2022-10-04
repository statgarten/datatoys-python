import os
from random import sample

import pandas as pd
from tqdm import tqdm

from datatoys import Datatoy


def test_create_data_directory():
    dirname = ".datatoys"
    cwd = os.getcwd()
    download_dir = os.path.join(cwd, dirname)
    os.makedirs(download_dir, exist_ok=True)
    assert os.path.exists(download_dir)


class TestDatatoy:

    dt = Datatoy()
    sample_dataset_names = sample(dt.get_manifest_dataset_names(), 3)

    def test_get_manifest(self):
        assert isinstance(self.dt.get_manifest(), pd.DataFrame)

    def test_get_manifest_dataset_names(self):
        assert isinstance(self.dt.get_manifest_dataset_names(), list)
        assert (
            len(self.dt.get_manifest_dataset_names()) >= 37
        )  # 2022. 10. 4. 37 datasets

    def test_install(self):
        for dataset_nm in tqdm(self.sample_dataset_names):
            tqdm.write(f"Installing {dataset_nm}")
            assert self.dt.install(dataset_nm)

    def test_load(self):
        for dataset_nm in tqdm(self.sample_dataset_names):
            tqdm.write(f"Loading {dataset_nm}")
            assert isinstance(self.dt.load(dataset_nm), pd.DataFrame)

    def test_clean(self):
        for dataset_nm in tqdm(self.sample_dataset_names):
            tqdm.write(f"Cleaning {dataset_nm}")
            assert self.dt.clean(dataset_nm)
