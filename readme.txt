Documentation for Qubit Simulation:

WARNING: When running the .udaproj file, the files data.csv and out.txt are generated. These are one time use only.
Please make sure to delete them before re-running the test sequence so that errors and discrepancies are not caused.

Here are the functions of the various files in this folder:

ScopeData:
Contains UDA as a .udaproj format.

ScopeData.udaproj:
Is the UDA project and contains tests which: 
- Remotely connects to the oscilloscope via a VISA address so it may be able to get information
- Contains the following test sequence:
	1. Gather waveform from the oscilloscope and store it as a .csv file named 'data.csv' containing voltage values over a constant timestep.
This is done by calling the :WAVeform:DATA? SCPI command and storing the returned value from the oscilloscope.
Yet to make sure file paths are appropriately modified for when an installer will created to run on other systems.
	2. Launch the data_process.py python file which then processes data.csv and stores it in out.txt. 
The out.txt file generation then triggers the UDA test sequence to then stop and pass with a 1 value in its report.

data_process.py:
Reads the data.csv file generated by the UDA test sequence to then store waveform as a single dimensional array.
Open file to learn more.

Generated files:
1. data.csv: Stores temporary waveform in a .csv file
2. out.txt: Is outputted by data_process and contains the waveform array to trigger the end of the test sequence.