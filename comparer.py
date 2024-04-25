www = {'ia100':'world', 'tui3':'fjfj', '9090909':'end', '10':'end', 'ia2':'im here', '0':'hello', 'mmc':[{'ddd':['efjuerhfg','klkl']}, 'jkkjk']}
www2 = {'ia100':'world', 'tui3':'fjfj', '9090909':'end', '10':'end', '0':'hello', 'ia2':'im here', 'mmc':[{'ddd':['klkl', 'efjuerhfg']}, 'jkkjk']}
words = {}
# for x in www.keys():
new_www= []
def check_dicts(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        if sorted(dict1.keys()) != sorted(dict2.keys()):
            return False
        for key in dict1.keys():
            if not check_dicts(dict1[key], dict2[key]):
                return False
        return True
    elif isinstance(dict1, list) and isinstance(dict2, list):
        if len(dict1) != len(dict2):
            return False
        for item1, item2 in zip(dict1, dict2):
            if not check_dicts(item1, item2):
                return False
        return True
    else:
        return True
print(check_dicts(www, www2))        