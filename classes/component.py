class Component: 

    def __init__(self, level) -> None:
        self.name = input('[?] Component Name:  ')
        print('... {} ... '.format(self.name))
        self.cType = input('[?] Component Type:  ')
        print('... {} .. {} ... '.format(self.cType, self.name))
        self.cID = input('[?] Component custom ID:  ')
        print('... {} .. {} ... '.format(self.cType, self.name))
        self.cClass = input('[?] Component custom CSS Classes:  ')
        print('... {} .. {} ... '.format(self.cType, self.name))
        self.visible = input('[?] Visible:  y or n ')
        self.level = level
        self.children = []
        print('... {} created !!.... '.format(self.name))