# -*- coding: utf-8 -*-
import xmltodict, json
import os
import sys
import codecs

Files = []
def Test2(rootDir): 
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        Files.append(path)
        if os.path.isdir(path): 
            Test2(path)

result = {}
if __name__ == '__main__':
    Test2("source")
    for file in Files:
        input_file = codecs.open(file, "r", "utf8")
        text = input_file.read()
        o = xmltodict.parse(text)
        source = json.loads(json.dumps(o))
        index = 1
        for item in source["wordbook"]["item"]:
            tag = item["tags"]
            if tag not in result:
                result[tag] = []
            tmp_result = result[tag]
#             print ([item["word"], item["trans"], item["phonetic"]])
            line = "\n".join([str(index) + " : " + str(item["word"]), str(item["phonetic"]), str(item["trans"])])
            print (line)
            tmp_result.append(line)
            result[tag] = tmp_result
            index += 1
        input_file.close()
    
    for file_name, lines in result.items():
        output_file = codecs.open("output/%s.txt" % file_name, "w", "utf8")
        output_file.write("\n\n".join(lines))
        output_file.close()