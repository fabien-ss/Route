import xml.etree.ElementTree as ET

tree = ET.parse('config.xml')
root = tree.getroot()

for database in root.iter('database'):
    user_name = database.find('username').text
    pass_word = database.find('password').text
    host_ = database.find('host').text
    port_ = database.find('port').text
    base_ = database.find('base').text
    print(user_name + " " + pass_word)