import re


class FileSystemError(Exception):
    pass


class NotEnoughSpaceError(FileSystemError):
    pass


class DestinationNotADirectoryError(FileSystemError):
    pass


class NodeDoesNotExistError(FileSystemError):
    pass


class DeletionError(FileSystemError):
    pass


class DestinationNodeExistsError(FileSystemError):
    pass


class NonEmptyDirectoryDeletionError(DeletionError):
    pass


class NonExplicitDirectoryDeletionError(DeletionError):
    pass


class SourceNodeDoesNotExistError(NodeDoesNotExistError):
    pass


class DestinationNodeDoesNotExistError(NodeDoesNotExistError):
    pass


class FileSystemMountError(FileSystemError):
    pass


class MountPointDoesNotExistError(FileSystemMountError):
    pass


class MountPointNotADirectoryError(FileSystemMountError):
    pass


class MountPointNotEmptyError(FileSystemMountError):
    pass


class FileSystem:
    DIR_SEPARATOR = "/"
    DIR_SIZE = 1
    ROOT_PATH = "/"

    def __init__(self, size):
        self.size = size
        self.available_size = size - FileSystem.DIR_SIZE
        self._root_node = Directory(FileSystem.ROOT_PATH)

    def get_node(self, path):
        if path == FileSystem.ROOT_PATH:
            return self._root_node
        if path == "":
            raise NodeDoesNotExistError

        path = path.split(FileSystem.DIR_SEPARATOR)[1:]
        node = self._root_node
        while len(path) > 0:
            name = path.pop(0)
            if name not in node.paths.keys():
                raise NodeDoesNotExistError
            node = node.paths[name]
        return node

    def create(self, path, directory=False, content=''):
        try:
            node = self.get_node(self.__get_parent_dir_path(path))
            name = self.__extract_name_from_path(path)
            if not node.is_directory:
                raise DestinationNotADirectoryError
            if name in node.paths.keys():
                raise DestinationNodeExistsError
        except NodeDoesNotExistError:
            raise DestinationNodeDoesNotExistError

        if directory:
            needed_space = FileSystem.DIR_SIZE
            new_node = Directory(path)
        else:
            needed_space = len(content) + 1
            new_node = File(path, content)

        self.__alocate_size(needed_space)
        node.add_node(new_node)

    def remove(self, path, directory=False, force=True):
        node = self.get_node(path)
        if node.is_directory:
            if not directory:
                raise NonExplicitDirectoryDeletionError
            elif len(node.nodes) > 0 and not force:
                raise NonEmptyDirectoryDeletionError
        parent = self.get_node(self.__get_parent_dir_path(node.path))
        if node.is_directory:
            for child_node in node.nodes:
                if child_node.is_directory:
                    self.remove(child_node.path, True, True)
                else:
                    node.remove_node(child_node)
                    self.available_size += child_node.size
            parent.remove_node(node)
            self.available_size += node.size
        else:
            parent.remove_node(node)
            self.available_size += node.size

    def move(self, source, destination):
        try:
            source = self.get_node(source)
        except NodeDoesNotExistError:
            raise SourceNodeDoesNotExistError
        try:
            destination = self.get_node(destination)
            if not destination.is_directory:
                raise DestinationNotADirectoryError
            if source.name in destination.paths.keys():
                raise DestinationNodeExistsError
        except NodeDoesNotExistError:
            raise DestinationNodeDoesNotExistError

        self.remove(source.path, source.is_directory, True)
        if source.is_directory:
            for node in source.nodes:
                if node.is_directory:
                    self.move(node.path, destination.path)
                else:
                    dest_path = destination.path + FileSystem.DIR_SEPARATOR
                    dest_path += node.name
                    self.create(dest_path, False, node.content)
        else:
            dest_path = destination.path + FileSystem.DIR_SEPARATOR
            dest_path += source.name
            self.create(dest_path, False, source.content)

    def link(self, source, destination, symbolic=True):
        pass

    def mount(self, file_system, path):
        pass

    def unmount(self, path):
        pass

    def __alocate_size(self, size):
        self.available_size -= size
        if self.available_size < 0:
            self.available_size += size
            raise NotEnoughSpaceError

    def __extract_name_from_path(self, path):
        path = path.split(FileSystem.DIR_SEPARATOR)
        path = [node_name for node_name in path if node_name != ""]
        if len(path) > 0:
            return path.pop()
        else:
            return FileSystem.ROOT_PATH

    def __get_parent_dir_path(self, path):
        name = self.__extract_name_from_path(path)
        path = re.sub(r"/{}/*".format(name), "", path)
        if path == "":
            path = FileSystem.ROOT_PATH
        return path


class File:

    def __init__(self, path, content=''):
        self.path = path
        self.content = content
        self.is_directory = False

    @property
    def name(self):
        return self.path.split(FileSystem.DIR_SEPARATOR)[-1]

    def append(self, text):
        self.content += text

    def truncate(self, text):
        self.content = text

    @property
    def size(self):
        return len(self.content) + 1

    def add_node(self):
        raise DestinationNotADirectoryError


class Directory:

    def __init__(self, path):
        self.path = path
        self.content = []
        self.is_directory = True


    @property
    def name(self):
        return self.path.split(FileSystem.DIR_SEPARATOR)[-1]

    @property
    def size(self):
        return FileSystem.DIR_SIZE

    @property
    def directories(self):
        directories = {}
        for node in self.content:
            if node.is_directory:
                directories[node.name] = node
        return directories

    @property
    def files(self):
        files = {}
        for node in self.content:
            if not node.is_directory:
                files[node.name] = node
        return files

    @property
    def paths(self):
        paths = self.files.copy()
        paths.update(self.directories)
        return paths

    @property
    def nodes(self):
        return self.content

    def add_node(self, node):
        self.content.append(node)

    def remove_node(self, node):
        self.content.remove(node)
