import os
from random import sample

import pandas as pd
import pytest

from datatoys import Datatoy

THRESHOLD_NUM_DATASETS = 80


# This fixture returns a Datatoy instance
@pytest.fixture(scope="module")
def datatoy_instance():
    return Datatoy()


# This fixture generates a static list of sample dataset names
@pytest.fixture(scope="module")
def sample_dataset_name(datatoy_instance):
    _sample_dataset_name = sample(datatoy_instance.get_manifest_dataset_names(), 1)[0]
    print("\nSelected dataset is: ", _sample_dataset_name)
    return _sample_dataset_name


def test_create_data_directory():
    dirname = ".datatoys"
    cwd = os.getcwd()
    download_dir = os.path.join(cwd, dirname)
    os.makedirs(download_dir, exist_ok=True)
    assert os.path.exists(download_dir)


def test_get_manifest(datatoy_instance):
    assert isinstance(datatoy_instance.get_manifest(), pd.DataFrame)


def test_get_manifest_dataset_names(datatoy_instance):
    assert isinstance(datatoy_instance.get_manifest_dataset_names(), list)
    assert len(datatoy_instance.get_manifest_dataset_names()) >= THRESHOLD_NUM_DATASETS


# Use the static list from the fixture for parameterization
def test_install(datatoy_instance, sample_dataset_name):
    assert datatoy_instance.install(sample_dataset_name)


def test_load(datatoy_instance, sample_dataset_name):
    df = datatoy_instance.load(sample_dataset_name)
    print(df)
    assert isinstance(df, pd.DataFrame)
