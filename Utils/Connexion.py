import psycopg2
import xml.etree.ElementTree as ET

def enterBdd():
    
    #tree = ET.parse('../config.xml')
    #root = tree.getroot()
    user_name = "fabien"
    pass_word = "fabien"
    hosting = "localhost"
    specified_port = "5432"
    base = "bddspaciale"
    
    # for database in root.iter('database'):
    #     user_name = database.find('username').text
    #     pass_word = database.find('password').text
    #     hosting = database.find('host').text
    #     specified_port = database.find('port').text
    #     base = database.find('base').text
    try:
        conn = psycopg2.connect(
            user = user_name, 
            password = pass_word,
            host = hosting,  
            port = specified_port,
            database = base 
        )                       
        return conn;
    except (Exception, psycopg2.Error) as error :
        return None
