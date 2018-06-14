import os


# Creating directory for each project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


# Create queue and crawled, if not created already
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Append file
def append_to_file(path, data):
    with open(path, 'a') as f:
        f.append(data)


# Delete file contents
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read a file and convert each line to set items
def file_to_set(filename):
    results = set()
    with open(filename, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Each set item will be added as a new line in the file
def set_to_file(links, filename):
    delete_file_contents(filename)
    for link in links:
        append_to_file(filename, link)



