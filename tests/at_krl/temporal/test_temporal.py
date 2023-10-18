from xml.etree.ElementTree import tostring, fromstring

from at_krl.core.temporal.kb_allen_operation import KBEvent, KBInterval, KBAllenOperation


def test_event_interval():
    interval_xml = fromstring("""<Interval Name="Положительный_интервал_13064720_0">
            <Open>
                <LogOp Value="AND">
                    <EqOp Value="eq">
                        <Attribute Value="Таймер.такт" />
                        <Number Value="1" />
                    </EqOp>
                    <EqOp Value="ge">
                        <Attribute Value="Главный_объект.температура" />
                        <Number Value="300" />
                    </EqOp>
                </LogOp>
            </Open>
            <Close>
                <EqOp Value="eq">
                    <Attribute Value="Таймер.такт" />
                    <Number Value="2" />
                </EqOp>
            </Close>
        </Interval>""")
    
    interval = KBInterval.from_xml(interval_xml)
    print(interval.krl)
    print(tostring(interval.xml, encoding='unicode'))
    int2 = KBInterval.from_xml(interval.xml)
    print('')
    print(tostring(int2.xml, encoding='unicode'))

    event_xml = fromstring("""<Event Name="Текущий_такт_0">
            <Formula>
                <EqOp Value="eq">
                    <Attribute Value="Таймер.такт" />
                    <Number Value="0" />
                </EqOp>
            </Formula>
        </Event>""")
    event = KBEvent.from_xml(event_xml)

    print(event.krl)
    print(tostring(event.xml, encoding='unicode'))

    ev2 = KBEvent.from_xml(event.xml)
    print()
    print(tostring(ev2.xml, encoding='unicode'))

    operation = KBAllenOperation('d', event, interval)
    print()
    print(operation.krl)
    print()
    print(tostring(operation.xml, encoding='unicode'))
    op2 = KBAllenOperation.from_xml(operation.xml)
    op2.validate_tag([event], [interval])
    print()
    print(op2.krl)
    print()
    print(tostring(op2.xml, encoding='unicode'))

    op3 = KBAllenOperation('d', event.id, interval.id)
    print(op3.krl)
    op3.get_tag_by_events_and_intervals(events=[event], intervals=[interval])
    print(op3)
    
    