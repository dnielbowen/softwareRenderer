import util

# Shitty, non-robust STL parser that works for well-formed models
def parseSTL(stlFilename):
    v = []
    f = []
    with open(stlFilename) as fp:
        for line in fp:
            words = line.strip().split()
            if words[0].lower() == 'vertex':
                vert = util.Vertex(
                    float(words[1]), float(words[2]), float(words[3]),
                    util.randomColor())
                v.append(vert)
                #print("v(%d %d %d) i=%d" % (vert.x, vert.y, vert.z, len(v)-1))
            elif words[0].lower() == 'endfacet':
                n = len(v)
                f.append((n-1, n-2, n-3))
                #print("f %d %d %d" % f[-1])
    print("Read %d vertices and %d faces" % (len(v), len(f)))
    return v,f
