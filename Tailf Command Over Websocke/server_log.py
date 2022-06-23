import os


class ReadFile:
    def __init__(self):
        self.__file_name = f"log.txt"
        if not os.path.isfile(self.__file_name):
            raise FileNotFoundError(f"File Not Found")

    @property
    def file_name(self):
        return self.__file_name

    def read_file(self, olp):
        with open(self.__file_name, 'rb') as fp:
            try:
                fp.seek(-100, 2)
            except OSError:
                return None, olp
            lp = fp.tell()
            if lp == olp:
                return None, lp
            file_data = fp.readline(-1)
            if file_data:
                return file_data, lp
