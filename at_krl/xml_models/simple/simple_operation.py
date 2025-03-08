from typing import Literal
from typing import Union

from pydantic_xml import attr

from at_krl.core.simple.simple_operation import SimpleOperation
from at_krl.utils.context import Context
from at_krl.xml_models.kb_entity import KBEntityRootXMLModel
from at_krl.xml_models.simple.simple_evaluatable import SimpleEvaluatableLegacyXMLModel
from at_krl.xml_models.simple.simple_evaluatable import SimpleEvaluatableXMLModel
from at_krl.xml_models.simple.simple_reference import SimpleReferenceLegacyXMLModel
from at_krl.xml_models.simple.simple_reference import SimpleReferenceXMLModel
from at_krl.xml_models.simple.simple_value import SimpleBooleanValueLegacyXMLModel
from at_krl.xml_models.simple.simple_value import SimpleNumberValueLegacyXMLModel
from at_krl.xml_models.simple.simple_value import SimpleStringValueLegacyXMLModel
from at_krl.xml_models.simple.simple_value import SimpleValueXMLModel


class BinaryOperationXMLModel(SimpleEvaluatableXMLModel):
    left: Union[SimpleValueXMLModel, SimpleReferenceXMLModel, "AnyOperation"]
    right: Union[SimpleValueXMLModel, SimpleReferenceXMLModel, "AnyOperation"]

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["left"] = self.left.to_internal(context.create_child("left"))
        data["right"] = self.right.to_internal(context.create_child("right"))
        data["sign"] = self.__xml_tag__
        return data

    def build_target(self, data, context: Context):
        result = SimpleOperation(**data)
        return result


class UnaryOperationXMLModel(SimpleEvaluatableXMLModel):
    operand: Union[SimpleValueXMLModel, SimpleReferenceXMLModel, "AnyOperation"]

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["left"] = self.operand.to_internal(context.create_child("left"))
        data["sign"] = self.__xml_tag__
        data.pop("operand", None)
        return data

    def build_target(self, data, context: Context):
        result = SimpleOperation(**data)
        return result


class Eq(BinaryOperationXMLModel, tag="eq"):
    pass


class Gt(BinaryOperationXMLModel, tag="gt"):
    pass


class Ge(BinaryOperationXMLModel, tag="ge"):
    pass


class Lt(BinaryOperationXMLModel, tag="lt"):
    pass


class Le(BinaryOperationXMLModel, tag="le"):
    pass


class Ne(BinaryOperationXMLModel, tag="ne"):
    pass


class And(BinaryOperationXMLModel, tag="and"):
    pass


class Or(BinaryOperationXMLModel, tag="or"):
    pass


class Not(UnaryOperationXMLModel, tag="not"):
    pass


class Xor(BinaryOperationXMLModel, tag="xor"):
    pass


class Neg(UnaryOperationXMLModel, tag="neg"):
    pass


class Add(BinaryOperationXMLModel, tag="add"):
    pass


class Sub(BinaryOperationXMLModel, tag="sub"):
    pass


class Mul(BinaryOperationXMLModel, tag="mul"):
    pass


class Div(BinaryOperationXMLModel, tag="div"):
    pass


class Mod(BinaryOperationXMLModel, tag="mod"):
    pass


class Pow(BinaryOperationXMLModel, tag="pow"):
    pass


AnyOperation = Eq | Gt | Ge | Lt | Le | Ne | And | Or | Not | Xor | Neg | Add | Sub | Mul | Mod | Pow

BinaryOperationXMLModel.model_rebuild()
UnaryOperationXMLModel.model_rebuild()

Eq.model_rebuild()
Gt.model_rebuild()
Ge.model_rebuild()
Lt.model_rebuild()
Le.model_rebuild()
Ne.model_rebuild()
And.model_rebuild()
Or.model_rebuild()
Not.model_rebuild()
Xor.model_rebuild()
Neg.model_rebuild()
Add.model_rebuild()
Sub.model_rebuild()
Mul.model_rebuild()
Div.model_rebuild()
Mod.model_rebuild()
Pow.model_rebuild()


class SimpleEvaluatableRootXMLModel(KBEntityRootXMLModel):
    root: Union["AnyOperation", SimpleValueXMLModel, SimpleReferenceXMLModel]


SimpleEvaluatableRootXMLModel.model_rebuild()


class BinaryOperationLegacyXMLModel(SimpleEvaluatableLegacyXMLModel):
    sign: str = attr(name="Value")
    left: Union[
        SimpleStringValueLegacyXMLModel,
        SimpleBooleanValueLegacyXMLModel,
        SimpleNumberValueLegacyXMLModel,
        SimpleReferenceLegacyXMLModel,
        "AnyOperationLegacy",
    ]
    right: Union[
        SimpleStringValueLegacyXMLModel,
        SimpleBooleanValueLegacyXMLModel,
        SimpleNumberValueLegacyXMLModel,
        SimpleReferenceLegacyXMLModel,
        "AnyOperationLegacy",
    ]

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["left"] = self.left.to_internal(context.create_child("left"))
        data["right"] = self.right.to_internal(context.create_child("right"))
        return data

    def build_target(self, data, context: Context):
        result = SimpleOperation(**data)
        return result


class ArOp(BinaryOperationLegacyXMLModel, tag="ArOp"):
    sign: Literal[
        "+",
        "add",
        "ADD",
        "-",
        "sub",
        "SUB",
        "*",
        "mul",
        "MUL",
        "/",
        "div",
        "DIV",
        "%",
        "mod",
        "MOD",
        "^",
        "**",
        "pow",
        "POW",
    ] = attr(name="Value")


class LogOp(BinaryOperationLegacyXMLModel, tag="LogOp"):
    sign: Literal[
        "&",
        "&&",
        "and",
        "AND",
        "|",
        "||",
        "or",
        "OR",
        "xor",
        "XOR",
    ] = attr(name="Value")


class EqOp(BinaryOperationLegacyXMLModel, tag="EqOp"):
    sign: Literal[
        "=",
        "==",
        "eq",
        "EQ" ">",
        "gt",
        "GT",
        ">=",
        "ge",
        "GE",
        "<",
        "lt",
        "LT",
        "<=",
        "le",
        "LE",
        "<>",
        "!=",
        "ne",
        "NE",
    ] = attr(name="Value")


AnyOperationLegacy = ArOp | LogOp | EqOp

BinaryOperationLegacyXMLModel.model_rebuild()

ArOp.model_rebuild()
LogOp.model_rebuild()
EqOp.model_rebuild()


class SimpleEvaluatableLegacyRootXMLModel(KBEntityRootXMLModel):
    root: Union[
        "AnyOperationLegacy",
        SimpleReferenceLegacyXMLModel,
        SimpleNumberValueLegacyXMLModel,
        SimpleStringValueLegacyXMLModel,
        SimpleBooleanValueLegacyXMLModel,
    ]


SimpleEvaluatableLegacyRootXMLModel.model_rebuild()


if __name__ == "__main__":
    xml_data = """
    <SimpleEvaluatableRootXMLModel>
        <and>
            <or>
                <eq>
                    <ref id="obj">
                        <ref id="attr" />
                    </ref>
                    <value>10</value>
                </eq>
                <gt>
                    <ref id="obj">
                        <ref id="attr" />
                    </ref>
                    <value>15</value>
                </gt>
            </or>
            <not>
                <ge>
                    <pow>
                        <ref id="obj">
                            <ref id="attr2" />
                        </ref>
                        <value>2</value>
                    </pow>
                    <value>4</value>
                </ge>
            </not>
        </and>
    </SimpleEvaluatableRootXMLModel>
    """
    model = SimpleEvaluatableRootXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)).krl)

    xml_data = """
    <SimpleEvaluatableLegacyRootXMLModel>
        <LogOp Value="OR">
            <ArOp Value="+">
                <Number Value="5" />
                <Attribute Value="obj.attr" />
            </ArOp>
            <EqOp Value="eq">
                <Number Value="5" />
                <Attribute Value="obj.attr" />
            </EqOp>
        </LogOp>
    </SimpleEvaluatableLegacyRootXMLModel>
    """

    model = SimpleEvaluatableLegacyRootXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)).krl)
