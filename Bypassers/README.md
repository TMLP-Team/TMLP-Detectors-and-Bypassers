## Bypassers

### Using Official Magisk or Magisk Alpha

- Install the latest Official [Magisk](https://github.com/LSPosed/LSPosed.github.io/releases/) or [Magisk Alpha](https://install.appcenter.ms/users/vvb2060/apps/magisk/distribution_groups/public)
  - Configure the Magisk
    - Enable Zygisk (or use [ZygiskNext](https://github.com/Dr-TSNG/ZygiskNext))
    - Disable Denylist
    - Empty Denylist
    - Launch the applications requiring root privileges like the MT Manager and grant root requests in Magisk
  - Install the [LSPosed](https://github.com/JingMatrix/LSPosed/actions) module (the Release version in the latest action in the ``Jing Matrix`` fork) in the Magisk layer
    - Reboot $\rightarrow$ Open the LSPosed Manager $\rightarrow$ Create the LSPosed parasite $\rightarrow$ Create a desktop shortcut to the LSPosed parasite $\rightarrow$ Disable the logs which could make LSPosed being detected and the LSPosed taskbar notification in the setting page of the LSPosed parasite $\rightarrow$ Uninstall the LSPosed Manager
    - Input ``*#*#5776733#*#*`` in the dialer (do not call) to open the LSPosed parasite if necessary (in case the desktop shortcut is missing)
    - Install the [HMAL](https://github.com/pumPCin/HMAL) plugin in the LSPosed layer
    - Set the target scope of the HMAL plugin to **System Framework** only and enable the HMAL plugin in the LSPosed Manager
    - Reboot the device
    - Configure the HMAL
      - Hide HMAL's icon from the launcher in the HMAL's settings page
      - Set the three switches in Data Isolation to ``On``, ``Off``, and ``On`` in sequence in the HMAL's settings page (may require root privileges)
      - Build appropriate whitelist (what applications the detectors can see) or blacklist (what applications the detectors cannot see) templates (can refer to [this tutorial](./HMAL/README.md))
      - Except for the Magisk Manager and the plugins, enable hiding for all user applications and system-pre-installed non-critical applications with suitable templates applied
  - Install the [Shamiko](https://github.com/LSPosed/LSPosed.github.io/releases/) module in the Magisk layer
    - Use the MT Manager to create an empty file named ``whitelist`` under ``/data/adb/shamiko/`` (or execute the command ``touch /data/adb/shamiko/whitelist`` as root)
    - Add the package names of the applications that are allowed to obtain root privileges to this file if necessary
  - Install the [Play Integrity FIx](https://github.com/chiteroman/PlayIntegrityFix) module in the Magisk layer
  - Install the [Tricky Store](https://github.com/5ec1cff/TrickyStore) module in the Magisk layer
    - Use the MT Manager to rename the ``keybox.xml`` file in the ``/data/adb/tricky_store/`` directory to ``keybox.xml.bak`` (``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``)
    - Search for a free recent ``keybox.xml`` in the Telegram channel [FreeKeyboxShare](https://t.me/FreeKeyboxShare) and use the MT Manager to move it to ``/data/adb/tricky_store/``
    - Use [Key Attestation](https://github.com/vvb2060/KeyAttestation) to check if it passes the Device (old Strong) integrity $\rightarrow$ Click ``/data/adb/tricky_store/keybox.xml.bak`` in the MT Manager and restore the backup if not
    - Please try to generate a ``keybox.xml`` that can pass the Basic (old Device) integrity via a Python script from [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) if the free ``keybox.xml`` does not work or the ``keybox.xml`` signed based on the root certificate from the AOSP is not wished to be used
    - Never buy a ``keybox.xml`` unless the seller guarantees to offer you a new valid one once the previous one is revoked since each ``keybox.xml`` will be revoked by Google in a short period usually
    - Use the MT Manager to extract the installation package names of the detectors (long press to copy) and add them to ``/data/adb/tricky_store/target.txt`` (blacklist mode)
    - Use the MT Manager to write the current date, the date of the 1st day of the current month, or the date of the first day of the second month of the last season to ``/data/adb/tricky_store/security_patch.txt`` in the form of ``20250201``
  - Install the [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) module in the Magisk layer if the device does not have a broken TEE
  - Install the [bindhosts](https://github.com/backslashxx/bindhosts) or the built-in ``Systemless hosts`` module in the Magisk layer
    - Please remove the other module if one is selected to be used since they are not compatible
    - After rebooting, click the "Action" button of this module one or more times in the Magisk Manager to make it display "reset" and then click the "Action" button again to apply the latest rules if using the bindhosts module

### Using Magisk Delta

- Install the lastest version of [Magisk Delta](https://github.com/HuskyDG/magisk-files) before it was discontinued
  - It can be out-of-date since it was discontinued in early 2024
  - Configure Magisk Delta
    - Enable Zygisk (or use [ZygiskNext](https://github.com/Dr-TSNG/ZygiskNext))
    - Enable whitelist mode on the setting page of the Magisk Delta
    - Select the package of the application that requires root privileges (you can only select the necessary packages in the applications)
  - Install the [LSPosed](https://github.com/JingMatrix/LSPosed/actions) module (the Release version in the latest action in the ``Jing Matrix`` fork) in the Magisk layer
    - Reboot $\rightarrow$ Open the LSPosed Manager $\rightarrow$ Create the LSPosed parasite $\rightarrow$ Create a desktop shortcut to the LSPosed parasite $\rightarrow$ Disable the logs which could make LSPosed being detected and the LSPosed taskbar notification in the setting page of the LSPosed parasite $\rightarrow$ Uninstall the LSPosed Manager
    - Input ``*#*#5776733#*#*`` in the dialer (do not call) to open the LSPosed parasite if necessary (in case the desktop shortcut is missing)
    - Install the [HMAL](https://github.com/pumPCin/HMAL) plugin in the LSPosed layer
    - Set the target scope of the HMAL plugin to **System Framework** only and enable the HMAL plugin in the LSPosed Manager
    - Reboot the device
    - Configure the HMAL
      - Hide HMAL's icon from the launcher in the HMAL's settings page
      - Set the three switches in Data Isolation to ``On``, ``Off``, and ``On`` in sequence in the HMAL's settings page (may require root privileges)
      - Build appropriate whitelist (what applications the detectors can see) or blacklist (what applications the detectors cannot see) templates (can refer to [this tutorial](./HMAL/README.md))
      - Except for the Magisk Manager and the plugins, enable hiding for all user applications and system-pre-installed non-critical applications with suitable templates applied
  - Install the [Play Integrity FIx](https://github.com/chiteroman/PlayIntegrityFix) module in the Magisk layer
  - Install the [Tricky Store](https://github.com/5ec1cff/TrickyStore) module in the Magisk layer
    - Use the MT Manager to rename the ``keybox.xml`` file in the ``/data/adb/tricky_store/`` directory to ``keybox.xml.bak`` (``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``)
    - Search for a free recent ``keybox.xml`` in the Telegram channel [FreeKeyboxShare](https://t.me/FreeKeyboxShare) and use the MT Manager to move it to ``/data/adb/tricky_store/``
    - Use [Key Attestation](https://github.com/vvb2060/KeyAttestation) to check if it passes the Device (old Strong) integrity $\rightarrow$ Click ``/data/adb/tricky_store/keybox.xml.bak`` in the MT Manager and restore the backup if not
    - Please try to generate a ``keybox.xml`` that can pass the Basic (old Device) integrity via a Python script from [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) if the free ``keybox.xml`` does not work or the ``keybox.xml`` signed based on the root certificate from the AOSP is not wished to be used
    - Never buy a ``keybox.xml`` unless the seller guarantees to offer you a new valid one once the previous one is revoked since each ``keybox.xml`` will be revoked by Google in a short period usually
    - Use the MT Manager to extract the installation package names of the detectors (long press to copy) and add them to ``/data/adb/tricky_store/target.txt`` (blacklist mode)
    - Use the MT Manager to write the current date, the date of the 1st day of the current month, or the date of the first day of the second month of the last season to ``/data/adb/tricky_store/security_patch.txt`` in the form of ``20250201``
  - Install the [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) module in the Magisk layer if the device does not have a broken TEE
  - Install the [bindhosts](https://github.com/backslashxx/bindhosts) or the built-in ``Systemless hosts`` module in the Magisk layer
    - Please remove the other module if one is selected to be used since they are not compatible
    - After rebooting, click the "Action" button of this module one or more times in the Magisk Manager to make it display "reset" and then click the "Action" button again to apply the latest rules if using the bindhosts module

### Using Apatch / KSU / KSU Next

- Install the latest version of [Apatch](https://t.me/APatchChannel)
  - Configure Apatch at the Super User tab
    - Grant root privileges to all applications requiring them
    - Use the default configurations for all the applications that do not require root privileges
  - Install the [NeoZygisk](https://github.com/JingMatrix/NeoZygisk/actions) module (the Release version in the latest action in the ``Jing Matrix`` fork) in the root manager layer
  - Install the [LSPosed](https://github.com/JingMatrix/LSPosed/actions) module (the Release version in the latest action in the ``Jing Matrix`` fork) in the root manager layer
    - Reboot $\rightarrow$ Open the LSPosed Manager $\rightarrow$ Create the LSPosed parasite $\rightarrow$ Create a desktop shortcut to the LSPosed parasite $\rightarrow$ Disable the logs which could make LSPosed being detected and the LSPosed taskbar notification in the setting page of the LSPosed parasite $\rightarrow$ Uninstall the LSPosed Manager
    - Input ``*#*#5776733#*#*`` in the dialer (do not call) to open the LSPosed parasite if necessary (in case the desktop shortcut is missing)
    - Install the [HMAL](https://github.com/pumPCin/HMAL) plugin in the LSPosed layer
    - Set the target scope of the HMAL plugin to **System Framework** only and enable the HMAL plugin in the LSPosed Manager
    - Reboot the device
    - Configure the HMAL
      - Hide HMAL's icon from the launcher in the HMAL's settings page
      - Set the three switches in Data Isolation to ``On``, ``Off``, and ``On`` in sequence in the HMAL's settings page (may require root privileges)
      - Build appropriate whitelist (what applications the detectors can see) or blacklist (what applications the detectors cannot see) templates (can refer to [this tutorial](./HMAL/README.md))
      - Except for the Magisk Manager and the plugins, enable hiding for all user applications and system-pre-installed non-critical applications with suitable templates applied
  - Install the [Play Integrity FIx](https://github.com/chiteroman/PlayIntegrityFix) module in the Magisk layer
  - Install the [Tricky Store](https://github.com/5ec1cff/TrickyStore) module in the Magisk layer
    - Use the MT Manager to rename the ``keybox.xml`` file in the ``/data/adb/tricky_store/`` directory to ``keybox.xml.bak`` (``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``)
    - Search for a free recent ``keybox.xml`` in the Telegram channel [FreeKeyboxShare](https://t.me/FreeKeyboxShare) and use the MT Manager to move it to ``/data/adb/tricky_store/``
    - Use [Key Attestation](https://github.com/vvb2060/KeyAttestation) to check if it passes the Device (old Strong) integrity $\rightarrow$ Click ``/data/adb/tricky_store/keybox.xml.bak`` in the MT Manager and restore the backup if not
    - Please try to generate a ``keybox.xml`` that can pass the Basic (old Device) integrity via a Python script from [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) if the free ``keybox.xml`` does not work or the ``keybox.xml`` signed based on the root certificate from the AOSP is not wished to be used
    - Never buy a ``keybox.xml`` unless the seller guarantees to offer you a new valid one once the previous one is revoked since each ``keybox.xml`` will be revoked by Google in a short period usually
    - Use the MT Manager to extract the installation package names of the detectors (long press to copy) and add them to ``/data/adb/tricky_store/target.txt`` (blacklist mode)
    - Use the MT Manager to write the current date, the date of the 1st day of the current month, or the date of the first day of the second month of the last season to ``/data/adb/tricky_store/security_patch.txt`` in the form of ``20250201``
  - Install the [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) module in the Magisk layer if the device does not have a broken TEE

---

## 过检方法

### 正在使用官方版或 Alpha 版面具

- 安装最新版[官方版面具](https://github.com/LSPosed/LSPosed.github.io/releases/)或 [Alpha 版面具](https://install.appcenter.ms/users/vvb2060/apps/magisk/distribution_groups/public)
  - 配置面具
    - 打开 Zygisk（或使用 [ZygiskNext](https://github.com/Dr-TSNG/ZygiskNext)）
    - 关闭“遵守排除列表”开关
    - 清空“配置排除列表”列表
    - 启动 MT 管理器和其它需要 root 权限的应用程序并用 Magisk 管理器进行授权
  - 在面具层安装 ``Jing Matrix`` 分支中最后一次 action 生成的 Release 版 [LSPosed](https://github.com/JingMatrix/LSPosed/actions) 模块
    - 重启设备 $\rightarrow$ 打开 LSPosed 管理器 $\rightarrow$ 创建 LSPosed 寄生器 $\rightarrow$ 创建寄生器快捷方式 $\rightarrow$ 关闭可能导致 LSPosed 被检测到的日志功能和 LSPosed 的任务栏通知 $\rightarrow$ 卸载 LSPosed 管理器
    - 如有需要可使用拨号键拨号 ``*#*#5776733#*#*``（不用呼叫）打开 LSPosed 寄生器（例如在桌面快捷方式丢失的情况下）
    - 在 LSPosed 层安装 [HAML](https://github.com/pumPCin/HMAL) 插件
    - 设置作用域为仅**系统框架**并启用插件
    - 重启设备
    - 配置 HMAL 插件
      - 在 HMAL 的设置页面将 HMAL 的图标从启动器中隐藏
      - 在 HMAL 的设置页面将数据隔离中的三个开关依次设置为开、关、开（部分修改需要 root 权限）
      - 构建适当的白名单（只想让检测软件检测到哪些应用）或黑名单（让检测软件不能检测到哪些应用）模板（可参照[该教程](./HMAL/README.md)）
      - 对除面具和插件之外的一切用户应用和系统预装的非关键应用启用隐藏并应用模板
  - 在面具层安装 [Shamiko](https://github.com/LSPosed/LSPosed.github.io/releases/) 模块
    - 使用 MT 管理器在 ``/data/adb/shamiko/`` 目录下创建一个名为 ``whitelist`` 的空文件（可直接在 root 下执行 ``touch /data/adb/shamiko/whitelist`` 命令）
    - 如果需要可以向该文件添加允许获取 root 权限的应用的包名
  - 在面具层安装 [Play Integrity Fix](https://github.com/chiteroman/PlayIntegrityFix) 模块
  - 在面具层安装 [Tricky Store](https://github.com/5ec1cff/TrickyStore) 模块
    - 使用 MT 管理器将 ``/data/adb/tricky_store/`` 目录下的 ``keybox.xml`` 文件重命名为 ``keybox.xml.bak``（``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``）
    - 在电报频道 [FreeKeyboxShare](https://t.me/FreeKeyboxShare) 搜索一个最近的免费 ``keybox.xml`` 并使用 MT 管理器将其移动到 ``/data/adb/tricky_store/`` 目录下
    - 使用 [Key Attestation](https://github.com/vvb2060/KeyAttestation) 检验是否通过 Device（旧 Strong）完整性等级，如果不是，请在 MT 管理器中单击 ``/data/adb/tricky_store/keybox.xml.bak`` 并恢复备份
    - 如果免费 ``keybox.xml`` 无效或不希望使用基于安卓开源项目根证书签署的 ``keybox.xml``，请尝试使用来自 [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) 的 Python 脚本来生成一个 可以通过 Basic（旧 Device）完整性等级的 ``keybox.xml``
    - 永远不要购买 ``keybox.xml``，除非卖家保证在之前的 ``keybox.xml`` 被撤销后立即为您提供一个新的且有效的 ``keybox.xml`` 因为每个 ``keybox.xml`` 通常会在短时间内被 Google 撤销
    - 使用 MT 管理器提取检测应用的安装包包名（可以长按复制）并编辑 ``/data/adb/tricky_store/target.txt`` 将所有目标应用的包名添加进去（黑名单模式）
    - 使用 MT 管理器编辑 ``/data/adb/tricky_store/security_patch.txt`` 将当天的日期、当月的 1 号的日期或上一个季度的第二个月份的 1 号按照 ``20250201`` 的格式写进去
  - 如果设备不存在 TEE 损坏的情况，可在面具层安装 [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) 模块
  - 在面具层安装 [bindhosts](https://github.com/backslashxx/bindhosts) 或内置的 Systemless hosts 模块
    - 由于两者不兼容，如果决定使用两者中的某一个模块，请移除另一个模块
    - 如果使用 bindhosts，请在重启设备后在面具管理器中点击一次或多次该模块的“操作”按钮使其显示 ``reset`` 后再点一次“操作”按钮使其应用最新规则

### 正在使用 Delta 版面具（小狐狸面具）

- 安装停更前的最后一个版本的 [Delta 面具](https://github.com/HuskyDG/magisk-files)
  - 由于已在 2024 年初停更未来可能跟不上时代潮流
  - 配置面具
    - 打开 Zygisk（或使用 [ZygiskNext](https://github.com/Dr-TSNG/ZygiskNext)）
    - 在设置界面启用白名单模式
    - 选定需要 root 权限的应用的包（可以不选定某个应用程序内的所有包）
  - 在面具层安装 ``Jing Matrix`` 分支中最后一次 action 生成的 Release 版 [LSPosed](https://github.com/JingMatrix/LSPosed/actions) 模块
    - 重启设备 $\rightarrow$ 打开 LSPosed 管理器 $\rightarrow$ 创建 LSPosed 寄生器 $\rightarrow$ 创建寄生器快捷方式 $\rightarrow$ 关闭可能导致 LSPosed 被检测到的日志功能和 LSPosed 的任务栏通知 $\rightarrow$ 卸载 LSPosed 管理器
    - 如有需要可使用拨号键拨号 ``*#*#5776733#*#*``（不用呼叫）打开 LSPosed 寄生器（例如在桌面快捷方式丢失的情况下）
    - 在 LSPosed 层安装 [HAML](https://github.com/pumPCin/HMAL) 插件
    - 设置作用域为仅**系统框架**并启用插件
    - 重启设备
    - 配置 HMAL 插件
      - 在 HMAL 的设置页面将 HMAL 的图标从启动器中隐藏
      - 在 HMAL 的设置页面将数据隔离中的三个开关依次设置为开、关、开（部分修改需要 root 权限）
      - 构建适当的白名单（只想让检测软件检测到哪些应用）或黑名单（让检测软件不能检测到哪些应用）模板
      - 对除面具和插件之外的一切用户应用和系统预装的非关键应用启用隐藏并应用模板
  - 在面具层安装 [Play Integrity Fix](https://github.com/chiteroman/PlayIntegrityFix) 模块
  - 在面具层安装 [Tricky Store](https://github.com/5ec1cff/TrickyStore) 模块
    - 使用 MT 管理器将 ``/data/adb/tricky_store/`` 目录下的 ``keybox.xml`` 文件重命名为 ``keybox.xml.bak``（``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``）
    - 在电报频道 [FreeKeyboxShare](https://t.me/FreeKeyboxShare) 搜索一个最近的免费 ``keybox.xml`` 并使用 MT 管理器将其移动到 ``/data/adb/tricky_store/`` 目录下
    - 使用 [Key Attestation](https://github.com/vvb2060/KeyAttestation) 检验是否通过 Device（旧 Strong）完整性等级，如果不是，请在 MT 管理器中单击 ``/data/adb/tricky_store/keybox.xml.bak`` 并恢复备份
    - 如果免费 ``keybox.xml`` 无效或不希望使用基于安卓开源项目根证书签署的 ``keybox.xml``，请尝试使用来自 [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) 的 Python 脚本来生成一个 可以通过 Basic（旧 Device）完整性等级的 ``keybox.xml``
    - 永远不要购买 ``keybox.xml``，除非卖家保证在之前的 ``keybox.xml`` 被撤销后立即为您提供一个新的且有效的 ``keybox.xml`` 因为每个 ``keybox.xml`` 通常会在短时间内被 Google 撤销
    - 使用 MT 管理器提取检测应用的安装包包名（可以长按复制）并编辑 ``/data/adb/tricky_store/target.txt`` 将所有目标应用的包名添加进去（黑名单模式）
    - 使用 MT 管理器编辑 ``/data/adb/tricky_store/security_patch.txt`` 将当天的日期、当月的 1 号的日期或上一个季度的第二个月份的 1 号按照 ``20250201`` 的格式写进去
  - 如果设备不存在 TEE 损坏的情况，可在面具层安装 [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) 模块
  - 在面具层安装 [bindhosts](https://github.com/backslashxx/bindhosts) 或内置的 Systemless hosts 模块
    - 由于两者不兼容，如果决定使用两者中的某一个模块，请移除另一个模块
    - 如果使用 bindhosts，请在重启设备后在面具管理器中点击一次或多次该模块的“操作”按钮使其显示 ``reset`` 后再点一次“操作”按钮使其应用最新规则

### 正在使用 Apatch / KSU / KSU Next

- 安装最新版 [Apatch](https://t.me/APatchChannel)
  - 在超级用户页配置 Apatch
    - 将所有需要 Root 的应用程序进行授权
    - 将剩余应用中所有不需要被 LSPosed 注入的添加到排除列表
  - 在 Root 管理器层安装 ``Jing Matrix`` 分支中最后一次 action 生成的 Release 版 [NeoZygisk](https://github.com/JingMatrix/NeoZygisk/actions) 模块
  - 在 Root 管理器层安装 ``Jing Matrix`` 分支中最后一次 action 生成的 Release 版 [LSPosed](https://github.com/JingMatrix/LSPosed/actions) 模块
    - 重启设备 $\rightarrow$ 打开 LSPosed 管理器 $\rightarrow$ 创建 LSPosed 寄生器 $\rightarrow$ 创建寄生器快捷方式 $\rightarrow$ 关闭可能导致 LSPosed 被检测到的日志功能和 LSPosed 的任务栏通知 $\rightarrow$ 卸载 LSPosed 管理器
    - 如有需要可使用拨号键拨号 ``*#*#5776733#*#*``（不用呼叫）打开 LSPosed 寄生器（例如在桌面快捷方式丢失的情况下）
    - 在 LSPosed 层安装 [HAML](https://github.com/pumPCin/HMAL) 插件
    - 设置作用域为仅**系统框架**并启用插件
    - 重启设备
    - 配置 HMAL 插件
      - 在 HMAL 的设置页面将 HMAL 的图标从启动器中隐藏
      - 在 HMAL 的设置页面将数据隔离中的三个开关依次设置为开、关、开（部分修改需要 root 权限）
      - 构建适当的白名单（只想让检测软件检测到哪些应用）或黑名单（让检测软件不能检测到哪些应用）模板
      - 对除面具和插件之外的一切用户应用和系统预装的非关键应用启用隐藏并应用模板
  - 在 Apatch 层安装 [Play Integrity Fix](https://github.com/chiteroman/PlayIntegrityFix) 模块
  - 在 Apatch 层安装 [Tricky Store](https://github.com/5ec1cff/TrickyStore) 模块
    - 使用 MT 管理器将 ``/data/adb/tricky_store/`` 目录下的 ``keybox.xml`` 文件重命名为 ``keybox.xml.bak``（``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``）
    - 在电报频道 [FreeKeyboxShare](https://t.me/FreeKeyboxShare) 搜索一个最近的免费 ``keybox.xml`` 并使用 MT 管理器将其移动到 ``/data/adb/tricky_store/`` 目录下
    - 使用 [Key Attestation](https://github.com/vvb2060/KeyAttestation) 检验是否通过 Device（旧 Strong）完整性等级，如果不是，请在 MT 管理器中单击 ``/data/adb/tricky_store/keybox.xml.bak`` 并恢复备份
    - 如果免费 ``keybox.xml`` 无效或不希望使用基于安卓开源项目根证书签署的 ``keybox.xml``，请尝试使用来自 [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) 的 Python 脚本来生成一个 可以通过 Basic（旧 Device）完整性等级的 ``keybox.xml``
    - 永远不要购买 ``keybox.xml``，除非卖家保证在之前的 ``keybox.xml`` 被撤销后立即为您提供一个新的且有效的 ``keybox.xml`` 因为每个 ``keybox.xml`` 通常会在短时间内被 Google 撤销
    - 使用 MT 管理器提取检测应用的安装包包名（可以长按复制）并编辑 ``/data/adb/tricky_store/target.txt`` 将所有目标应用的包名添加进去（黑名单模式）
    - 使用 MT 管理器编辑 ``/data/adb/tricky_store/security_patch.txt`` 将当天的日期、当月的 1 号的日期或上一个季度的第二个月份的 1 号按照 ``20250201`` 的格式写进去
  - 如果设备不存在 TEE 损坏的情况，可在面具层安装 [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) 模块

### 特殊情况

#### Momo

##### 包管理服务异常

参考一篇 2023 年初的问答：[https://zhidao.baidu.com/question/633770792883881924.html](https://zhidao.baidu.com/question/633770792883881924.html)

##### 已开启调试模式

- 在不使用调试模式时关闭调试模式
- 不建议使用插件进行过检因为对检测应用注入虽然能够过检掉调试模式（可疑级别）但会暴露 Xposed 注入（确信级别）反而得不偿失

##### 存在 TWRP 文件

将 ``/sdcard/`` 下的 TWRP 文件夹重命名（例如 .TWRP）

##### Bootloader 未锁定

- 在面具层安装 [Play Integrity Fix](https://github.com/chiteroman/PlayIntegrityFix) 模块
- 不建议使用插件进行过检因为对检测应用注入虽然能够过检掉调试模式（可疑级别）但会暴露 Xposed 注入（确信级别）反而得不偿失

#### Ruru

##### syscall 找到 HMA

换用 HMAL

#### 牛头人

##### 最近的版本（约 ``26.0`` 开始）报 Malicious hook

暂无解决办法（一说是假阳性）

#### Native root detector

##### 检测到 GMS 或本应用的的 odex 文件中存在 LSPosed 痕迹

临时解决方案：重命名该文件为 *.odex.bak
永久解决方案：将原有 LSPosed 卸载干净后安装 [https://github.com/JingMatrix/LSPosed/actions](https://github.com/JingMatrix/LSPosed/actions) 中最后一次成功的 Release 版本并依照 [../Detectors/README.md](../Detectors/README.md) 中的注意事项重新启动检测

#### 邮储银行

##### 2023 年 9 月左右使用了当时最新版官方面具和最新版 Shamiko 依旧闪退

- 历史问题更新即可
- 如果希望继续使用官方面具或 Alpha 面具
  - 更新至最新版官方面具或 Alpha 面具
  - 更新至最新版 Shamiko
- 如果希望换用 Delta 版面具（当时的 Delta 版面具不会让邮储银行出现闪退）
  - 当时的解决方法：2023 年 9 月左右的 Delta 版面具可以有效过检
  - 现在的解决方法：使用停更前的最后一个 Delta 版面具

#### Octopus、中银香港等应用

##### Apatch 用户闪退或闪退后打开一个网页告知手机环境异常

- 添加到排除列表

#### 微信

##### 开启指纹支付提示失败（但其它境内外应用都能正常使用指纹）

- 临时解决方法：使用微信支付模块或微信支付插件（原理是通过指纹后将预先存储的密码进行提交）
- 本质解决方法：暂无
