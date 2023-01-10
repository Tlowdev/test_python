highlighted_poems = """Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, 
Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   
Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, 
Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, 
In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"""
#changing string to list
highlighted_poems_list = highlighted_poems.split(',')
#cleaning up list 
highlighted_poems_stripped = []
for lines in highlighted_poems_list:
  highlighted_poems_stripped.append(lines.strip())
#separating details of list
highlighted_poems_details = []
for lines in highlighted_poems_stripped:
  highlighted_poems_details.append(lines.split(':'))
#organizing details into specific list
titles = []
poets = []
dates = []
for detail in highlighted_poems_details:
  titles.append(detail[0])
  poets.append(detail[1])
  dates.append(detail[2])
#formating a string using specific lists
for detail in range(0, len(highlighted_poems_details)):
 print("The poem {} was published by {} in {}.".format(titles[detail], poets[detail], dates[detail]))
