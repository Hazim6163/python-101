
from classes.component import Component


print('----------------------')
print('Me 4 Life  |  Components Generator')
print('----------------------')

templateName = input('[?] Template Name:  ')
pID = input('[?] Global ID:  ')
pClass = input('[?] Global CSS Class:   ')
#create components array
components = []
#info    msg
print('... Start Creating Components')
#create component obj
component  = Component(1)
#push component to components array: 
components.append(component)
