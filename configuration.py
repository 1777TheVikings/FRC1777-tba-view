import xml.etree.ElementTree as ElementTree


_tree = ElementTree.parse("config.xml")
_root = _tree.getroot()

X_TBA_AUTH_KEY = _root.find("AuthKey")
TEAM_KEY = _root.find("TeamKey")
MATCH_KEY = _root.find("MatchKey")
TEAM_LOGO_FILE = _root.find("TeamLogo")
