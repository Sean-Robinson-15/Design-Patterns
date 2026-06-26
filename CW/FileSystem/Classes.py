#Composite pattern
from abc import ABC, abstractmethod

#The Component interface that defines the common operations for both files and directories.
class FileSystemComponent(ABC):
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def size(self):
        pass
    @abstractmethod
    def display(self, indent = 4):
        pass
    @abstractmethod
    def count(self):
        pass
    @abstractmethod
    def find(self, name):
        pass
    @abstractmethod
    def path(self):
        pass
    @abstractmethod
    def parent(self):
        pass
    
    def get_children(self):
        raise NotImplementedError("This component does not have children.")
    
    def add(self, child):
        raise NotImplementedError("Cannot add child to this component.")
    
    def remove(self, child):
        raise NotImplementedError("Cannot remove child from this component.")

# The Leaf class
class File(FileSystemComponent):
    def __init__(self, name, size):
        self._name = name
        self._size = size
        self._parent = None
        
    def name(self):
        return self._name
    
    def size(self):
        return self._size

    def display(self, indent):
        print(" " * indent + f"{self._name} (File, {self._size} bytes)")
        
    def count(self):
        return 1
    
    def find(self, name):
        return self if self._name == name else None

    def path(self):
        if self._parent:
            return self._parent.path() + "/" + self._name
        return self._name
    
    def parent(self):
        return self._parent

# The Composite class
class Directory(FileSystemComponent):
    def __init__(self, name, root = False):
        self._name = name
        self._children = {}
        self._parent = None
        self._root = root
        
    def name(self):
        return self._name
    
    def size(self):
        return sum(child.size() for child in self._children.values())
    
    def add(self, child):
        child._parent = self
        self._children[child.name()] = child
    
    def remove(self, child):
        del self._children[child.name()]
    
    def display(self, indent = 4):
        print(" " * indent + f"{self._name} (Directory, {self.size()} bytes, {self.count()} items)")
        for child in self._children.values():
            child.display(indent=indent+4)

    def count(self):
        return sum(child.count() for child in self._children.values())
    
    def find(self, name):
        if self._name == name:
            return self
        for child in self._children.values():
            found = child.find(name)
            if found:
                return found
        return None
    
    def path(self):
        if self._parent:
            return self._parent.path() + "/" + self._name
        return self._name
    
    def get_children(self):
        return self._children.copy()
    
    def parent(self):
        return self._parent