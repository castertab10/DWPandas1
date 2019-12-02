import pandas as pd

a = { 'Student' : ['Ice Bear', 'Panda', 'Grizzly'], 
        'Math': [80, 95, 79]}

b = { 'Student' : ['Ice Bear', 'Panda', 'Grizzly'], 
        'Electronics': [85, 81, 83]}

c = { 'Student' : ['Ice Bear', 'Panda', 'Grizzly'], 
        'GEAS': [90, 79, 93]}

d = { 'Student' : ['Ice Bear', 'Panda', 'Grizzly'], 
        'ESAT': [93, 89, 88]}

we = pd.DataFrame(a, columns=['Student', 'Math'])
bare = pd.DataFrame(b, columns=['Student', 'Electronics'])
bears = pd.DataFrame(c, columns=['Student', 'GEAS'])
arecute = pd.DataFrame(d, columns=['Student', 'ESAT'])

fluffy = pd.merge(we,bare, how = 'left', on='Student')
adorable = pd.merge(fluffy,bears, how = 'left', on='Student')
huggable = pd.merge(adorable,arecute, how = 'left', on='Student')
tidy_bears = pd.melt(huggable, id_vars =['Student'], value_vars =['Math', 'Electronics', 'GEAS', 'ESAT'])
x = tidy_bears.rename(columns = {'variable' : 'Subject', 'value':'Grades'})
y = x.sort_values('Student')
z = y.reset_index()
etonatalaga = z.drop(columns = 'index')