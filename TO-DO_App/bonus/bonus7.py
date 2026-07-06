filenames = ['1.doc', '1.report', '1.presentation']
new_filenames = []

#could be the following code too:
#filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
for name in filenames:
    new_name = name.replace('.', '-') + '.txt.'
    new_filenames.append(new_name)

for filename in enumerate(new_filenames, start= 1):
    print(new_filenames)