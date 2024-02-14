import json
from zipfile import ZipFile


class GarpixZipReader:
    """This class reads data from single zip file, contains Garpix json files with calculation data."""

    def __init__(self, zip_file_name):
        """
        Initializing class instance.
        :param str zip_file_name: path and name of the zip containing the data
        """
        self._zip_file_name = zip_file_name
        self._data = []

    def read_zip(self):
        """
        This method reads data from zip file, contains Garpix data
        :return: copy list of dictionaries with data from zip file
        """
        self._data.clear()
        with ZipFile(self._zip_file_name) as zip_f:
            files = zip_f.namelist()
            for file in files:
                with zip_f.open(file) as json_file:
                    json_data = json.load(json_file)
                    self._data.append(json_data)
        return self._data.copy()

    def get_data(self):
        """
        This method returns list of dictionaries with data from zip
        :return: copy list of dictionaries with data from zip file
        """
        return self._data.copy()
