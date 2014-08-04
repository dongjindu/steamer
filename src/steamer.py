# Copyright (c) 2014, Yetaai
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

__author__="Yetaai"
__date__ ="$Aug 4, 2014 12:33:54 AM$"

if __name__ == "__main__":
    print "Hello World"

def wire000(lx, ly, lz,  radius, thickness, bottomthickness=3.0, base=FreeCAD.Vector(0, 0, 0), axis=FreeCAD.Vector(0, 0, 1), angle=360, diff = 0.00001):
	import FreeCAD
	from FreeCAD import Base
	import Part
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

def wire001(lx, ly, lz,  radius, thickness, bottomthickness=3.0, base=FreeCAD.Vector(0, 0, 0), axis=FreeCAD.Vector(0, 0, 1), angle=360, diff = 0.00001, )
	pt300 = FreeCAD.Vector(base.x + lx - 1.5 * thickness, base.base.y + ly/2.0 - smallhalf, base.z)
	
	
import FreeCAD
import Sketcher
import Draft
import Part
from FreeCAD import Base
App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")
kk = wire000(60.0, 100.0, 100.0, 8.0, 6.0, 0)
App.ActiveDocument.addObject("Part::Feature", "sh0")
App.ActiveDocument.getObject("sh0").Shape = kk
Gui.SendMsgToActiveView("ViewFit")
#App.ActiveDocument.addObject("Part::Feature", "face1")
#App.ActiveDocument.getObject("face1").Shape = f1
#Gui.ActiveDocument.getObject("face1").ShapeColor = (321., 121., 300.)
#Gui.SendMsgToActiveView("ViewFit")

