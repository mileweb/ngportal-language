# NG Portal Language Files
This repository is the [Git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) of 
[NG Portal](https://github.com/mileweb/ngportal) implementing i18n in portal UI. 
## Documents:  
* [i18n Proper Noun Lookup Table](https://docs.google.com/spreadsheets/d/1068zI3pqrDOeNGgDbvH6bWBMIQQ834xI_u7iVwmReiM/edit#gid=0)
## Naming Convention
* ar_SA.json: Arabic (Saudi Arabia)
* en_US.json: English (United States)
* es_ES.json: Spanish (Spain)
* fr_FR.json: French (France)
* it_IT.json: Italian (Italy)
* jk_KR.json: Korean (Korea)
* jp_JP.json: Japanese (Japan)
* zh-Hans.json: Simplified Chinese (China)
## How It Works
NG portal used [React Intl](https://www.npmjs.com/package/react-intl) to support internationalization by loading
the JSON file corresponding to the language chosen by the customer. Texts are stored in key-value pairs in these JSON
files, for example "Start Purge" or "开始 Purge" in Chinese are sharing the same key "purge.button.start". Developers can
conveniently load the text in their components:
```javascript
import {injectIntl} from "react-intl";
...
class myComponent extends React.Component {
    ...
    let text = this.props.intl.formatMessage({id: 'purge.button.start'});
    ...
    render = () => <div>{text}</div>
}
export default injectIntl(myComponent);
```
Translators just need to modify the text values corresponding to key "purge.button.start".  
en_US.json:
```json
{"purge.button.start": "Start Purge"}
```
zh-Hans.json:
```json
{"purge.button.start": "开始 Purge"}
```
## Useful Tools
[BabelEdit](https://www.codeandweb.com/babeledit) is a translation editor for web applications. It enables developers to edit JSON properties and translation files with ease. We have a Volume License. Please ask Bin Ni for the license key.

This project should only be worked on with this tool.

Before you commit, please do a `git diff` to make sure you did not inadvertantely change the line order, indentation, line-end etc. Only the lines you actually modified should show up in the diff. Otherwise it will be very difficult to track changes.
