class Room(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.paths = {}
    def go(self,direction):
        return self.paths.get(direction, None)
    def add_paths(self, paths):
        self.paths.update(paths)       
        
