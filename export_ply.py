import pointshape as ps
import parametric_to_ply as para

def export_faces(shape,filename):
    if shape == None:
        return

    with open(filename,'w+') as f:
        f.write(
                "ply\nformat ascii 1.0\n" +
                "element vertex " + str(len(shape.vertices.points)) + "\n" +
                "property float x\nproperty float y\nproperty float z\n" +
                "element face " + str(len(shape.faces)) + "\n" +
                "property list uchar int vertex_index\n" +
                #"property uchar red\nproperty uchar green\nproperty uchar blue\n"
                "end_header\n"
                )
        for p in shape.vertices.points:
            f.write(str(p.x) + ' ' + str(p.y) + ' ' + str(p.z) + '\n')
        for q in shape.faces:
            f.write(str(len(q)) + ' ' + ' '.join([str(i) for i in q]) + '\n')
            #f.write(' ' + str(shape.color.r) + ' ' + str(shape.color.g) + ' ' + str(shape.color.b) + '\n')
    return


def export_edges(shape, filename):
    if shape == None:
        return

    with open(filename,'w+') as f:
        f.write(
            "ply\nformat ascii 1.0\n" +
            "element vertex " + str(len(shape.vertices.points)) + "\n" +
            "property float x\nproperty float y\nproperty float z\n" +
            "element edge " + str(len(shape.vertices.points) -1) + "\n" +
            "property int vertex1\nproperty int vertex2\n" +
            "end_header\n"
        )
        for p in shape.vertices.points:
            f.write(str(p.x) + ' ' + str(p.y) + ' ' + str(p.z) + '\n')
        for i in range(len(shape.vertices.points) - 1):
            f.write(str(i) + ' ' + str(i+1) + '\n')
    return

'''
def export_edges(shape,filename):
    with open(filename,'w') as f:
        f.write(
                "ply\nformat ascii 1.0\n" +
                "element vertex " + str(len(shape.vertices.points)) + "\n" +
                "property float x\nproperty float y\nproperty float z\n" +
                "element face " + str(len(shape.faces)) + "\n" +
                "property list uchar int vertex_index\n" +
                #"property uchar red\nproperty uchar green\nproperty uchar blue\n"
                "end_header\n"
                )
        for p in shape.vertices.points:
'''

def main():
    #PointClouds
    #p_w1 = para.winter_branch1()
    #p_w2 = para.winter_branch2()
    #p_w3 = para.winter_branch3f()


    #p_sp1 = para.spring_branch1()
    #p_sp2 = para.spring_branch2()

    #p_su1 = para.summer_branch1()
    #p_su2 = para.summer_branch2()
    #p_su3 = para.summer_branch3()
    #p_su4 = para.summer_branch4()


    #winter
    #export_edges(p_w1, "winter_branch_1.ply")
    #export_edges(p_w2, "winter_branch_2.ply")
    #export_edges(p_w3, "winter_branch_3.ply")


    #spring
    #export_edges(p_sp1, "spring_branch_1.ply")
    #export_edges(p_sp2, "spring_branch_2.ply")


    #summer
    #export_edges(p_su1, "summer_branch_1.ply")
    #export_edges(p_su2, "summer_branch_2.ply")
    #export_edges(p_su3, "summer_branch_3.ply")
    #export_edges(p_su4, "summer_branch_4.ply")

    #le = para.leanne_branch()
    o = para.olivia_branch()
    #export_edges(le, "leanne_branch.ply")
    export_edges(o, "olivia_branch.ply")


if __name__=='__main__':
    main()