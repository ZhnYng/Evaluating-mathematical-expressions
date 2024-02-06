# -----------------------------------------------------
# ST1507 DSAA
# CA2
#
# A class for performing read and write operations on files and folders.
#
# -----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : FileHandler.py
#
# -----------------------------------------------------
# To run: python main.py
# -----------------------------------------------------
import os
from ADT.File import File
from ADT import SortedList


class FileHandler:
    """
    A class for performing read and write operations on files and folders.
    """

    def read(self, filename: str, read_mode: str = "char"):
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
        if not filename.lower().endswith((".txt")):  # Check if the file type is valid
            raise ValueError("File type invalid!")
        if not os.path.isfile(filename):  # Check if the file exists
            raise FileNotFoundError("File does not exist!")

        contents = []  # Initialize list to store file contents
        with open(filename) as f:
            if read_mode == "char":  # Read file as characters
                lines = f.readlines()
                for message in lines:
                    contents.extend(
                        [*message]
                    )  # Extend the list with individual characters
            elif read_mode == "line":  # Read file as lines
                lines = f.read().splitlines()
                contents.extend(lines)  # Extend the list with lines

        if contents:
            return contents  # Return the list of file contents
        else:
            raise ValueError("File is empty!")  # Raise an error if the file is empty

    def write(self, filename: str, content: str):
        """
        Writes content to a file, either overwriting the existing content or appending to it.

        Parameters:
        - filename (str): The name of the file to write to.
        - content (str): The content to be written to the file.
        - mode (str, optional): Specifies the write mode, 'w' for overwriting or 'a' for appending. Default is 'w'.
        """
        if not filename.lower().endswith((".txt")):  # Check if the file type is valid
            raise ValueError("File type invalid!")
        elif os.path.isfile(filename):  # Check if the file already exists
            handle_file_exists = ""  # Initialize variable to handle file existence
            while handle_file_exists not in {
                "O",
                "A",
                "F",
            }:  # Prompt user for action until a valid choice is made
                handle_file_exists = input(
                    f'\n{"File already exists!"}\nWould you like to overwrite(O), append(A), or write into a different file(F)?\n'
                ).upper()
            if handle_file_exists == "O":  # Overwrite existing file
                with open(filename, "w") as f:
                    f.write(content)
            elif handle_file_exists == "A":  # Append to existing file
                with open(filename, "a") as f:
                    content = (
                        "=" * 60 + "\n" + content
                    )  # Add separator line before appending
                    f.write(content)
            elif handle_file_exists == "F":  # Write to a different file
                new_file = input("New file name: ")
                self.write(
                    new_file, content
                )  # Call write method recursively with a new file name
        else:  # Write to a new file
            with open(filename, "w") as f:
                f.write(content)

    def read_folder(self, folder: str):
        """
        Lists all the files in a folder.

        Parameters:
        - folder (str): The path of the folder to list files from.

        Returns:
        - List of File Objects from the folder.
        """
        if not os.path.isdir(folder):  # Check if the folder exists
            raise FileNotFoundError("Folder does not exist!")

        files: list[File] = []  # Initialize an empty list to store File objects
        with os.scandir(
            f"{folder}/"
        ) as dir_files:  # Iterate over files in the directory
            for file in dir_files:
                file = File(
                    file.name
                )  # Create a File object for each file in the directory
                files.append(file)  # Add the File object to the list
        return files  # Return the list of File objects

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
        """
        Sorts a list of files alphabetically and returns them.

        Parameters:
        - files (list): List of File objects to be sorted.

        Returns:
        - List of sorted File objects.
        """
        sorted_files = SortedList()  # Create a SortedList instance
        for file in files:  # Iterate over each file in the input list
            sorted_files.insert(file)  # Insert the file into the sorted list
        return sorted_files.items()  # Return the sorted list of files

    def __str__(self):
        """
        Returns a string representation of the FileHandler class.
        """
        return "FileHandler class for performing read and write operations on files and folders."

    def __repr__(self):
        """
        Returns a string representation of the FileHandler object.
        """
        return "FileHandler()"

    """
    OOP Principles Applied:

    Encapsulation:
    - The FileHandler class encapsulates file read and write operations, providing a unified interface for interacting with files and folders.
    - Internal data and behavior, such as file paths and file contents, are encapsulated within the class, promoting data integrity and reducing complexity.
    - External classes interact with FileHandler through defined methods, maintaining encapsulation boundaries.

    Abstraction:
    - FileHandler abstracts away the complexities of file manipulation by providing high-level methods like read, write, read_folder, get_file_path, and queue_files.
    - Users interact with FileHandler without needing to know the internal implementation details of these methods, promoting a simpler and more intuitive interface.

    Polymorphism:
    - The FileHandler class can handle different types of file operations, such as reading files, writing files, listing files in a folder, and joining file paths, seamlessly.
    - Methods like read, write, read_folder, get_file_path, and queue_files are flexible and can accommodate various file-related tasks without changes to their interface.

    Modularity:
    - Each method in the FileHandler class serves a specific purpose, promoting modularity and code reusability.
    - For example, the read method is responsible for reading the contents of a file, while the read_folder method is responsible for listing files in a folder.
    - This modular design makes the FileHandler class easier to understand, maintain, and extend.
    """
