from typing import Iterable, List, Union
from xml.etree.ElementTree import Element
from at_krl.core.kb_entity import KBEntity

class MFPoint(KBEntity):
    x: float|int = None
    y: float|int = None

    def __init__(self, x: float|int, y: float|int):
        self.tag = 'point'
        self.x = x
        self.y = y

    @property
    def attrs(self) -> dict:
        return dict(
            x=str(self.x), y=str(self.y),
            **super().attrs
        )
    
    @property
    def krl(self) -> str:
        return f"{self.x}|{self.y}"
    
    def __dict__(self) -> dict:
        return dict(x=self.x, y=self.y, **(super().__dict__()))
    
    @staticmethod
    def from_xml(xml: Element) -> 'MFPoint':
        return MFPoint(x=xml.attrib.get('x'), y=xml.attrib.get('y'))
    
    @staticmethod
    def from_dict(d: dict) -> 'MFPoint':
        return MFPoint(x=d.get('x'), y=d.get('y'))


class MembershipFunction(KBEntity):
    points: List[MFPoint] | Iterable[MFPoint] = None
    name: str = None
    min: float = None
    max: float = None

    def __init__(self, name: str, min: float, max: float, points: List[MFPoint] | Iterable[MFPoint]):
        self.tag = 'parameter'
        self.name = name
        self.min = min
        self.max = max
        self.points = points
        for point in self.points:
            point.owner = self

    @property
    def attrs(self) -> dict:
        res = super().attrs
        res['min-value'] = str(self.min)
        res['max-value'] = str(self.max)
        return res
    
    @property
    def inner_xml(self) -> List[Element] | Iterable[Element]:
        value = Element('value')
        value.text = self.name
        mf = Element('mf')
        for point in self.points:
            mf.append(point.xml)
        return [value, mf]
    
    def __dict__(self) -> dict:
        res = super().__dict__()
        res['name'] = self.name
        res['min'] = self.min
        res['max'] = self.max
        res['points'] = [p.__dict__() for p in self.points]
        return res
    
    @staticmethod
    def from_xml(xml: Element) -> 'MembershipFunction':
        min = xml.attrib.get('min-value')
        max = xml.attrib.get('max-value')
        
        name = xml.find('value').text
        mf = xml.find('mf')
        points = [MFPoint.from_xml(p) for p in mf]

        return MembershipFunction(name, min, max, points)
    
    @staticmethod
    def from_dict(d: dict) -> 'MembershipFunction':
        return MembershipFunction(
            d.get('name'),
            d.get('min'),
            d.get('max'),
            points=[MFPoint.from_dict(p) for p in d.get('points')]
        )
    
    @property
    def krl(self) -> str:
        points_krl = '={' + "; ".join([p.krl for p in self.points]) +  '}'
        return f'"{self.name}" {self.min} {self.max} {len(self.points)} {points_krl}'