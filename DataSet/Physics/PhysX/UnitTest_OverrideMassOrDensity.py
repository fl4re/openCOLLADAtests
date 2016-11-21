from Core.Common.DOMParser import *
from Core.FColladaTest import FColladaTest
from numpy import *
from xml.dom.minidom import *


def GetChildrenElementsByTagName(element, tag):
    result = []
    for child in element.childNodes:
        if child.nodeType == Node.ELEMENT_NODE and child.tagName == tag:
            result.append(child)
    return result


def GetChildElementByTagName(element, tag):
    for child in element.childNodes:
        if child.nodeType == Node.ELEMENT_NODE and child.tagName == tag:
            return child
    return None


def GetElementValue(element):
    if len(element.childNodes) is not 1:
        return None
    if element.firstChild.nodeType is not Node.TEXT_NODE:
        return None
    return element.firstChild.nodeValue


def ParseFloat(string):
    try:
        tmp = float(string)
    except ValueError:
        return None
    return float(string)


def GetRigidBodyMass(rb):
    tc = GetChildElementByTagName(rb, 'technique_common')
    assert (tc is not None)
    mass = GetChildElementByTagName(tc, 'mass')
    if mass is None:
        return None
    mass = ParseFloat(GetElementValue(mass))
    assert (mass is not None)
    return mass


def GetShape(rb):
    tc = GetChildElementByTagName(rb, 'technique_common')
    assert (tc is not None)
    shape = GetChildElementByTagName(tc, 'shape')
    assert (shape is not None)
    return shape


def GetShapeMass(shape):
    mass = GetChildElementByTagName(shape, 'mass')
    if mass is None:
        return None
    mass = ParseFloat(GetElementValue(mass))
    assert (mass is not None)
    return mass


def GetShapeDensity(shape):
    density = GetChildElementByTagName(shape, 'density')
    if density is None:
        return None
    density = ParseFloat(GetElementValue(density))
    assert (density is not None)
    return density


class Test_OverrideMassOrDensity:
    def test_override_mass_or_density(self):
        rbs = FColladaTest.GetRoot().getElementsByTagName('rigid_body')
        assert (len(rbs) == 4)

        rb1 = rbs[0]
        rb2 = rbs[1]
        rb3 = rbs[2]
        rb4 = rbs[3]

        mass = GetRigidBodyMass(rb1)
        assert (mass is None)
        shape = GetShape(rb1)
        mass = GetShapeMass(shape)
        assert (mass is None)
        density = GetShapeDensity(shape)
        assert (density is not None)
        assert (isclose(density, 1000))

        mass = GetRigidBodyMass(rb2)
        assert (mass is not None)
        assert (isclose(mass, 2000))
        shape = GetShape(rb2)
        mass = GetShapeMass(shape)
        assert (mass is None)
        density = GetShapeDensity(shape)
        assert (density is not None)
        assert (isclose(density, 1000))

        mass = GetRigidBodyMass(rb3)
        assert (mass is not None)
        assert (isclose(mass, 3000, atol=1))
        shape = GetShape(rb3)
        mass = GetShapeMass(shape)
        assert (mass is None)
        density = GetShapeDensity(shape)
        assert (density is not None)
        assert (isclose(density, 1000))

        mass = GetRigidBodyMass(rb4)
        assert (mass is None)
        shape = GetShape(rb4)
        mass = GetShapeMass(shape)
        assert (mass is not None)
        assert (isclose(mass, 4000))
        density = GetShapeDensity(shape)
        assert (density is None)
