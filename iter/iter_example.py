def filter_text(file_name):
    with open(file_name, 'rt') as f:
        for line in iter(lambda: f.readline().strip(), 'END'):
            print(line)

filter_text('some_file.txt')