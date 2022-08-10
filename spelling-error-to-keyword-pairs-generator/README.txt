README.txt

CONTENTS OF THIS FILE
---------------------
   
 * Introduction
 * Requirements
 * Configuration
 * Instructions


INTRODUCTION
------------

This script will output a csv of (spelling error|keyword) pairs given 2 keywords in a sequence that fall within a Levenshtein Distance of 2, for example if the first searched keyword is 'musik theory' and the second searched keyword is 'music theory' and create a query pair.


REQUIREMENTS
------------

This module requires the following external modules:

 * pandas
 * Levenshtein


CONFIGURATION
-------------

 * spelling-error-to-keyword-pairs-generator.py.py - script
 * configurationVariables.py - configuration variables
 * input-keyword-sequence-pairs.csv - input file with searched keywords in a sequence, mapped to 1 ID per sequence


INSTRUCTIONS
-------------

Input File:
	csv: input-keyword-sequence-pairs.csv

	ID		Keyword		Count
	1000	musik theory	1
	1000	music theory	1
	1001	musik theory	1
	1001	music theory	1
	1002	music theor		1
	1002	music theory	1
	1003	musi theory		1
	1003	music theory	1
	1004	harmoni			1
	1004	harmony			1
	1005	chordd			1
	1005	chords			1
	1006	harmoni			1
	1006	harmonics		1
	1007	moosik theory	1
	1007	music theory	1
	1008	music theory	1
	1008	music theory	1
	1009	panda bear		1
	1009	music theory	1

Command:
    $ python3 spelling-error-to-keyword-pairs-generator.py

Output File: 
    csv: output-query1-query2-acronym-pairs.csv

    Keyword Sequence 1		Keyword Sequence 2		Count
	musik theory			music theory			2
	musi theory				music theory			1
	music theor				music theory			1
	harmoni					harmony					1
	harmoni					harmonics				1
	chordd					chords					1
