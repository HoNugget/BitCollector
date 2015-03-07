## File Name: Test1.py
##
## Author(s): Daniel "Albinohat" Mercado
##
## Purpose: This script is being used to test the dynamic import functionality of bitCollector_main.py
##          It will also be used as a template when creating future modules.
##
## Glossary
## 1. Required - The method or parameters MUST be present in order to work with framework.
## 2. Optional - The method or parameters are NOT REQUIRED. They are meant to serve as a guide or an example only.
##               i.e) Optional methods MAY be left out and the code can be put in the main() method.
##                    Make your code legible, though. :)
## Standard Imports
import json, logging, sys

## Global Variable Declarations - CONSTANTS - DO NOT CHANGE @ RUNTIME
_module_version = "Test1 Module: v0.1.0 Released 2015-03-06"

## Class Declarations

## Class Name: ModuleSettings
##
## Purpose: Hold information about the settings required to run this BitCollector module.
class ModuleSettings():
	## Method Name: __init__
	##
	## Purpose: Initialize the settings required to start the framework.
	##
	## Parameters
	## 1. module - The name and parameters to pass to the BitCollector module to be initialized.
	def __init__(self, module):
		## Loop through the dictionary containing this module's name and settings.
		for key in module:
			## Grab the name of this module as known by bitCollector_main
			if (key == "name"):
				self.name = module[key]
			
			## Grab the dictionary containing the list of settings dictionaries (head spinning yet? Mine was)
			elif (key == "parameters"):
				## Loop through the list of dictionaries containing setting names and values.
				for param_pair in module[key]:
					## Finally loop through each dictionary containing a single setting's name and value.
					for param, value in param_pair.iteritems():
						## Use an if-elif block to extract the settings and store them in named veriables.
						if (param == "par1"):
							self.par1 = str(value)

						elif (param == "par2"):
							self.par2 = value
							
						elif (param == "logging_level"):
							self.logging_level = value
							
						else:
							print "Startup - Test1.RuntimeSettings.__init__ - ERROR - Unexpected parameter: " + str(param) + ". Ignoring."
	
		## Call the method to initialize the module-level logger.
		self.initializeLogger()
		
	## Method Name: initializeLogger
	##
	## Purpose: Initializes the logger for this BitCollector module.
	##
	def initializeLogger(self):
		## Initialize the logger for this BitCollector module.
		self.logger = logging.getLogger(self.__class__.__name__)
		
		## Override the logging level from the root logger. (Optional)
		## This is meant to give access to debug-level logging without
		## needing to see the debug output form the framework.
		
		## Set the logging level for the root logger. (Can be overridden for each module.)		
		if (self.logging_level.upper() == "DEBUG"):
			self.logger.setLevel(logging.DEBUG)

		elif (self.logging_level.upper() == "INFO"):
			self.logger.setLevel(logging.INFO)

		elif (self.logging_level.upper() == "WARNING"):
			self.logger.setLevel(logging.WARNING)

		elif (self.logging_level.upper() == "ERROR"):
			self.logger.setLevel(logging.ERROR)

		elif (self.logging_level.upper() == "CRITICAL"):
			self.logger.setLevel(logging.CRITICAL)

		else:
			print "Startup - bitCollector_main.RuntimeSettings.initializeRootLogger - WARNING - Unknown logging level \"" + self.logging_level + "\" Defaulting to DEBUG."
			self.logger.setLevel(logging.DEBUG)
			
		self.logger.debug("Successfully started Test1 logger!")
		
## Classless Method Declarations		

## Method Name: main (Required)
##
## Purpose: Serves as the entry point into the script.
##
## Parameters (All Required)
## 1. thread_id        - The ID of the thread containing this BitCollector module.
## 2. path_to_main     - The absolute path to the bitCollector_main which initialized this BitCollector module.
## 3. runtime_settings - An instance of the RuntimeSettings class containing settings required to start the framework.
## 4. platform_details - An instance of the Platform class containing the platform-independent attributes as well as a platform-dependent object.
## 5. module           - The name and parameters to pass to the BitCollector module to be initialized.
def main(thread_id, path_to_main, runtime_settings, platform_details, module):
	## Add the additional search path for bitCollector_main.
	## Might not be needed, but good practice for now.
	sys.path.append(path_to_main)
	
	## Import bitCollector_main.
	## Might not be needed, but good practice for now.
	import bitCollector_main

	## Initialize an instance of the ModuleSettings class to store the settings required to start the module.
	module_settings = ModuleSettings(module)
		
	## Create a logger for methods called by main()
	## Set it's logging level. (Optional)
	## You only need to do this to override the root logging level from the framework.
	main_logger = logging.getLogger("module_root")
	main_logger.setLevel(module_settings.logging_level.upper())
	main_logger.debug("Initialized main_logger")
	
	main_logger.info("Test1 module started successfully!")
	print module_settings.par1

if (__name__ == "__main__"):
	main(thread_id, path_to_main, runtime_settings, platform_details, module)