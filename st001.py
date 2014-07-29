def newRoundBox1(lx, ly, lz,  smallradius, base=FreeCAD.Vector(0, 0, 0), axis=FreeCAD.Vector(0, 0, 1), angle=360):
	import Part
	import FreeCAD
	from FreeCAD import Base
	vec00 = base
	vec01 = FreeCAD.Vector(base.x + lx, base.y, base.z)
	vec02 = FreeCAD.Vector(base.x + lx, base.y + ly, base.z)
	vec03 = FreeCAD.Vector(base.x, base.y + ly, base.z)
	vec10 = FreeCAD.Vector(base.x, base.y, base.z + lz)
	vec11 = FreeCAD.Vector(base.x + lx, base.y, base.z + lz)
	vec12 = FreeCAD.Vector(base.x + lx, base.y + ly, base.z + lz)
	vec13 = FreeCAD.Vector(base.x, base.y + ly, base.z + lz)
	vecx = FreeCAD.Vector(1, 0, 0)
	vecxn = FreeCAD.Vector(-1, 0, 0)
	vecy = FreeCAD.Vector(0, 1, 0)
	vecyn = FreeCAD.Vector(0, -1, 0)
	vecz = FreeCAD.Vector(0, 0, 1)
	veczn = FreeCAD.Vector(0, 0, -1)
	b001 = Part.makeBox(lx, ly, lz)
	placement1 = FreeCAD.Placement(base, axis, angle)
	b001.Placement = placement1
	#### Not blank, to cut corner using cylinder	
	rx = lx * smallradius
	ry = ly * smallradius
	rz = lz * smallradius
	cylinderX1 = Part.makeCylinder(rx, lx, vec00, vecx, angle)
	cylinderX2 = Part.makeCylinder(rx, lx, vec03, vecx, angle)
	cylinderY1 = Part.makeCylinder(ry, ly, vec00, vecy, angle)
	cylinderY2 = Part.makeCylinder(ry, ly, vec01, vecy, angle)
	cylinderZ1 = Part.makeCylinder(rz, lz, vec00, vecz, angle)
	cylinderZ2 = Part.makeCylinder(rz, lz, vec01, vecz, angle)
	cylinderZ3 = Part.makeCylinder(rz, lz, vec02, vecz, angle)
	cylinderZ4 = Part.makeCylinder(rz, lz, vec03, vecz, angle)
	b001 = b001.cut(cylinderX1)
	b001 = b001.cut(cylinderX2)
	b001 = b001.cut(cylinderY1)
	b001 = b001.cut(cylinderY2)
	b001 = b001.cut(cylinderZ1)
	b001 = b001.cut(cylinderZ2)
	b001 = b001.cut(cylinderZ3)
	b001 = b001.cut(cylinderZ4)
	#### Not blank
	vec00i = FreeCAD.Vector(base.x + rx, base.y + ry , base.z + rz)   #i means internal
	vec01i = FreeCAD.Vector(base.x + lx - rx, base.y + ry, base.z + rz)
	vec02i = FreeCAD.Vector(base.x + lx - rx, base.y + ly - ry, base.z + rz)
	vec03i = FreeCAD.Vector(base.x + rx, base.y + ly -ry, base.z + rz)
	vec10i = FreeCAD.Vector(base.x + rx, base.y + ry, base.z + rz)
	vec11i = FreeCAD.Vector(base.x + lx - rx, base.y + ry, base.z + rz)
	vec12i = FreeCAD.Vector(base.x + lx - rx, base.y + ly - ry, base.z + rz)
	vec13i = FreeCAD.Vector(base.x + rx, base.y + ly - ry, base.z + rz)
	#### Not blank
	dx = 2 * rx
	dy = 2 * ry
	dz = 2 * rz
	cylinderX1 = Part.makeCylinder(rx, lx - dx, vec00i, vecx, angle)
	cylinderX2 = Part.makeCylinder(rx, lx - dx, vec02i, vecxn, angle)
	cylinderY1 = Part.makeCylinder(ry, ly - dy, vec01i, vecy, angle)
	cylinderY2 = Part.makeCylinder(ry, ly - dy, vec03i, vecyn, angle)
	cylinderZ1 = Part.makeCylinder(rz, lz - rz, vec10i, vecz, angle)
	cylinderZ2 = Part.makeCylinder(rz, lz - rz, vec11i, vecz, angle)
	cylinderZ3 = Part.makeCylinder(rz, lz - rz, vec12i, vecz, angle)
	cylinderZ4 = Part.makeCylinder(rz, lz - rz, vec13i, vecz, angle)
	b001 = b001.fuse(cylinderX1)
	b001 = b001.fuse(cylinderX2)
	b001 = b001.fuse(cylinderY1)
	b001 = b001.fuse(cylinderY2)
	b001 = b001.fuse(cylinderZ1)
	b001 = b001.fuse(cylinderZ2)
	b001 = b001.fuse(cylinderZ3)
	b001 = b001.fuse(cylinderZ4)
	return b001
	
def newRoundBox2(shape, lx, ly, lz,  smallradius, base=FreeCAD.Vector(0, 0, 0), axis=FreeCAD.Vector(0, 0, 1), angle=360, diff=0.00001):
	import Part
	import FreeCAD
	from FreeCAD import Base
	rx = lx * smallradius
	ry = ly * smallradius
	rz = lz * smallradius
	vec00i = FreeCAD.Vector(base.x + rx, base.y + ry , base.z + rz)   #i means internal
	vec01i = FreeCAD.Vector(base.x + lx - rx, base.y + ry, base.z + rz)
	vec02i = FreeCAD.Vector(base.x + lx - rx, base.y + ly - ry, base.z + rz)
	vec03i = FreeCAD.Vector(base.x + rx, base.y + ly - ry, base.z + rz)
	sphere001 = Part.makeSphere( rx,  vec00i )
	sphere002 = Part.makeSphere( rx,  vec01i )
	sphere003 = Part.makeSphere( rx )
	sphere003.Placement = FreeCAD.Placement(FreeCAD.Vector(base.x + lx - rx - diff, base.y + ly -ry - diff, base.z + rz + diff), FreeCAD.Vector(0, 1, 0), 0) 
	sphere004 = Part.makeSphere( rx,  vec03i )
	shape1 = shape.fuse( sphere001 )
	shape1 = shape1.fuse( sphere002 )
	shape1 = shape1.fuse( sphere003 )
	shape1 = shape1.fuse( sphere004 )
	return shape1

sh1 = newRoundBox1(100, 100, 100, 0.1)
sh2 = newRoundBox2(sh1, 100, 100, 100, 0.1)
import Part
App.ActiveDocument.addObject("Part::Feature", "osh2")
App.ActiveDocument.getObject("osh2").Shape = sh2
