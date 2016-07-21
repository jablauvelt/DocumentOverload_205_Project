#!/bin/bash
# Project: Dealing with Document Overload
# Script: Extract XML Metadata from ZIPs
# Purpose: The purpose of this script is to extract the XML metadata files from
# the enron repository. Note: this script takes under 10 minutes to run.

# I have previously mounted the EBS (Elastic Block Storage) into the /enron folder.
cd /enron/edrm-enron-v2/

# Zip up Kaminksi zips, because they are separated into .zip and .z01. Kean zips
# are similarly split up with parts, but it looks like someone already zipped them
# into _part1of8, _part2of8, etc. do not appear to need zipping
zip -FF edrm-enron-v2_kaminski-v_xml.zip --out edrm-enron-v2_kaminski-v_xml_full.zip

# Create list of xml zips. Remove Kean and Kaminski extra zip files (the ones that 
# don't have "partXofY" in the file name)
XML_ZIPS=$(ls | grep xml.*zip | grep -v kean-s_xml\\.zip | grep -v kaminski-v_xml\\.zip)

# Create unzipped directory
mkdir unzipped

# Create a folder for each custodian and extract just the XML metadata files into it.
for i in $XML_ZIPS
do 
	mkdir "unzipped/$(basename $i .zip)"
	unzip -j $i "*.xml" -d "/enron/edrm-enron-v2/unzipped/$(basename $i .zip)"	
done


