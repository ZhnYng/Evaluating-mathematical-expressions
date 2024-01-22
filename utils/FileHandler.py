import os
from ADT.File import File
from ADT import SortedList

class FileHandler:
    """
    A class for performing read and write operations on files and folders.

    Attributes:
    - None
    """
    def read(self, filename: str, read_mode: str = 'char'):
        """
        Reads the contents of a file and returns them as a list.

        Parameters:
        - filename (str): The name of the file to read.
        - read_mode (str, optional): Determines the level of reading. 
            'char' returns the file as a list of characters, 
            'line' returns the file as a list of lines. Default is 'char'.

        Returns:
        - List of characters or lines depending on the 'read_mode' parameter.
        """
        if not filename.lower().endswith(('.txt')):
            raise ValueError('File type invalid!')
        if not os.path.isfile(filename):
            raise FileNotFoundError('File does not exist!')

        contents = []
        with open(filename) as f:
            if read_mode == 'char':
                lines = f.readlines()
                for message in lines:
                    contents.extend([*message]) # extend keeps contents one dimensional
            elif read_mode == 'line':
                lines = f.read().splitlines()
                contents.extend(lines)

        if contents:
            return contents
        else:
            raise ValueError('File is empty!')

    def write(self, filename: str, content: str, mode: str='w'):
        """
        Writes content to a file, either overwriting the existing content or appending to it.

        Parameters:
        - filename (str): The name of the file to write to.
        - content (str): The content to be written to the file.
        - mode (str, optional): Specifies the write mode, 'w' for overwriting or 'a' for appending. Default is 'w'.
        """
        if not filename.lower().endswith(('.txt')):
            raise ValueError('File type invalid!')

        with open(filename, mode) as f:
            f.write(content)

    def read_folder(self, folder: str):
        """
        Lists all the files in a folder.

        Parameters:
        - folder (str): The path of the folder to list files from.

        Returns:
        - List of File Objects from the folder.
        """
        if not os.path.isdir(folder):
            raise FileNotFoundError('Folder does not exist!')

        files:list[File] = []
        with os.scandir(f'{folder}/') as dir_files:
            for file in dir_files:
                file = File(file.name)
                files.append(file)
        return files
    
    def get_file_path(self, *paths: str):
        """
        Joins multiple path components into a single file path.

        Parameters:
        - *paths (str): Variable number of path components to be joined.

        Returns:
        - The joined file path as a string.
        """
        return os.path.join(*paths)
    
    def queue_files(self, files):
        sorted_files = SortedList()
        for file in files:
            sorted_files.insert(file)
        return sorted_files.items()
    
    def __str__(self):
        return "FileHandler class for performing read and write operations on files and folders."

    def __repr__(self):
        return "FileHandler()"