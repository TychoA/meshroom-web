from os import path
import subprocess

class Meshroom(object):

    def __init__(self, inputdir, outputdir):
        """
        Constructor.

        ---
        inputdir: Path to input folder where the images of the model should be.
        outputdir: Path where meshroom will place its output.
        """
        self._input = inputdir
        self._output = outputdir

    def run(self, config):
        """
        Run a simulation with a given configuration file.

        raises: Exception
        ---
        config: Path to JSON file that holds the configuration of a meshroom simulation.
        """

        # Check if the given config file exists
        if not path.isfile(config):
            raise Exception(f"Config file {config} does not exist")

        # Check if it's a json file
        if not config.endswith('.json'):
            raise Exception(f"Config file {config} is not a JSON file")

        # Run the meshroom cli
        process = subprocess.run([
            path.join("meshroom", "meshroom_batch"),
            "--inputRecursive", self._input,
            "--output", self._output,
            "--overrides", config,
            "--save", path.join(self._output, "project")
        ])
