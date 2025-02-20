filenames = ["1.doc", '1.report', '1.presentation']

filenames = [filename.replace('.','-') + '.txt' for filename in filenames]
print(filenames)

user_entries = ['10', '19.1', '20']
floatinglist = []
for user_entry in user_entries:
    user_entry = float(user_entry)
    floatinglist.append(user_entry)

a = floatinglist[1] + floatinglist[2] + floatinglist[0]
print(a)


