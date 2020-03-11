import json
import os
from collections import OrderedDict

# Main language = English US
main_lang = 'en_US'
# Other languages to support
lang_list = ['ar_SA', 'es_ES', 'fr_FR', 'it_IT', 'jk_KR', 'jp_JP', 'zh-Hans']
result_path = 'result'

# Create export path
try:
    os.mkdir(result_path)
except FileExistsError:
    print("Result path already exists.")
    exit()

# Read English JSON file
with open(main_lang + '.json') as f:
    main_json = json.load(f)

# Auto generate key-value pairs for other languages
for lang_name in lang_list:
    print("Processing: " + lang_name + '...')
    with open(lang_name + '.json') as rf:
        lang_json = json.load(rf)
    result_dict = OrderedDict()
    for key in main_json:
        if key in lang_json:
            result_dict[key] = lang_json[key]
        else:
            result_dict[key] = main_json[key]
    with open(result_path + '/' + lang_name + '.json', 'w') as outfile:
        json.dump(result_dict, outfile, indent=2, ensure_ascii=False)
print("Finished!")
print("Locale language files generated in \"" + result_path + "\" path.")
