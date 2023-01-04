#EPI in Python 4.11
#Give 2 Rectangle (Bottom Left most cordinates, width, and height) -> Determine if the 2 rectangles intersect.
#If they intersect return the Cordinates, width, height of the new Rectangle formed by their intersection.
import collections

Rectangle = collections.namedtuple('Rectangle',('x', 'y', 'width', 'height'))
def new_rectangle(R1, R2):
    def is_intersection(R1, R2):
        return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x and R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)
    if (not is_intersection(R1, R2)):
        return Rectangle(0,0,-1,-1)
    return (
        max(R1.x, R2.x),
        max(R1.y, R2.y),
        (min(R1.x + R1.width, R2.x + R2.width)-max(R1.x, R2.x)),
        (min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))
    )

#driver code sample
# R1 = Rectangle(1,1,4,3)
# R2 = Rectangle(2,2,4,3)
# print(new_rectangle(R1,R2))

x1,y1,w1,h1 = map(int,input('Enter cordinated, width, height for 1st Rectangle seperated by comma: ').split(','))
R1 = Rectangle(x1,y1,w1,h1)
x2,y2,w2,h2 = map(int,input('Enter cordinated, width, height for 2nd Rectangle seperated by comma: ').split(','))
R2 = Rectangle(x2,y2,w2,h2)
print('The values for intersection Rectangle are: ',new_rectangle(R1, R2))






