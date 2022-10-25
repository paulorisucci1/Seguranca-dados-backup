class File:
    def __init__(self, name):
        self.__flag_modified = True
        self.__name = name
        self.__file_content = open(name).read()
        self.__new_file = True

    @property
    def name(self):
        return self.__name

    @property
    def was_modified(self):
        return self.__flag_modified

    def __has_changes(self):
        return open(self.__name).read() != self.__file_content

    def watch_modifications(self):
        if self.__has_changes() or self.__new_file:
            self.__new_file = False
            self.__flag_modified = True
            self.__file_content = open(self.__name).read()
        else:
            self.__flag_modified = False
