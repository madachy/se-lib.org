build_dir = './build/html/'
for file_name in ['index.html', 'function_reference.html', 'examples.html', 'installation.html', 'search.html']:
    print(file_name)
    # Read in the file
    with open(build_dir+file_name, 'r', encoding='utf-8') as file:
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('index.html', 'index.py')
    filedata = filedata.replace(
        'function_reference.html', 'function_reference.py')
    filedata = filedata.replace('examples.html', 'examples.py')
    filedata = filedata.replace('installation.html', 'installation.py')

    # Write the file out again
    with open(build_dir+file_name, 'w', encoding='utf-8') as file:
      file.write(filedata)
