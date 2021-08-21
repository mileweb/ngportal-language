# NG Portal Language Files
This repository is the [Git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) of 
[NG Portal](https://github.com/mileweb/ngportal) implementing i18n in portal UI. 
## Documents:  
We need to make sure the main keywords are translated consistently according to this table:
| English | Chinese | Korean | Japanese | Russian | French |
| --- | --- | --- | --- | --- | --- |
| property |
| property | 加速项 | 설정 | プロパティ | свойство | Configuration |
| edge configurations | 边缘配置 | 에지구성 | エッジ構成 | edge-конфигурация | Parametres |
| version | 版本 | 버전 | バージョン | версия | Version |
| hostname | 域名 | 호스트명 | ホスト名 | имя хоста | Nom d'hôte |
| report | 报表 | 리포트 | レポート | отчет | Rapport |
| report interval | 报表粒度 | 리포트 간격 | レポートの粒度 | интервал отчета | Delai de rapport |
| origin | 源站 | 오리진 | オリジン | источник | Origine |
| certificate | 证书 | 인증서 | 証明書 | сертификат | Certificat |
| action | 操作 | 액션 | アクション | действие | Action |
| edge logic | 边缘逻辑 | 엣지 로직  | エッジロジック | скрипт | Script server |
| deploy |
| staging | 演练 | 가상 환경 | ステージング | стейджинг | Platforme de test |
| production | 生产 | 실제 환경 | プロダクション | продуктив | Production |
| environment | 环境 | 환경 | 実環境 | окружение  | Environement |
| deploy | 发布 | 적용 | 適用 | развернуть | Deployé |
| undeploy | 卸载 | 비적용 | 非適用 | откатить | Non déployé |
| edge hostname |
| edge hostname | 边缘域名 | 에지호스트명 | エッジ　ホスト名 | имя edge-хоста | Nom d'hôte |
| client zone | 访客分区 | 클라이언트 지역 | クライアントゾーン | регион клиента | Région client |
| rule | 规则 | 룰 | ルール | правило | Regle |
| deliver | 分发 | 서비스 | 配信 | доставить | Delivré |
| reject | 拒绝 | 거부 | 拒否 | отклонить | Rejeté |
| redirect | 跳转 | 리다이렉트 | リダイレクト | перенаправить | Redirection |
| purge | 刷新 | 비우기 | パージ | отчиска | Purger |
| prefetch | 预取 | 미리가져오기 | プリフェッチ | пердварительная загрузка | Préchauffer |
| Secret |
| secret | 保密信息 | 비밀 | 秘密情報 | секрет | Secret |
| Account |
| impersonate | 身份切换 |  |  | Выдавать себя за другое лицо |  |

## Naming Convention
* ar_SA.json: Arabic (Saudi Arabia)
* en_US.json: English (United States)
* es_ES.json: Spanish (Spain)
* fr_FR.json: French (France)
* it_IT.json: Italian (Italy)
* jk_KR.json: Korean (Korea)
* jp_JP.json: Japanese (Japan)
* ru_RU.json: Russian (Russia)
* zh-Hans.json: Simplified Chinese (China)
## How It Works
NG portal used [React Intl](https://www.npmjs.com/package/react-intl) to support internationalization by loading
the JSON file corresponding to the language chosen by the customer. Texts are stored in key-value pairs in these JSON
files, for example "Start Purge" or "开始刷新" in Chinese are sharing the same key "purge.button.start". Developers can
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
{"purge.button.start": "开始刷新"}
```
## Useful Tools
[BabelEdit](https://www.codeandweb.com/babeledit) is a translation editor for web applications. It enables developers to edit JSON properties and translation files with ease. We have a Volume License. Please ask Bin Ni for the license key.

This project should only be worked on with this tool.

Before you commit, please do a `git diff` to make sure you did not inadvertantely change the line order, indentation, line-end etc. Only the lines you actually modified should show up in the diff. Otherwise it will be very difficult to track changes.
