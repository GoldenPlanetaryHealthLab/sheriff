# Sheriff


THe `sheriff` is a simple package that provides a set of tools for
enforcing the rules of the frontier. It’s most important and basic
functionality is to ensure that the user is a part of the frontier. It
does this by running the following simple checks:

1.  Does the user have an environment variable called `THE_FRONTIER` and
    does it point to a valid `frontier.yml` file?

2.  If not, is the current working directory a part of the frontier?
    This is done by checking the path for a `frontier.yml` file.

Further, more stringent checks can be implemented in future, but for
now, this is all that’s needed.

``` python
import os
from rich.console import Console
from pathlib import Path

console = Console()

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

        console.print("🤠 There's a new sheriff in town! Let's take a look at your papers...")

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

            console.print(f"🪪 Found frontier file at: {self.frontier_path}")
            console.print("🏞️ Welcome to the frontier, citizen!")
            return True
        
        # Check current working directory
        cwd = os.getcwd()

        # check that "frontier" is in the path
        if self.frontier_dirname in cwd:
            
            frontier_file_path = Path(cwd.split(self.frontier_dirname)[0]) / self.frontier_dirname / self.frontier_file
            
            if os.path.isfile(frontier_file_path):
                self.frontier_path = frontier_file_path
                console.print(f"🪪 Found frontier file at: {self.frontier_path}")
                console.print("🏞️ Welcome to the frontier, citizen!")
                return True
        
        console.print("❌ No frontier file found. Please set the THE_FRONTIER environment variable or navigate to a directory within the frontier to validate your citizenship.")
        return False
```

With this simple class definition, we can now create a script that
checks citizenship and prints the frontier path if found.

``` python
import typer

app = typer.Typer(
    name="sheriff",
    help="Validate your identity and lawful presence on The Frontier.",
)

@app.command()
def inspect():
    """
    Hey there, partner! The sheriff is here to check your papers and make sure you're a citizen of The Frontier. Let's see if you have what it takes to be a part of this wild and wonderful land.
    """
    sheriff = Sheriff()
    sheriff.check_citizen()
```

``` python
if __name__ == "__main__":
    app()
```

Cool!

# Script file

The code for this document can be found here:

- [../src/sheriff/sheriff.py](../src/sheriff/sheriff.py)
