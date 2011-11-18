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
    def create(self, name, label, tooltip, psd, guid, hybrid_uploader_url):
        self.label = label
        self.tooltip = tooltip
        self.hybrid_uploader_url = hybrid_uploader_url
        self.s_guid = "{"+guid+"}"
        self.id = self._slugged(name)+"/{"+guid+"}"
        t_icon = self.id+".psd"
        t_xml = self.id+".pbf"

        f_xml = cStringIO.StringIO()
        f_xml.write(self._pbf_xml())

        f_button = cStringIO.StringIO()
        wrapper = cStringIO.StringIO()

        button = zipfile.ZipFile(f_button, mode='w')
        wrapper = codecs.getwriter("utf8")(f_button)
        button.writestr(t_icon, psd.read())
        button.writestr(t_xml, f_xml.getvalue())
        f_xml.close()
        button.close()
        f_button.flush()
        return f_button

    def create_for_buttonmodel(self, model):
        button = self.create(
            model.name,
            model.label,
            model.tooltip,
            model.icon,
            model.guid,
            model.hybrid_uploader_url,
        )
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

