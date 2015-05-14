
# coding: utf-8

# In[3]:

import csv

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(rawfile, delimiter):
    opened_file = open(rawfile)
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    parsed_data = []
    fields = csv_data.next()
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))
    opened_file.close()
    return parsed_data

def main():
    new_data = parse(MY_FILE, ",")
    print(new_data)

if __name__ == "__main__":
    main()
    


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# 

# In[ ]:



