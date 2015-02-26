##################
##
# This script generates the 47 monthly data files for the Softalk Top 30 Dataset
# by Jim Salmons, devs_at_factminers.org
#
import csv
import os

row_data_cols = {'Oct-80', 'Nov-80', 'Dec-80', 'Jan-81', 'Feb-81', 'Mar-81', 'Apr-81', 'May-81',
                 'Jun-81', 'Jul-81', 'Aug-81', 'Sep-81', 'Oct-81', 'Nov-81', 'Dec-81',
                 'Jan-82', 'Feb-82', 'Mar-82', 'Apr-82', 'May-82', 'Jun-82', 'Jul-82',
                 'Aug-82', 'Sep-82', 'Oct-82', 'Nov-82', 'Dec-82', 'Jan-83', 'Feb-83',
                 'Mar-83', 'Apr-83', 'May-83', 'Jun-83', 'Jul-83', 'Aug-83', 'Sep-83',
                 'Oct-83', 'Nov-83', 'Dec-83', 'Jan-84', 'Feb-84', 'Mar-84', 'Apr-84',
                 'May-84', 'Jun-84', 'Jul-84', 'Aug-84', 'Sep-84'}

issue_date_dict = {'v1no02': 'Oct-80', 'v1no03': 'Nov-80', 'v1no04': 'Dec-80',
                   'v1no05': 'Jan-81', 'v1no06': 'Feb-81', 'v1no07': 'Mar-81',
                   'v1no08': 'Apr-81', 'v1no09': 'May-81', 'v1no10': 'Jun-81',
                   'v1no11': 'Jul-81', 'v1no12': 'Aug-81', 'v2no01': 'Sep-81',
                   'v2no02': 'Oct-81', 'v2no03': 'Nov-81', 'v2no04': 'Dec-81',
                   'v2no05': 'Jan-82', 'v2no06': 'Feb-82', 'v2no07': 'Mar-82',
                   'v2no08': 'Apr-82', 'v2no09': 'May-82', 'v2no10': 'Jun-82',
                   'v2no11': 'Jul-82', 'v2no12': 'Aug-82', 'v3no01': 'Sep-82',
                   'v3no02': 'Oct-82', 'v3no03': 'Nov-82', 'v3no04': 'Dec-82',
                   'v3no05': 'Jan-83', 'v3no06': 'Feb-83', 'v3no07': 'Mar-83',
                   'v3no08': 'Apr-83', 'v3no09': 'May-83', 'v3no10': 'Jun-83',
                   'v3no11': 'Jul-83', 'v3no12': 'Aug-83', 'v4no01': 'Sep-83',
                   'v4no02': 'Oct-83', 'v4no03': 'Nov-83', 'v4no04': 'Dec-83',
                   'v4no05': 'Jan-84', 'v4no06': 'Feb-84', 'v4no07': 'Mar-84',
                   'v4no08': 'Apr-84', 'v4no09': 'May-84', 'v4no10': 'Jun-84',
                   'v4no11': 'Jul-84', 'v4no12': 'Aug-84'}

# There is no Top 30 list for Sept'80, V1No01, so there are 47 lists, not 48.
top30_lists = {'v1no02': {},
               'v1no03': {},
               'v1no04': {},
               'v1no05': {},
               'v1no06': {},
               'v1no07': {},
               'v1no08': {},
               'v1no09': {},
               'v1no10': {},
               'v1no11': {},
               'v1no12': {},
               'v2no01': {},
               'v2no02': {},
               'v2no03': {},
               'v2no04': {},
               'v2no05': {},
               'v2no06': {},
               'v2no07': {},
               'v2no08': {},
               'v2no09': {},
               'v2no10': {},
               'v2no11': {},
               'v2no12': {},
               'v3no01': {},
               'v3no02': {},
               'v3no03': {},
               'v3no04': {},
               'v3no05': {},
               'v3no06': {},
               'v3no07': {},
               'v3no08': {},
               'v3no09': {},
               'v3no10': {},
               'v3no11': {},
               'v3no12': {},
               'v4no01': {},
               'v4no02': {},
               'v4no03': {},
               'v4no04': {},
               'v4no05': {},
               'v4no06': {},
               'v4no07': {},
               'v4no08': {},
               'v4no09': {},
               'v4no10': {},
               'v4no11': {},
               'v4no12': {}}

source_file = csv.DictReader(open("Top30_v2.csv"))

# First, gather up all ratings into their respective Top 30 lists
# in preparation for file generation.
for row in source_file:
    top30_program = row['Program']
    # For each Top 30 list, check for a data value and add the index and ordinal
    # values if found together with the program's name.
    for issue in row_data_cols:
        if row.get(issue) is not '':
            for volnum, pubdate in issue_date_dict.items():
                if pubdate == issue:
                    # Add the item to the issue's Top 30 list
                    top30_lists[volnum][top30_program] = {'position': int(row[pubdate + '2']),
                                                          'index': float(row[pubdate])}

# Now, generate a CSV file for each Top 30 list...
for filename, raw_top30 in top30_lists.items():
    file_path = os.path.join("top30_monthly/", filename + "_top30.csv")
    with open(file_path, 'a') as outcsv:
        #configure writer to write standard csv file
        writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['Program', 'Position', 'Index'])
        for item in sorted(raw_top30.items(), key=lambda t: t[1]['position']):
            #Write item to outcsv
            writer.writerow([item[0], item[1]['position'], item[1]['index']])

print("That's all folks!")