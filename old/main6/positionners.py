def centerize_placement(x,y,w,h,offset=(0,0)):
        """ 
            Calcul est position de placement de sorte a simulter un positionnement au centre de gravite.
            L'offset permet de creer un decalage pour bien ajuster la forme par rapport au curseur.
        """
        w_middle = int(w/2)
        h_middle = int(h/2)
        x1 = x - w_middle - offset[0]
        y1 = y - h_middle - offset[1]
        x2 = x1 + w
        y2 = y1 + h
        return x1, y1, x2, y2