#########################################################
# Name: config_reader_yaml
# Desc: A YAML configuration file reader. Given a simple
# config file convert it into a usable python dict.
# Usesful for ommitting senstive data from source 
# control.
#########################################################
def config_reader_yaml(path):
    import yaml
    with open(path) as config_file:
        data = yaml.load(config_file, Loader=yaml.FullLoader)
        
        #print(data)
        #print(data["username"])

#########################################################
# Name: config_reader_yaml
# Desc: A YAML configuration file reader. Given a simple
# config file convert it into a usable python dict.
# Usesful for ommitting senstive data from source 
# control.
#########################################################
def config_reader_json(path):
    import json
    with open(path) as config_file:
        data = json.load(config_file)
        
        #print(data)
        #print(data["username"])


### Example Use Case ###
#config_reader_yaml("./test.yaml")
#config_reader_json("./test.json")

