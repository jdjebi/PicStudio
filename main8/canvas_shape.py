def naive_shape_drap_discrete_position_computer(event,canvas,shape_id):
    """ Calcul les nouvelles coordonnees pour deplacer une forme """
    shape_rect_position = canvas.coords(shape_id)    
    dx, dy = canvas.cursor.get_movement()
    return dx, dy

