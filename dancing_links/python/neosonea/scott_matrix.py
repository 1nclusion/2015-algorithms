import pentominos
import incidence_matrix
import examples

class Scott_matrix(object):
    def __init__(self, width, height):
        self.width = 8;
        self.height = 8;

    
    def create_scott_matrix(self, legal):
        self.IM = examples.scott_example()

        #column = IM.h.right
        #while (not column.name.isdigit()) and (not column.name is "root")
        #    p = Pentomino(column.name)
        #TODO for flipping
        for p in pentominos.all_fixed_pentominos():
            self.create_all_rows_for(p, legal)
        #    column = column.right
        print(self.IM.representation())
        return self.IM

    def solve_scott_matrix(self, legal):
        pass

    def create_all_rows_for(self, p, legal):
        p.normalize();
        for i in range(self.width):
            for j in range(self.height):
                if legal(p):
                    print(" p"+p.name+" ij="+str(i)+str(j)+"  "+str([str(pos[0])+str(pos[1]) for pos in p.coos]))
                    self.IM.appendRow(p.name, [str(pos[0])+str(pos[1]) for pos in p.coos]);#([[c[0]+1,c[1]] for c in pentominos.I().coos]
                p.translate_one(1);
            p.normalize_coo(1);
            p.translate_one(0);

    def scott_legal(self, p):
        for hole in [ [3,3],[3,4],[4,3],[4,4] ]:
            if hole in p.coos:
                return False
        if p.max()[0] > self.width-1 or p.max()[1] > self.height-1:
            return False;
        return True
