README.txt

CONTENTS OF THIS FILE
---------------------
   
 * Introduction
 * Requirements
 * Configuration
 * Instructions


INTRODUCTION
------------

This script will create a list of query acronym pairs given a list of queries, for example if the first searched query is 'ama' and the second searched query is 'ask me anything' we can assume that 'ama' is an acronym for 'ask me anything' and create a query pair.


REQUIREMENTS
------------

This module requires the following external modules:

 * pandas
 * csv
 * re


CONFIGURATION
-------------

 * query-refinements-to-keyword-acronym-pairs-generator.py - script
 * configurationVariables.py - configuration variables
 * input-query1-query2-pairs.csv - input file with search query pairs


INSTRUCTIONS
-------------

Input File:
	csv: input-query1-query2-pairs.csv

	0,		1,											2
	ama,	ask me anything,							1
	ama,	ask me anything,							1
	daw,	digital audio workstation,					1
	lp,		long play,									1
	iwsc,	international standard musical work code,	1
	pm,		product manager,							1
	car,	vehicle,									1
	star,	sun,										1
	bread,	basket,										1

Command:
    $ python3 epicManagementData.py

Output File: 
    csv: output-query1-query2-acronym-pairs.csv

    pair_ID,	SearchQuery1,	SearchQuery2,				Count
	1001,		ama,			ask me anything,			2
	1006,		lp,				long play,					1
	1007,		pm,				product manager,			1
	1004,		daw,			digital audio workstation,	1