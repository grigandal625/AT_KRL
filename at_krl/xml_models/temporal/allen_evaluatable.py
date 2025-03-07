from at_krl.xml_models.simple.simple_evaluatable import SimpleEvaluatableLegacyXMLModel
from at_krl.xml_models.simple.simple_evaluatable import SimpleEvaluatableXMLModel


class AllenEvaluatableXMLModel(SimpleEvaluatableXMLModel):
    pass


class AllenEvaluatableLegacyXMLModel(SimpleEvaluatableLegacyXMLModel):
    pass


# из-за проблем с циклическими импортами, модели для
# AllenReference, AllenAttributeExpression и AllenOperation находятся в kb_operation
