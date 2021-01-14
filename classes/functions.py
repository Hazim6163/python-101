from classes.component import Component


def genChild(component):
    #ask about children
    isChildren = input('[?] {} children? y or n  '.format(component.name))
    if(isChildren == 'n'):
        return
    #info msg
    print('\n... [!] inserting to {} ...\n'.format(component.name))
    #component blue print: 
    
    #start children loop . 
    while True:
        #create child
        child = Component(component.level + 1)
        #push child to children
        component.children.append(child)
        #info : 
        print('... {}  to  {}    done !'.format(child.name, component.name))
        #check if the child has children: 
        genChild(child)
        #ask about children
        isNChildren = input('[?] {} next Child ? y or n  '.format(component.name))
        if(isNChildren == 'n'):
            break

def printChildren(array):
    for c in array:
        print(
            '   ' + c.name + '\n' +  
            '   ' + '   -' + c.cType + '\n' + 
            '   ' + '   -' + c.cID
        )

def genFile(array):
    for a in array:
        print(
            a.name + '\n' +  
            '   -' + a.cType + '\n' + 
            '   -' + a.cID
        )
        if(len(a.children) > 0):
            printChildren(a.children)
        


