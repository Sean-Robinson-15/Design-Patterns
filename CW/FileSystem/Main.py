from Classes import *
def main():
    root_directory = Directory("root", True)
    file = File("file.txt", 100)
    root_directory.add(file)
    print("---------------------------------------------------------------")
    root_directory.display()
    print("---------------------------------------------------------------")
    root_directory.add(Directory("subdir"))
    root_directory.display()
    print("---------------------------------------------------------------")
    root_directory.get_children()["subdir"].add(Directory("subdir-subdir"))
    root_directory.get_children()["subdir"].get_children()["subdir-subdir"].add(File("subfile.txt", 50))
    root_directory.display()
    print("---------------------------------------------------------------")
    print(f"Root directory size: {root_directory.size()} bytes")
    root_directory.remove(file)
    root_directory.display()
    print("---------------------------------------------------------------")
    subfile=root_directory.find("subfile.txt")
    print(subfile.path())
    

if __name__ == "__main__":    
    main()