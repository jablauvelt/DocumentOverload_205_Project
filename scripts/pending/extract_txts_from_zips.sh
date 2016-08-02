#!/bin/bash
# Project: Dealing with Document Overload
# Script: Extract XML Metadata from ZIPs
# Purpose: The purpose of this script is to extract the XML metadata files from
# the enron repository. Note: this script takes under 10 minutes to run.

# I have previously mounted the EBS (Elastic Block Storage) into the /enron folder.
cd /enron/edrm-enron-v2/

# Kaminski zips were already addressed in extract_xmls_...

# Create list of xml zips. Remove Kean and Kaminski extra zip files (the ones that 
# don't have "partXofY" in the file name)
XML_ZIPS=$(ls | grep xml.*zip | grep -v kean-s_xml\\.zip | grep -v kaminski-v_xml\\.zip)

# Create unzipped_txt directory
mkdir unzipped_txt

# Create a folder for each custodian and extract just the XML metadata files into it.
for i in $XML_ZIPS
do 
	TXT_FILES=$(unzip -l $i | grep .txt | sed 's/.*text.....\(fl\)*/\1/')
	echo $TXT_FILES
	txt_folders=$($TXT_FILES | sed 's/.*text_\(textnum\)*/\1/')
	txt_folders="${$txt_folders:2:1}"
	txt_folders=$($txt_folders | sort |unq)
	for j in $txt_folders
	do
		for k in $($TXT_FILES | grep text_00$j)
		do
			unzip -j "$k" -d "/enron/edrm-enron-v2/unzipped_txt/$j - $(basename $k .txt)"	
		done
	done
done
