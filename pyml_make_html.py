build_dir = './build/html/'
for file_name in ['index.html', 'function_reference.html', 'examples.html', 'installation.html', 'search.html']:
    # Read in the file
    with open(build_dir+file_name, 'r', encoding='utf-8') as file:
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('Quick search', 'Search')
    filedata = filedata.replace('<h3>Navigation</h3>', '<h3>Contents</h3>')
    filedata = filedata.replace(
        """<h1 class="logo"><a href="master_doc.html">PyML</a></h1>""", '')

    # set navbar active class
    filedata = filedata.replace(
        f"""<a href="{file_name}">""", f"""<a class="active" href="{file_name}">""")

    if file_name == "index.html":
        filedata = filedata.replace("""<h1>Home""",
                                    """<h1 class="pyml_home">""")

    # Write the file out again
    with open(build_dir+file_name, 'w', encoding='utf-8') as file:
      file.write(filedata)

    print(file_name)
