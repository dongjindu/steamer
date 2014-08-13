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
	ry = lx * smallradius
	rz = lx * smallradius
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
	#cylinderX1.scale(1.001)
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
	ry = lx * smallradius
	rz = lx * smallradius
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
	sl1 = 2.0
	sl2 = 1.6 * sl1
	sl3 = 1.0
	smallbox = Part.makeBox(sl2, ly, sl1, FreeCAD.Vector(base.x + ((lx - sl1) / 2.0), base.y, base.z + rz + 0.5), FreeCAD.Vector(0, 0, 1))
	shape1 = shape1.cut(smallbox)
	#sht1 = Part.makeTorus()
	#sht2 = Part.makeTorus()
	#sht3 = Part.makeTorus()
	#sht4 = Part.makeTorus()
	#shcy1 = Part.makeCyliner()
	#shh1 = Part.makeHelix()
	#shh1.Placement = FreeCAD.Placement()
	return shape1

def wire000(lx, ly, lz,  radius, thickness, bottomthickness=3.0, base=FreeCAD.Vector(0, 0, 0), axis=FreeCAD.Vector(0, 0, 1), angle=360, diff = 0.00001):
	import FreeCAD
	from FreeCAD import Base
	import Part
	import Sketcher
	import Draft
	ax = FreeCAD.Vector(1, 0, 0)
	ay = FreeCAD.Vector(0, 1, 0)
	az = FreeCAD.Vector(0, 0, 1)
	halfthickness = thickness / 2.0
	#Points of sides
	pt000 = FreeCAD.Vector( base.x + lx - halfthickness, base.y + thickness, base.z + radius) #Inner square corner of left up close b
	pt001 = FreeCAD.Vector( base.x + lx - halfthickness, base.y,  base.z + radius)
	pt002 = FreeCAD.Vector( base.x + radius, base.y, base.z + radius)
	pt003 = FreeCAD.Vector( base.x, base.y + radius, base.z + radius) #bottom point
	pt004 = FreeCAD.Vector( base.x + thickness, base.y + radius, base.z + radius) #Start of bottom inner circle
	pt005 = FreeCAD.Vector( base.x + radius, base.y + thickness, base.z + radius)
	ptcorner = FreeCAD.Vector( base.x + radius, base.y + radius, base.z + radius)
	#Points of Internal corners
	pt100 = FreeCAD.Vector( base.x + radius, base.y, base.z + radius)
	pt101 = FreeCAD.Vector( base.x + radius, base.y, base.z + lz - radius)
	pt102 = FreeCAD.Vector( base.x + radius, base.y + radius, base.z + lz)
	pt103 = FreeCAD.Vector( base.x + radius, base.y + ly - radius, base.z + lz)
	pt104 = FreeCAD.Vector( base.x + radius, base.y + ly, base.z + lz - radius)
	pt105 = FreeCAD.Vector( base.x + radius, base.y + ly, base.z + radius)
	pt106 = FreeCAD.Vector( base.x + radius, base.y + ly - radius, base.z)
	pt107 = FreeCAD.Vector( base.x + radius, base.y + radius, base.z)
	pt200 = FreeCAD.Vector( base.x + radius, base.y + radius, base.z + radius)
	pt201 = FreeCAD.Vector( base.x + radius, base.y + radius, base.z + lz - radius)
	pt202 = FreeCAD.Vector( base.x + radius, base.y + ly - radius, base.z + lz - radius)
	pt203 = FreeCAD.Vector( base.x + radius, base.y + ly - radius, base.z + radius)
	ptcenter = FreeCAD.Vector( base.x + lx - halfthickness, base.y + halfthickness, base.z + radius)
	place000 = FreeCAD.Placement(ptcenter, ax, 0)
	l000 = Part.makeCircle(halfthickness, ptcenter, az, 270, 90) #Arc
	l001 = Part.makeLine(pt001, pt002)
	place002 = FreeCAD.Placement(ptcorner, ax, 0)
	l002 = Part.makeCircle(radius, ptcorner, az, 180, 270) #Arc
	l003 = Part.makeLine(pt003, pt004)
	place004 = FreeCAD.Placement(ptcorner, ax, 0)
	l004 = Part.makeCircle(radius - thickness, ptcorner, az, 180, 270) #Arc
	l005 = Part.makeLine(pt005, pt000)
	lines000 = [l000, l001, l002, l003, l004, l005]
	wire000 = Part.Wire(lines000)
	wire000
	face000 = Part.Face(wire000)
	face000a = face000.mirror(FreeCAD.Vector(0, 0, base.z + lz/2.0), FreeCAD.Vector(0, 0, 1))
	face001 = face000a.mirror(FreeCAD.Vector(base.x + radius, base.y + radius, base.z + lz - radius), FreeCAD.Vector(0, 1, 1))
	face001a = face001.mirror(FreeCAD.Vector(0, base.y + ly/2.0, 0), FreeCAD.Vector(0, 1, 0))
	face002 = face001a.mirror(FreeCAD.Vector(0, base.y + ly/2.0, base.z + lz/2), FreeCAD.Vector(0, 1, -1))
	face002a = face002.mirror(FreeCAD.Vector(0, 0, base.z + lz/2.0), FreeCAD.Vector(0, 0, 1))
	face003 = face002a.mirror(FreeCAD.Vector(base.x + radius, base.y + radius, base.z + lz - radius), FreeCAD.Vector(0, 1, 1))
	face003a = face003.mirror(FreeCAD.Vector(0, base.y + ly/2.0, 0), FreeCAD.Vector(0, 1, 0))
	face000a.nullify()
	face001a.nullify()
	face002a.nullify()
	face003a.nullify()
	#sk0 = Draft.makeSketch(lines000)
	#l100 = Part.makeLine(pt100, pt101)
	#l101 = Part.makeCircle(radius, pt201, ax, 90, 180)
	#l102 = Part.makeLine(pt102, pt103)
	#l103 = Part.makeCircle(radius, pt202, ax, 0, 90)
	#l104 = Part.makeLine(pt104, pt105)
	#l105 = Part.makeCircle(radius, pt203, ax, 270, 360)
	#l106 = Part.makeLine(pt106, pt107)
	#l107 = Part.makeCircle(radius, pt200, ax, 180, 270)
	#Part.show(l100)
	#Part.show(l101)
	#Part.show(l102)
	#Part.show(l103)
	#Part.show(l104)
	#Part.show(l105)
	#Part.show(l106)
	#Part.show(l107)
	#lines001 = [l100, l101, l102, l103, l104, l105, l106, l107]
	#wire001 = Part.Wire(lines001)
	s0 = face000.extrude(Base.Vector(0, 0, lz - 2.0 * radius))
	s0.scale(1.001)
	s1 = face001.extrude(Base.Vector(0, ly - 2.0 * radius, 0))
	s1.scale(1.001)
	s0 = s0.fuse(s1)
	s1.nullify()
	s2 = face002.extrude(Base.Vector(0, 0, 2.0 * radius - lz))
	s2.scale(1.001)
	s0 = s0.fuse(s2)
	s2.nullify()
	s3 = face003.extrude(Base.Vector(0, 2.0 * radius - ly, 0))
	s3.scale(1.001)
	s0 = s0.fuse(s3)
	s3.nullify()
	s4 = face000.revolve(pt200, ax, 90)
	s0 = s0.fuse(s4)
	s4.nullify()
	s5 = face001.revolve(pt201, ax, 90)
	s5.scale(1.001)
	s0 = s0.fuse(s5)
	s5.nullify()
	s6 = face002.revolve(pt202, ax, 90)
	s6.scale(1.001)
	s0 = s0.fuse(s6)
	s6.nullify()
	s7 = face003.revolve(pt203, ax, 90)
	s7.scale(1.001)
	s0 = s0.fuse(s7)
	s7.nullify()
	sbottom = Part.makeBox(thickness + bottomthickness, ly - 2 * radius, lz - 2 * radius, Base.Vector(base.x - bottomthickness, base.y + radius, base.z + radius), az)
	s0 = s0.fuse(sbottom)
	#return sk1
	return s0

#def wire001(lx, ly, lz,  radius, thickness, bottomthickness=3.0, base=FreeCAD.Vector(0, 0, 0), axis=FreeCAD.Vector(0, 0, 1), angle=360, diff = 0.00001, ):
#	pt300 = FreeCAD.Vector(base.x + lx - 1.5 * thickness, base.base.y + ly/2.0 - smallhalf, base.z)
	
#                    w     l     t     ku   kd   ot   r1   r2   r3   rd    place(base, rotation by axis and angle, center point)
#	sbase1 = wire002(12.0, 11.0, 2.50, 1.0, 1.0, 0.0, 2.8, 2.0, 1.8, 11.2, FreeCAD.Placement(FreeCAD.Vector(80, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
def wire002(width, length, thickness, keyupthickness, keydownthickness, otherthickness, r1, r2, r3, rd, place=FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 0.0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0, 0, 0))):
	import FreeCAD
	from FreeCAD import Base
	import Part
	import Sketcher
	import Draft
	#The whole base.
	#rd is the distance from base place to the center of key
	#r1 is the radius of the cylinder part of the hole
	#r2 is the radius of the upper part farrest end. Here it is equal to r3
	#r3 is the radius of the lower part farrest end
	#the end of description of function
	propup = 2.0
	propdown = 1.1
	bx = place.Base.x
	by = place.Base.y
	bz = place.Base.z
	#shape of main base box
	if r2 == 0.0:
		r2 = r3
	s0 = Part.makeBox(width, length, thickness, place.Base, place.Rotation.Axis)
	#shape of half cylinder of base
	bx1 = bx + (width/2.0)
	by1 = by
	bz1 = bz
	place1 = place
	place1.Base.x = bx1
	bx2 = bx1
	by2 = by1 + length
	bz2 = bz1
	place2 = place1
	place2.Base.y = by2
	s1 = Part.makeCylinder((width / 2.0), thickness, place2.Base, place2.Rotation.Axis, 360)
	s0 = s0.fuse(s1)
	s1.nullify()
	#shape of the cylinder of the hole which is to be cut from the base
	place3 = place
	bx3 = bx1 
	by3 = by + rd
	bz3 = bz1
	place3.Base.x = bx3
	place3.Base.y = by3
	s2 = Part.makeCylinder(r1, thickness, place3.Base, place3.Rotation.Axis, 360)
	s0 = s0.cut(s2)
	#Shpae of the box of the hole which to be cut from the base and from which the lower part can go through to its position
	place4 = place3
	bx4 = bx3 - r3
	by4 = by3 - r1 - propdown * r3
	bz4 = bz3
	place4.Base.x = bx4
	place4.Base.y = by4
	s3 = Part.makeBox(2.0 * r3, r1 + propdown * r3, thickness, place4.Base, place4.Rotation.Axis)
	s0 = s0.cut(s3)
	#Shpae of the half cylinder of the hole which to be cut at farest
	place5 = place3
	bx5 = bx3
	by5 = by3 - r1 - propdown * r3
	bz5 = bz3
	place5.Base.x = bx5
	place5.Base.y = by5
	place5.Base.z = bz5
	s4 = Part.makeCylinder(r3, thickness, place5.Base, place5.Rotation.Axis, 360)
	s0 = s0.cut(s4)
	return s0

def wire002a(width, length, thickness, keyupthickness, keydownthickness, otherthickness, r1, r2, r3, rd, place=FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 0.0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0, 0, 0))):
	import FreeCAD
	from FreeCAD import Base
	import Part
	import Sketcher
	import Draft
	#The key. But the parameters are designed for the base primarily. The parameter of the key has to be derived from them.
	#rd is the distance from base place to the center of key
	#r1 is the radius of the cylinder part of the hole
	#r2 is the radius of the upper part farrest end
	#r3 is the radius of the lower part farrest end
	#otherthickness is not used right now.
	#The end of description of the funciton.
	#prefix processing to get the initial position.
	propup = 1.6
	propdown = 1.1
	bx = place.Base.x
	by = place.Base.y
	bz = place.Base.z
	place1 = place
	bx1 = bx + (width /2.0)
	by1 = by
	bz1 = bz
	place1.Base.x = bx1
	place1.Base.y = by1
	place1.Base.z = bz1
	if r2 == 0.0:
		r2 = r3
	#shape of the cylinder of the key
	place2 = place1
	bx2 = bx1
	by2 = by1 + rd
	bz2 = bz1 - keydownthickness
	place2.Base.x = bx2
	place2.Base.y = by2
	place2.Base.z = bz2
	s1 = Part.makeCylinder(r1 * 0.999, thickness + keyupthickness + keydownthickness, place2.Base, place2.Rotation.Axis, 360)
	#shape of the box of the bottom part of the key
	place3 = place2
	bx3 = bx2 - r3
	by3 = by2 - r1 - propdown * r3
	bz3 = bz2
	place3.Base.x = bx3
	place3.Base.y = by3
	place3.Base.z = bz3
	s2 = Part.makeBox(2.0 * 0.999 * r3, r1 + propdown * r3, keydownthickness, place3.Base, place3.Rotation.Axis)
	#shape of the half cylinder of the bottom part of the key
	place4 = place2
	bx4 = bx2
	by4 = by2 - r1 - propdown * r3 
	bz4 = bz2
	place4.Base.x = bx4
	place4.Base.y = by4
	place4.Base.z = bz4
	s3 = Part.makeCylinder(r3 * 0.999, keydownthickness, place4.Base, place4.Rotation.Axis, 360)
	#shape of the box of the upper part of the key
	place5 = place2
	bx5 = bx2 - r2
	by5 = by2 - r1 - r2 * propup 
	bz5 = bz2 + keydownthickness + thickness
	place5.Base.x = bx5
	place5.Base.y = by5
	place5.Base.z = bz5
	s4 = Part.makeBox(2.0 * r2 * 0.999, r1 * 0.999 + propup * r2 * 0.999, keyupthickness, place5.Base, place5.Rotation.Axis)
	#shpae of the half cylinder of the upper part of the key
	place6 = place2
	bx6 = bx2
	by6 = by2 - r1 - r2 * propup
	bz6 = bz2 + thickness + keydownthickness
	place6.Base.x = bx6
	place6.Base.y = by6
	place6.Base.z = bz6
	s5 = Part.makeCylinder(r2 * 0.999, keyupthickness, place6.Base, place6.Rotation.Axis, 360)
	s0 = s1
	s0 = s0.fuse(s2)
	s0 = s0.fuse(s3)
	s0 = s0.fuse(s4)
	s0 = s0.fuse(s5)
	return s0

def wire003(lx, ly, lz,  radius, thickness, bottomthickness=3.0, base=FreeCAD.Vector(0, 0, 0), axis=FreeCAD.Vector(0, 0, 1), angle=360, diff = 0.00001):
	from random import randint
	#makeplatform
	redundancy = 0.6
	thicknessplat = 0.3
	####Important parameters which are key parameters as well
	keybaselength = 11.0 + 12.0 / 2.0 #10.0 is length of keybase. It is also the diameter of cylinder of keybase. 12.0 is width of keybase
	keybasewidth = 12.0
	propup = 1.6
	propdown = 1.1
	rd = 11.2
	r1 = 2.8 #Radius of cylinder Part of the key hole
	r2 = 2.0 #Upper part of the key which must be able to go through the hole of the plat
	####End of important parameter which are key parameters as well
	basex = base.x
	basey = base.y
	basez = base.z
	p000 = base
	bx000 = basex + thickness + redundancy
	by000 = basey + thickness + redundancy
	bz000 = basez
	p000.x = bx000
	p000.y = by000
	p000.z = bz000
	#Main platform body
	s0 = Part.makeBox(lx - 2.0 * thickness - redundancy * 2.0, ly - 2.0 * thickness - 2.0 * redundancy, thicknessplat, p000, axis)
	#Round corner
	rincornercut = 1.5 * ( radius - thickness - redundancy )
	#print 'rincornercut:', rincornercut 
	rincornerfuse = radius - thickness - redundancy
	pin000x = basex + radius
	pin000y = basey + radius
	pin000z = basez
	pin000 = FreeCAD.Vector(pin000x, pin000y, pin000z)
	scornercut0 = Part.makeCylinder(rincornercut, thicknessplat, pin000, FreeCAD.Vector(0, 0, 1), 90)
	scornercut0.rotate(pin000, FreeCAD.Vector(0, 0, 1), 180)
	s0 = s0.cut(scornercut0)
	scornerfuse0 = Part.makeCylinder(rincornerfuse, thicknessplat, pin000, FreeCAD.Vector(0, 0, 1), 90)
	scornerfuse0.rotate(pin000, FreeCAD.Vector(0, 0, 1), 180)
	s0 = s0.fuse(scornerfuse0)
	scornercut0.nullify
	scornerfuse0.nullify
	pin001x = basex + lx - radius
	pin001y = basey + radius
	pin001z = basez
	pin001 = FreeCAD.Vector(pin001x, pin001y, pin001z)
	scornercut1 = Part.makeCylinder(rincornercut, thicknessplat, pin001, FreeCAD.Vector(0, 0, 1), 90)
	scornercut1.rotate(pin001, FreeCAD.Vector(0, 0, 1), 270)
	s0 = s0.cut(scornercut1)
	scornerfuse1 = Part.makeCylinder(rincornerfuse, thicknessplat, pin001, FreeCAD.Vector(0, 0, 1), 90)
	scornerfuse1.rotate(pin001, FreeCAD.Vector(0, 0, 1), 270)
	s0 = s0.fuse(scornerfuse1)
	scornercut1.nullify
	scornerfuse1.nullify
	pin002x = basex + lx - radius
	pin002y = basey + ly - radius
	pin002z = basez
	pin002 = FreeCAD.Vector(pin002x, pin002y, pin002z)
	scornercut2 = Part.makeCylinder(rincornercut, thicknessplat, pin002, FreeCAD.Vector(0, 0, 1), 90)
	#scornercut2.rotate(pin002, FreeCAD.Vector(0, 0, 1), 360)
	s0 = s0.cut(scornercut2)
	scornerfuse2 = Part.makeCylinder(rincornerfuse, thicknessplat, pin002, FreeCAD.Vector(0, 0, 1), 90)
	#scornerfuse2.rotate(pin002, FreeCAD.Vector(0, 0, 1), 360)
	s0 = s0.fuse(scornerfuse2)
	scornercut2.nullify
	scornerfuse2.nullify
	pin003x = basex + radius
	pin003y = basey + ly - radius
	pin003z = basez
	pin003 = FreeCAD.Vector(pin003x, pin003y, pin003z)
	scornercut3 = Part.makeCylinder(rincornercut, thicknessplat, pin003, FreeCAD.Vector(0, 0, 1), 90)
	scornercut3.rotate(pin003, FreeCAD.Vector(0, 0, 1), 90)
	s0 = s0.cut(scornercut3)
	scornerfuse3 = Part.makeCylinder(rincornerfuse, thicknessplat, pin003, FreeCAD.Vector(0, 0, 1), 90)
	scornerfuse3.rotate(pin003, FreeCAD.Vector(0, 0, 1), 90)
	s0 = s0.fuse(scornerfuse3)
	scornercut3.nullify
	scornerfuse3.nullify
	#Start of key hole punching
	keyprop1 = 0.28
	keyprop2 = 1.0 - keyprop1
	keyhole0x = basex + keyprop1 * lx 
	keyhole0y = basey + thickness + rd - r2 * propup - r1
	keyhole1x = basex + keyprop2 * lx
	keyhole1y = basey + thickness + rd - r2 * propup - r1
	keyhole2x = basex + keyprop1 * lx
	keyhole2y = basey + ly - thickness - rd
	keyhole3x = basex + keyprop2 * lx
	keyhole3y = basey + ly - thickness - rd
	skeyhole0box = Part.makeBox(2.0 * r2, r1 + propup * r2, thicknessplat, FreeCAD.Vector(keyhole0x - r2, keyhole0y, bz000))
	skeyhole0cy1 = Part.makeCylinder(r1, thicknessplat, FreeCAD.Vector(keyhole0x, basey + thickness + rd, bz000), FreeCAD.Vector(0, 0, 1), 360)
	skeyhole0cy2 = Part.makeCylinder(r2, thicknessplat, FreeCAD.Vector(keyhole0x, keyhole0y, bz000), FreeCAD.Vector(0, 0, 1), 360)
	s0 = s0.cut(skeyhole0box)
	s0 = s0.cut(skeyhole0cy1)
	s0 = s0.cut(skeyhole0cy2)
	skeyhole0box.nullify
	skeyhole0cy1.nullify
	skeyhole0cy2.nullify
	skeyhole1box = Part.makeBox(2.0 * r2, r1 + propup * r2, thicknessplat, FreeCAD.Vector(keyhole1x - r2, keyhole1y, bz000))
	skeyhole1cy1 = Part.makeCylinder(r1, thicknessplat, FreeCAD.Vector(keyhole1x, basey + thickness + rd, bz000), FreeCAD.Vector(0, 0, 1), 360)
	skeyhole1cy2 = Part.makeCylinder(r2, thicknessplat, FreeCAD.Vector(keyhole1x, keyhole1y, bz000), FreeCAD.Vector(0, 0, 1), 360)
	s0 = s0.cut(skeyhole1box)
	s0 = s0.cut(skeyhole1cy1)
	s0 = s0.cut(skeyhole1cy2)
	skeyhole1box.nullify
	skeyhole1cy1.nullify
	skeyhole1cy2.nullify
	skeyhole2box = Part.makeBox(2.0 * r2, r1 + propup * r2, thicknessplat, FreeCAD.Vector(keyhole2x - r2, keyhole2y, bz000))
	skeyhole2cy1 = Part.makeCylinder(r1, thicknessplat, FreeCAD.Vector(keyhole2x, keyhole2y, bz000), FreeCAD.Vector(0, 0, 1), 360)
	skeyhole2cy2 = Part.makeCylinder(r2, thicknessplat, FreeCAD.Vector(keyhole2x, keyhole2y + propup * r2 + r1, bz000), FreeCAD.Vector(0, 0, 1), 360)
	s0 = s0.cut(skeyhole2box)
	s0 = s0.cut(skeyhole2cy1)
	s0 = s0.cut(skeyhole2cy2)
	skeyhole2box.nullify
	skeyhole2cy1.nullify
	skeyhole2cy2.nullify
	skeyhole3box = Part.makeBox(2.0 * r2, r1 + propup * r2, thicknessplat, FreeCAD.Vector(keyhole3x - r2, keyhole3y, bz000))
	skeyhole3cy1 = Part.makeCylinder(r1, thicknessplat, FreeCAD.Vector(keyhole3x, keyhole3y, bz000), FreeCAD.Vector(0, 0, 1), 360)
	skeyhole3cy2 = Part.makeCylinder(r2, thicknessplat, FreeCAD.Vector(keyhole3x, keyhole3y + propup * r2 + r1, bz000), FreeCAD.Vector(0, 0, 1), 360)
	s0 = s0.cut(skeyhole3box)
	s0 = s0.cut(skeyhole3cy1)
	s0 = s0.cut(skeyhole3cy2)
	skeyhole3box.nullify
	skeyhole3cy1.nullify
	skeyhole3cy2.nullify
	#End of key hole punching
	#Steam hole 
	i0 = 0
	i1 = 0
	i2 = 0
	ix = 0
	iy = 0
	rhole = 1.6
	holedistancey = 3.8 * rhole
	holedistancex = 3.8 * rhole
	holerimy = 3.0 * rhole
	holerimx = 3.0 * rhole
	cholex = bx000 + holerimx # + (randint(1,5) - 3.0) / 10.0 # Beginning offset
	choley = by000 + holerimy
	cholez = bz000
	limit0x0 = keyhole0x - keybasewidth / 2.0
	limit0x1 = keyhole0x + keybasewidth / 2.0
	limit0y0 = by000
	limit0y1 = by000 + keybaselength
	limit1x0 = keyhole1x - keybasewidth / 2.0
	limit1x1 = keyhole1x + keybasewidth / 2.0
	limit1y0 = by000
	limit1y1 = by000 + keybaselength
	limit2x0 = keyhole2x - keybasewidth / 2.0
	limit2x1 = keyhole2x + keybasewidth / 2.0
	limit2y0 = basey + ly - keybaselength - thickness
	limit2y1 = basey + ly - thickness
	limit3x0 = keyhole3x - keybasewidth / 2.0
	limit3x1 = keyhole3x + keybasewidth / 2.0
	limit3y0 = basey + ly - keybaselength - thickness
	limit3y1 = basey + ly - thickness
	while True:
		i1 = i1 + 1
		#if (cholex > (bx000 + lx - 2.0 * thickness - 2.0 * redundancy - rhole * 1.2)) and (choley > (by000 + ly - 2.0 * thickness - 2.0 * redundancy - rhole * 1.2)):
		if ( choley > (basey + ly - thickness - redundancy - holerimy) )or ( i1 > 1000 ):
			#i0 = 1
			break
		elif (cholex > (basex + lx - thickness - redundancy - holerimx)) and (choley <= (basey + ly - thickness - redundancy - holerimy)):
			ix = 0
			iy = iy + 1
			cholex = bx000 + holerimx 
			choley = choley + holedistancey
			if (choley > (basey + ly - thickness - redundancy - holerimy)): #Late processing to prevent y exceeds boundary
				continue
		elif (cholex <= (basex + lx - thickness - redundancy - holerimx)) and (choley <= (basey + ly - thickness - redundancy - holerimy)):
			ix = ix + 1
			if ix > 1:
				cholex = cholex + holedistancex
			if (cholex > basex + lx - thickness - redundancy - holerimx): #Late processing to prevent x exceeds boundary
				continue
		else:
			print 'what happen', ix, iy
		#Don't make hole if falling in restriction area
		if (     cholex > limit0x0 and cholex < limit0x1 and choley > limit0y0 and choley < limit0y1) \
			or ( cholex > limit1x0 and cholex < limit1x1 and choley > limit1y0 and choley < limit1y1) \
			or ( cholex > limit2x0 and cholex < limit2x1 and choley > limit2y0 and choley < limit2y1) \
			or ( cholex > limit3x0 and cholex < limit3x1 and choley > limit3y0 and choley < limit3y1):
			#print 'cholex:', cholex, ', choley:', choley,
			#print limit0x0, limit0x1, lim0t0y0, limit0y1
			#print limit1x0, limit1x1, lim0t1y0, limit1y1
			#print limit2x0, limit2x1, lim0t2y0, limit2y1
			#print limit3x0, limit3x1, lim0t3y0, limit3y1
			continue
		#Make a hole finally
		else:
			i2 = i2 + 1
			#shole = Part.makeCylinder(rhole, thicknessplat, FreeCAD.Vector(cholex + ((randint(1, 5) - 3.0)/ 10), choley + ((randint(1, 5) - 3.0) / 10), bz000), FreeCAD.Vector(0, 0, 1), 360)
			#s0 = s0.cut(shole)
			#shole.nullify
	#print 'Total columns of y(first x then y):', iy
	#print 'Total loops: ',  i1
	#print 'Total holes: ',  i2
	#print 'basex: ', basex
	#print 'bx000: ', bx000
	#print 'p000:', p000
	#print 'biggest x: ', basex + lx - thickness - redundancy - holerimx
	return s0

#                   w     l     t   ku   kd   ot   r1   r2   r3    rd    place(base, rotation by axis and angle, center point)
#sbase1 = wire002(18.0, 18.0, 2.50, 1.0, 1.0, 0.0, 3.0, 2.0, 1.8, 19.1, FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
#skey1 = wire002a(18.0, 18.0, 2.50, 1.0, 1.0, 0.0, 3.0, 2.0, 1.8, 19.1, FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
#skey2 = wire002a(18.0, 18.0, 2.50, 1.0, 1.0, 0.0, 3.0, 2.0, 1.8, 19.1, FreeCAD.Placement(FreeCAD.Vector(0, 0, 8), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
#skey3 = wire002a(18.0, 18.0, 2.50, 1.0, 1.0, 0.0, 3.0, 2.0, 1.8, 19.1, FreeCAD.Placement(FreeCAD.Vector(0, 0, -10), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
	
def assemble001(width, length, thickness, keyupthickness, keydownthickness, otherthickness, r1, r2, r3, rd, place=FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 0.0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0, 0, 0))):
	import FreeCAD
	from FreeCAD import Base
	import Part
	import Sketcher
	import Draft
	lx = 60
	ly = 100
	lz = 100
	redundancy = 0.6
	thicknessplat = 0.3
	#             lx    ly     lz    rad    thick   bottomthickness, base, axis, angle, diff
	s0 = wire000(60.0, 100.0, 100.0, 6.0,   3.0,     0)
	s0.rotate(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 1, 0), 270)
	App.ActiveDocument.addObject("Part::Feature", "sbarrel1")
	App.ActiveDocument.getObject("sbarrel1").Shape = s0
	#sbase1 = wire002(width, length, thickness, keyupthickness, keydownthickness, otherthickness, r1, r2, r3, rd, place=FreeCAD.Placement(FreeCAD.Vector(80.0, 0.0, 0.0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0, 0, 0)))
	#skey1 = wire002a(width, length, thickness, keyupthickness, keydownthickness, otherthickness, r1, r2, r3, rd, place=FreeCAD.Placement(FreeCAD.Vector(80.0, 0.0, 0.0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0, 0, 0)))
	sbase1 = wire002(12.0, 11.0, 2.50, 1.0, 1.0, 0.0, 2.8, 2.0, 1.8, 11.2, FreeCAD.Placement(FreeCAD.Vector(110.0, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
	skey1 = wire002a(12.0, 11.0, 2.50, 1.0, 1.0, 0.0, 2.8, 2.0, 1.8, 11.2, FreeCAD.Placement(FreeCAD.Vector(128.0, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
	sbase2 = wire002(12.0, 11.0, 2.50, 1.0, 1.0, 0.0, 2.8, 2.0, 1.8, 11.2, FreeCAD.Placement(FreeCAD.Vector(140.0, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
	skey2 = wire002a(12.0, 11.0, 2.50, 1.0, 1.0, 0.0, 2.8, 2.0, 1.8, 11.2, FreeCAD.Placement(FreeCAD.Vector(158.0, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
	#sbase3p = wire002(12.0, 11.0, 2.50, 1.0, 1.0, 0.0, 2.8, 2.0, 1.8, 11.2, FreeCAD.Placement(FreeCAD.Vector(170, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
	#skey3p = wire002a(12.0, 11.0, 2.50, 1.0, 1.0, 0.0, 2.8, 2.0, 1.8, 11.2, FreeCAD.Placement(FreeCAD.Vector(188, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
	#sbase4p = wire002(12.0, 11.0, 2.50, 1.0, 1.0, 0.0, 2.8, 2.0, 1.8, 11.2, FreeCAD.Placement(FreeCAD.Vector(200, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
	#skey4p = wire002a(12.0, 11.0, 2.50, 1.0, 1.0, 0.0, 2.8, 2.0, 1.8, 11.2, FreeCAD.Placement(FreeCAD.Vector(212, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
	splat1 = wire003(100.0, 100.0, 100.0, 6.0,   3.0,     0.0)
	deltaz = 30.0
	splat1.translate(FreeCAD.Vector(0.0 - ly + thickness + redundancy, 0.0, deltaz + thickness))
	sbase1.translate(FreeCAD.Vector(0.0 - 110.0 - ly + thickness + redundancy + 0.28 * ly - 6.0, thickness + redundancy, deltaz))
	sbase2.translate(FreeCAD.Vector(0.0 - 140.0 - ly + thickness + redundancy + 0.72 * ly - 6.0, thickness + redundancy, deltaz))
	sbase3 = sbase1.mirror(FreeCAD.Vector(0.0, 0.0 + ly / 2.0, 0.0), FreeCAD.Vector(0, 1, 0)) #sbase3p.mirror(FreeCAD.Vector(0, (length/2.0 + width /4.0),0), FreeCAD.Vector(0, 1, 0))
	sbase4 = sbase2.mirror(FreeCAD.Vector(0.0, 0.0 + ly / 2.0, 0.0), FreeCAD.Vector(0, 1, 0)) #sbase3.translate(FreeCAD.Vector(0 - ly + thickness + redundancy + 0.28 * ly, ly - thickness - redundancy, deltaz))
	#sbase4 = sbase4p.mirror(FreeCAD.Vector(0, (length/2.0 + width /4.0),0), FreeCAD.Vector(0, 1, 0))
	#sbase4.translate(FreeCAD.Vector(0 - ly + thickness + redundancy + 0.72 * ly, ly - thickness - redundancy, deltaz))
	skey1.translate(FreeCAD.Vector(0.0 - ly + thickness + redundancy + 0.28 * ly - 128.0 - 6.0, thickness + redundancy, deltaz))
	skey2.translate(FreeCAD.Vector(0.0 - ly + thickness + redundancy + 0.72 * ly - 158.0 - 6.0, thickness + redundancy, deltaz))
	skey3 = skey1.mirror(FreeCAD.Vector(0.0, ly / 2.0, 0.0), FreeCAD.Vector(0, 1, 0))#skey3 = skey3p.mirror(FreeCAD.Vector(0, (length/2.0 + width /4.0),0), FreeCAD.Vector(0, 1, 0))
	#skey3.translate(FreeCAD.Vector(0 - ly + thickness + redundancy + 0.28 * ly, ly - thickness - redundancy, deltaz))
	skey4 = skey2.mirror(FreeCAD.Vector(0.0, ly / 2.0, 0.0), FreeCAD.Vector(0, 1, 0))#skey4 = skey4p.mirror(FreeCAD.Vector(0, (length/2.0 + width /4.0),0), FreeCAD.Vector(0, 1, 0))
	#skey4.translate(FreeCAD.Vector(0 - ly + thickness + redundancy + 0.72 * ly, ly - thickness - redundancy, deltaz))
	App.ActiveDocument.addObject("Part::Feature", "shbase1")
	App.ActiveDocument.getObject("shbase1").Shape = sbase1
	App.ActiveDocument.addObject("Part::Feature", "shkey1")
	App.ActiveDocument.getObject("shkey1").Shape = skey1
	App.ActiveDocument.addObject("Part::Feature", "shbase2")
	App.ActiveDocument.getObject("shbase2").Shape = sbase2
	App.ActiveDocument.addObject("Part::Feature", "shkey2")
	App.ActiveDocument.getObject("shkey2").Shape = skey2
	App.ActiveDocument.addObject("Part::Feature", "shbase3")
	App.ActiveDocument.getObject("shbase3").Shape = sbase3
	App.ActiveDocument.addObject("Part::Feature", "shkey3")
	App.ActiveDocument.getObject("shkey3").Shape = skey3
	App.ActiveDocument.addObject("Part::Feature", "shbase4")
	App.ActiveDocument.getObject("shbase4").Shape = sbase4
	App.ActiveDocument.addObject("Part::Feature", "shkey4")
	App.ActiveDocument.getObject("shkey4").Shape = skey4
	App.ActiveDocument.addObject("Part::Feature", "shplat1")
	App.ActiveDocument.getObject("shplat1").Shape = splat1

	#####################Barrel creation old method
	#sh1 = newRoundBox1(30.0, 10.0, 12.0, 0.1, FreeCAD.Vector(20, 20, 0))
	#sh2 = newRoundBox2(sh1, 30.0, 10.0, 12.0, 0.1, FreeCAD.Vector(20, 20, 0))
	#App.ActiveDocument.addObject("Part::Feature", "osh2")
	#App.ActiveDocument.getObject("osh2").Shape = sh2
	#Gui.SendMsgToActiveView("ViewFit")

App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")
assemble001(12.0, 11.0, 2.50, 1.0, 1.0, 0.0, 2.8, 2.0, 1.8, 11.2, FreeCAD.Placement(FreeCAD.Vector(80, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0.0, 0.0, 1.0), 360), FreeCAD.Vector(0.0, 0.0, 0.0)))
#r1 is 3.0 which is the center hole of the key
