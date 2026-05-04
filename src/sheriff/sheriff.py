from pathlib import Path
import os

class Sheriff:
    """
A simple class that checks for frontier citizenship by looking for a frontier.yml file in the environment variable or the current working directory.
    """
    def __init__(self, frontier_dirname="frontier", frontier_file="frontier.yml"):
        """
        Initializes the Sheriff Class.
        Args:
            frontier_dirname (str): The name of the directory that contains the frontier.yml file. Default is "frontier".
            frontier_file (str): The name of the frontier file. Default is "frontier.yml".
        """
        self.frontier_dirname = frontier_dirname
        self.frontier_file = frontier_file
        self.frontier_path = None

        print("There's a new sheriff in town!")

    def check_citizen(self):
        """
        Checks for frontier citizenship by looking for a frontier.yml file in the environment variable or the current working directory.
        Returns:
            bool: True if the user is a citizen of the frontier, False otherwise.
        """
        # Check for environment variable
        env_path = os.getenv('THE_FRONTIER')
        if env_path and os.path.isfile(env_path):
            self.frontier_path = env_path

            print(f"Found frontier file at: {self.frontier_path}")
            print("Welcome to the frontier, citizen!")
            return True
        
        # Check current working directory
        cwd = os.getcwd()

        # check that "frontier" is in the path
        if self.frontier_dirname in cwd:
            
            frontier_file_path = Path(cwd.split(self.frontier_dirname)[0]) / self.frontier_dirname / self.frontier_file
            
            if os.path.isfile(frontier_file_path):
                self.frontier_path = frontier_file_path
                print(f"Found frontier file at: {self.frontier_path}")
                print("Welcome to the frontier, citizen!")
                return True
        
        print("No frontier file found. Please set the THE_FRONTIER environment variable or navigate to a directory within the frontier to validate your citizenship.")
        return False


if __name__ == "__main__":
    sheriff = Sheriff()
    sheriff.check_citizen()
