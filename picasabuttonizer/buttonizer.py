import cStringIO
import zipfile
import codecs
from lxml import etree
from django.template.defaultfilters import slugify

class Buttonizer:

    id = None
    s_guid = None
    label = None
    tooltip = None
    hybrid_uploader_url = None

    def create(self, **kwargs):
        self.label = kwargs['label']
        self.tooltip = kwargs['tooltip']
        psd = kwargs['psd']
        self.id = self._slugged(kwargs['name'])+"/{"+kwargs['guid']+"}"

        f_xml = cStringIO.StringIO()
        f_xml.write(self._pbf_xml())

        f_button = cStringIO.StringIO()

        button = zipfile.ZipFile(f_button, mode='w')

        button.writestr(self.id+".psd", psd.read())
        button.writestr(self.id+".pbf", f_xml.getvalue())
        f_xml.close()
        button.close()
        f_button.flush()
        return f_button

    def create_for_buttonmodel(self, model):
        button = self.create(**model.__dict__)
        return self._button_name(model.name), button

    def _slugged(self, name):
        return slugify(name)

    def _button_name(self, name):
        return self._slugged(name)+".pbz"

    def _pbf_xml(self):
        buttons = etree.Element("buttons", format="1", version="0.1")
        button = etree.Element("button", id=self.id, type="dynamic")
        button.append(etree.Element("icon", name=self.s_guid+"/icon", src="pbz"))
        label = etree.Element("label")
        label.text = self.label
        button.append(label)
        action = etree.Element("action", verb="hybrid")
        action.append(etree.Element("param", name="url", value=self.hybrid_uploader_url))
        buttons.append(button)
        button.append(action)

        return etree.tostring(buttons, pretty_print=True, encoding="utf-8", xml_declaration=True)

