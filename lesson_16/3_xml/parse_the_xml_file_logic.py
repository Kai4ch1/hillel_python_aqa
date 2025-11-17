import definitions
import xml.etree.ElementTree as ET
import logging
logging.basicConfig(
    filename='xml_parse.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)
logger = logging.getLogger("LOG EVENT")
xml_file_storage = definitions.XML_FILES_STORAGE
file_to_parse = xml_file_storage / "groups.xml"


def parse_the_xml(xml_file, searching_number):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for group in root.findall("group"):
        current_group_number = group.find("number")
        exbytes = group.find("timingExbytes")
        if exbytes is not None and searching_number == current_group_number.text:
            incoming = exbytes.find("incoming")
            logger.info(f"LOGGED SUCCESSFULLY searching_number,incoming.text, searching number ={searching_number}, exbyte={incoming.text}")
            return f"The number is: {searching_number}, and incoming byte is: {incoming.text}"
    else:
        return f"Group Not Found: searching number = {searching_number}"


if __name__ == '__main__':
    print(parse_the_xml(file_to_parse, "2"))