## 📣Introduction
**Because every time I delete a third-party installed app under Mac, I cannot delete it manually. Therefore, I wrote a small tool to delete app dependencies, configurations, logs, and caches.**

## ✨Technology
**According to keywords, traverse the following folders**

```
'~/Library/Application Support',
'~/Library/Preferences/',
'~/Library/Caches/',
'~/Library/Logs/',
'~/Library/Application Support/CrashReporter/',
'~/Library/Saved Application State/',
'~/Library/LaunchAgents/',
'/Library/Caches',
'/Library/Logs',
'/Library/Preferences/',
'/Library/Application Support',
'/Applications',
'/private/var/db/receipts',
'/Library/StagedExtensions/Library/Extensions',
'/Library/StagedExtensions/Library/Application Support',
'/Library/Extensions/',
'~'
```

## 🔰Install
#### 1. Dependency install
```
pip install prettytable
pip install colorama
```
#### 2. Add bash script to env
```
$ vim /etc/profile
export PATH="$PATH:{maclean_path}"

$ source /etc/profile
```

## 📝Usage
#### 1. If you want to delete app
**Firstly finds app's full name with command: `ls -al /Applications`**     
```
......
drwxr-xr-x@  3 root     wheel    96  4 10  2020 Keynote.app
drwxr-xr-x@  3 root     wheel    96  2 23  2019 Launchpad.app
......
```
**Then input command: `maclean ShadowsocksX-NG.app`**

```
 $ maclean ShadowsocksX-NG.app                              
[+]Searches app Info.plist successfully
[+]Found the following results:
+----+--------------------------------------------------------------------------------+-------+
| ID |                                  Folder/File                                   |  Size |
+----+--------------------------------------------------------------------------------+-------+
| 0  |           /Users/test123/Library/Application Support/ShadowsocksX-NG           |  19MB |
| 1  |     /Users/test123/Library/Preferences/com.qiuyuzhou.ShadowsocksX-NG.plist     |   1KB |
| 2  |  /Users/test123/Library/LaunchAgents/com.qiuyuzhou.shadowsocksX-NG.http.plist  | 739B  |
| 3  | /Users/test123/Library/LaunchAgents/com.qiuyuzhou.shadowsocksX-NG.local.plist  |   1KB |
| 4  | /Users/test123/Library/LaunchAgents/com.qiuyuzhou.shadowsocksX-NG.kcptun.plist | 945B  |
| 5  |                  /Library/Application Support/ShadowsocksX-NG                  |  53KB |
| 6  |                       /Applications/ShadowsocksX-NG.app                        |  39MB |
| 7  |                        /Users/test123/.ShadowsocksX-NG                         | 549KB |
+----+--------------------------------------------------------------------------------+-------+
[+]Please confirm the deleted id (e.g.: 0 1 3 or all):all
[+]Your choices: all
[+]Successfully deleted: /Users/test123/Library/Application Support/ShadowsocksX-NG
[+]Successfully deleted: /Users/test123/Library/Preferences/com.qiuyuzhou.ShadowsocksX-NG.plist
[+]Successfully deleted: /Users/test123/Library/LaunchAgents/com.qiuyuzhou.shadowsocksX-NG.http.plist
[+]Successfully deleted: /Users/test123/Library/LaunchAgents/com.qiuyuzhou.shadowsocksX-NG.local.plist
[+]Successfully deleted: /Users/test123/Library/LaunchAgents/com.qiuyuzhou.shadowsocksX-NG.kcptun.plist
[+]Successfully deleted: /Library/Application Support/ShadowsocksX-NG
[+]Successfully deleted: /Applications/ShadowsocksX-NG.app
[+]Successfully deleted: /Users/test123/.ShadowsocksX-NG
[*]8 files cleaned
```
#### 2. If it's dependency, log, cache or someting others
**For example, I want to delete Samsung's portablessd: `maclean portablessd`**
```
$ maclean portablessd
[*]Searches app Info.plist failed, native input will be used
[+]Found the following results:
+----+--------------------------------------------------------------------------------------------+-------+
| ID |                                        Folder/File                                         |  Size |
+----+--------------------------------------------------------------------------------------------+-------+
| 0  | /Users/test123/Library/Saved Application State/com.samsung.portablessd.software.savedState |   2KB |
| 1  |         /Users/test123/Library/LaunchAgents/com.samsung.portablessdplus.mon.plist          | 529B  |
| 2  |            /private/var/db/receipts/com.samsung.portablessdplus.softwarepkg.bom            |  67KB |
| 3  |              /private/var/db/receipts/com.samsung.portablessd.driverXpkg.bom               |  35KB |
| 4  |               /private/var/db/receipts/com.samsung.portablessd.driverpkg.bom               |  35KB |
| 5  |           /private/var/db/receipts/com.samsung.portablessdplus.softwarepkg.plist           | 281B  |
| 6  |              /private/var/db/receipts/com.samsung.portablessd.driverpkg.plist              | 287B  |
| 7  |         /Library/StagedExtensions/Library/Extensions/SamsungPortableSSDDriver.kext         |  92KB |
| 8  |                     /Library/Extensions/SamsungPortableSSDDriver.kext                      |  92KB |
+----+--------------------------------------------------------------------------------------------+-------+
[+]Please confirm the deleted id (e.g.: 0 1 3 or all):all
[+]Your choices: all
[+]Successfully deleted: /Users/test123/Library/Saved Application State/com.samsung.portablessd.software.savedState
[+]Successfully deleted: /Users/test123/Library/LaunchAgents/com.samsung.portablessdplus.mon.plist
[+]Successfully deleted: /private/var/db/receipts/com.samsung.portablessdplus.softwarepkg.bom
[+]Successfully deleted: /private/var/db/receipts/com.samsung.portablessd.driverXpkg.bom
[+]Successfully deleted: /private/var/db/receipts/com.samsung.portablessd.driverpkg.bom
[+]Successfully deleted: /private/var/db/receipts/com.samsung.portablessdplus.softwarepkg.plist
[+]Successfully deleted: /private/var/db/receipts/com.samsung.portablessd.driverpkg.plist
[+]Successfully deleted: /Library/Extensions/SamsungPortableSSDDriver.kext
[*]8 files cleaned
```