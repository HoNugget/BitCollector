## File Name: bitCollector_main.py
##
## Author(s): Daniel "Albinohat" Mercado
##
## Purpose: This script will act as the framework supporting the other modules
##          written to collect different types of information as well as perform 
##          module-independent tasks.
##
## TODO - Create style guide. (Maybe)
##		- Add CLA support. (What CLA will be available?)
##      - Add multi-thread support? (Will require an "entry point" in each module. Use main())

## Standard imports (Static)
import logging, platform, re, sys

## Add the additional search path for BitCollector modules.
sys.path.append("../Modules")

## Third-party imports (Static)

## Global Variable Declarations - CONSTANTS - DO NOT CHANGE @ RUNTIME
## Configure logging formats for the log file and STDOUT.
_log_file_format = logging.Formatter('%(asctime)s,%(module)s.%(name)s.%(funcName)s,%(levelname)s,%(message)s', '%Y-%m-%dT%H:%M:%S')		
_log_console_format	= logging.Formatter('%(asctime)s - %(module)s.%(name)s.%(funcName)s - [%(levelname)s] - %(message)s', '%Y-%m-%d %H:%M:%S')		

## Create the root logging object and get the name of the current module.
_root_logger = logging.getLogger("")
_root_logger.setLevel(logging.DEBUG)

## Create the log file logging stream and configure it.
_log_file_handler = logging.FileHandler("example.csv", "w")
_log_file_handler.setFormatter(_log_file_format)
_root_logger.addHandler(_log_file_handler)

## Create the console logging stream and configure it.
_log_console_handler = logging.StreamHandler(sys.stdout)
_log_console_handler.setFormatter(_log_console_format)
_root_logger.addHandler(_log_console_handler)

## Class Declarations

## Class Name: Platform
##
## Purpose: Hold information about the target machine.
class Platform():
	## Method Name: __init__
	##
	## Purpose: Initialize the platform-independent attributes as well as the correct platform-dependent object.
	##
	## Parameters
	## 1. tuple - A 6 part-tuple containing platform-independent information about the target machine.
	##    Index 0  - The type of OS running on the target machine. (Windows, Linux, etc) 
	##    Index 1  - The hostname of the target machine.
	##    Index 2  - The release # of the OS running on the target machine. (2.2.0, NT, 8, etc)
	##    Index 3  - The version of the OS running on the target machine.
	##    Index 4  - The machine CPU architecture (i386, AMD64, etc)
	##    Index 5  - Information about the processor in the target machine as a 3-part tuple.
	def __init__(self, tuple):
		self.logger = logging.getLogger(self.__class__.__name__)	
		self.logger.debug("BitCollector.Platform.__init__():")
	
		## Replace unknown information ('') with "Unknown"
		for each in tuple:
			if (each == ""):
				each = "Unknown"

		## Initialize the platform-independent attributes.
		self.system    = tuple[0]
		self.node      = tuple[1]
		self.release   = tuple[2]
		self.version   = tuple[3]
		self.machine   = tuple[4]
		self.processor = tuple[5]

		## Initialize the platform OS-dependent attribute objects.
		## Mac OS
		if (re.search(r'mac', self.system.lower())):
			self.mac_platform = MacPlatform(platform.mac_ver(release='', versioninfo=('', '', ''), machine=''))		
		## Linux/Unix
		elif (re.search(r'nix', self.system.lower())):
			self.nix_platform = NixPlatform(platform.linux_distribution(distname='', version='', id='', supported_dists=('SuSE', 'debian', 'redhat', 'mandrake'), full_distribution_name=1))
		## Windows
		elif (re.search(r'win', self.system.lower())):
			self.win_platform = WinPlatform(platform.win32_ver(release='', version='', csd='', ptype=''))
		else:
			self.logger.warning("Unknown system type.")

## Class Name: MacPlatform
##
## Purpose: Hold Mac OS-dependent information about the target machine.
class MacPlatform():
	## Method Name: __init__
	##
	## Purpose: Initialize the Mac OS-dependent attributes.
	##
	## Parameters
	## 1. tuple - A 4 part-tuple containing platform-independent information about the target machine.
	##    Index 0  - The release # of the Mac OS running on the target machine. (2.2.0, NT, 8, etc)
	##    Index 1  - Information about the running Mac OS version as a tuple.
	##        Index[1][0] - The version of the Mac OS running on the target machine.
	##        Index[1][1] - The dev stage of the Mac OS version running on the target machine.
	##        Index[1][2] - Whether or not the Mac OS version running on the target machine is a non-release version.
	##    Index 2  - The parenthesized portion of the version. (usually a codename)
	def __init__(self, tuple):
		self.logger = logging.getLogger(self.__class__.__name__)
		self.logger.debug("BitCollector.MacPlatform.__init__():")

		## Replace unknown information ('') with "Unknown"
		for each in tuple:
			if (each == ""):
				each = "Unknown"

		## Initialize the Mac OS-dependent attribute objects.
		self.release      = tuple[0]
		self.version_info = tuple[1]
		self.machine      = tuple[2]

## Class Name: NixPlatform
##
## Purpose: Hold Linux/Unix OS-dependent information about the target machine.
class NixPlatform():
	## Method Name: __init__
	##
	## Purpose: Initialize the Linux/Unix OS-dependent attributes.
	##
	## Parameters
	## 1. tuple - A 4 part-tuple containing platform-independent information about the target machine.
	##    Index 0  - The full distribution name of the Linux/Unix OS.
	##    Index 1  - The version of the Linux/Unix OS running on the target machine.
	##    Index 2  - The parenthesized portion of the version. (usually a codename)
	def __init__(self, tuple):
		self.logger = logging.getLogger(self.__class__.__name__)
		self.logger.debug("BitCollector.NixPlatform.__init__():")

		## Replace unknown information ('') with "Unknown"
		for each in tuple:
			if (each == ""):
				each = "Unknown"
		
		## Initialize the Linux/Unix OS-dependent attribute objects.
		self.distname = tuple[0]
		self.version  = tuple[1]
		self.id       = tuple[2]

## Class Name: WinPlatform
##
## Purpose: Hold Windows OS-dependent information about the target machine.
class WinPlatform():
	## Method Name: __init__
	##
	## Purpose: Initialize the Windows OS-dependent attributes.
	##
	## Parameters
	## 1. tuple - A 4 part-tuple containing platform-independent information about the target machine.
	##    Index 0  - The release # of the Windows OS running on the target machine.
	##    Index 1  - The version of the Windows OS running on the target machine.
	##    Index 2  - The service pack level of the Windows OS.
	##    Index 3  - The proecessor type.
	def __init__(self, tuple):
		self.logger = logging.getLogger(self.__class__.__name__)
		self.logger.debug("BitCollector.WinPlatform.__init__():")

		## Replace unknown information ('') with "Unknown"
		for each in tuple:
			if (each == ""):
				each = "Unknown"

		## Initialize the Windows OS-dependent attribute objects.
		self.release = tuple[0]
		self.version = tuple[1]
		self.csd     = tuple[2]
		self.ptype   = tuple[3]

## Method Name: importBCModules
##
## Purpose: Dynamically import the BitCollector modules specified in the configuration file.
def importBCModules():
	_root_logger.debug("BitCollector.importBCModules():")
	
	## Populate the list of BitCollector modules. DEBUG CODE
	bc_module_list = ["os", "foo", "math", "time", "bar"]
	
	## Attempt to import each of the BitCollector modules.
	for each in bc_module_list:
		try:
			__import__(each)
			_root_logger.info("Successfully imported module: " + str(each))
		except:
			_root_logger.warning("Unable to import module: " + str(each))
		
## Method Name: main
##
## Purpose: Serves as the entry point into the script.
def main():
	_root_logger.debug("BitCollector.main():")

	## Parse the configuration file to determine runtime settings.
	parseConfig()

	## Dynamically import BitCollector modules specified in the configuration file.
	importBCModules()

	## Create a Platform instance to check the OS version. (Debug-only)
	Platform(platform.uname())

## Method Name: parseConfig
##
## Purpose: Parse through the configuration file to determine runtime settings.
def parseConfig():
	_root_logger.debug("BitCollector.parseConfig():")

## This will prevent main() from running unless explicitly called.
if __name__ == "__main__":
	main()
