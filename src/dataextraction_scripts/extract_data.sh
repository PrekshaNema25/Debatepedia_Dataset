# Run the bash script to extract the data from debatepedia website.

# Give the links to the categories in the "categories" file, the debate links will be extracted 
# These links will be stored in category_links/all_links
python extract_links categories


#To extract the document/summary/query from the output of the above command:
#The text files containing the above mentioned information will be stored in the 
#director Data
python extract_text category_links/all_links Data


