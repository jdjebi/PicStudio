class Position:
    x = None
    y = None

    def updateByPosition(self,position):
        self.x = position.x
        self.y = position.y
    
    def updateByValues(self,x,y):
        self.x = x
        self.y = y
    
    def get(self):
        return (self.x,self.y)

class CursorPosition:
    old_position = Position()
    current_position = Position()

    def update(self,new_x,new_y):
        self.old_position.updateByPosition(self.current_position)
        self.current_position.updateByValues(new_x,new_y)
    
    def get_movement(self):
        """ Retourne la distance en pixel du dernier deplacement elementaire du curseur. """
        dx = self.current_position.x - self.old_position.x
        dy = self.current_position.y - self.old_position.y
        return dx, dy
