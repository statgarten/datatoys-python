import os

import pandas as pd
import pyreadr


class Datatoy:
    """Easily install & load curated Republic of Korea public datasets from https://github.com/statgarten/datatoys"""

    DATATOYS_URL = "https://github.com/statgarten/datatoys"
    README_POSTFIX = "/blob/main/README.md"
    DOWNLOAD_DIR = f"{os.path.join(os.getcwd(), '.datatoys')}"
    DATASET_HEADER_KO = "데이터셋"

    def __init__(self):
        self.__create_download_directory()
        self.manifest = self.get_manifest()

    def __create_download_directory(self):
        os.makedirs(self.DOWNLOAD_DIR, exist_ok=True)
        assert os.path.exists(self.DOWNLOAD_DIR)

    def _dataset_downloaded(self, dataset_nm: str) -> bool:
        return os.path.exists(f"{self.DOWNLOAD_DIR}/{dataset_nm}.rda")

    def _dataset_in_manifest(self, dataset_nm: str) -> bool:
        return dataset_nm in self.get_manifest_dataset_names()

    def get_manifest(self) -> pd.DataFrame:
        url = self.DATATOYS_URL + self.README_POSTFIX
        response = pd.read_html(url)
        assert len(response) == 1 and isinstance(response[0], pd.DataFrame)
        return response.pop()

    def get_manifest_dataset_names(self) -> list:
        return self.manifest.loc[:, self.DATASET_HEADER_KO].tolist()

    def show_manifest(self):
        print(self.get_manifest())

    def install(self, dataset_nm: str) -> bool:
        """Install the dataset to the download directory.

        Args:
                dataset_nm (str): The name of the dataset to be deleted.

        Returns:
                return: return True if successfully installed otherwise false.

        Raises:
                raise ValueError: raise ValueError if the dataset is not in the manifest.
        """

        remote_url = f"{self.DATATOYS_URL}/blob/main/data/{dataset_nm}.rda?raw=true"
        dst_path = f"{self.DOWNLOAD_DIR}/{dataset_nm}.rda"
        if not self._dataset_in_manifest(dataset_nm):
            raise ValueError(
                f"Dataset `{dataset_nm}` is not in the manifest. Check the manifest with `Datatoy().show_manifest()`."
            )
        try:
            pyreadr.download_file(remote_url, dst_path)
        except Exception as e:
            print(f"Exception occured while downloading {remote_url}", e)
            return False
        assert self._dataset_downloaded(dataset_nm)
        return True

    def load(self, dataset_nm: str) -> pd.DataFrame:
        """Load the dataset from the download directory.

        Calls `Datatoy().install()` if the dataset is not downloaded.

        Args:
                dataset_nm (str): The name of the dataset to be deleted.

        Returns:
                return: pandas.DataFrame
        """

        dst_path = f"{self.DOWNLOAD_DIR}/{dataset_nm}.rda"
        if not self._dataset_downloaded(dataset_nm):
            print(f"Dataset `{dataset_nm}` is not installed. Installing it first.")
            self.install(dataset_nm)
        res = pyreadr.read_r(dst_path)
        data = res.get(dataset_nm)
        assert isinstance(data, pd.DataFrame)
        return data

    def clean(self, dataset_nm: str) -> bool:
        """Delete the dataset from the download directory.

        Args:
                dataset_nm (str): The name of the dataset to be deleted.

        Returns:
                return: return True if the dataset is deleted successfully otherwise false.
        """

        dst_path = f"{self.DOWNLOAD_DIR}/{dataset_nm}.rda"
        if self._dataset_downloaded(dataset_nm):
            os.remove(dst_path)
            return True
        return False

    def clean_all(self):
        """Cleanup all datasets within the download directory."""

        for dataset_nm in self.get_manifest_dataset_names():
            self.clean(dataset_nm)


if __name__ == "__main__":
    dt = Datatoy()
    dt.show_manifest()
    dataset_nm = "karaoke"
    df = dt.load("karaoke")
    print(df.head())
    dt.clean(dataset_nm)
