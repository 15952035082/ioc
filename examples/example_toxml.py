import json

from ioc_writer.toxml_api import TOXML
"""
    Generate xml file from a json string
    Don't care about letter case of 'type',
"""


items = [{"type": "IP", "content": "190.85.21.244"},
         {"type": "DNS", "content": "header.id"},
         {"type": "SHA1", "content": "696d616765732f7964774e657761726b2e6a7067"},
         {"type": "Email", "content": "jesus@el-perdedor.eu"},
         {"type": "URI", "content": "http://allisonbessblog.com/7Bsf4bSOgI/"},
         ]

json_str = json.dumps(items)
print(TOXML(json_str).write_to_xml())
