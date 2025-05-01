## Bypassers

### Using Official Magisk (Including Release, Canary, and Debug Versions) or Magisk Alpha

- Install the latest [Magisk Alpha](https://install.appcenter.ms/users/vvb2060/apps/magisk/distribution_groups/public)
  - Configure the Magisk
    - Disable built-in Zygisk
    - Disable Denylist
    - Empty Denylist
    - Launch the applications requiring root privileges like the MT Manager and grant root requests in Magisk
  - Install the [Zygisk Next](https://github.com/Dr-TSNG/ZygiskNext) module in the Magisk layer
    - Disable the Denylist in Zygisk Next
  - Install the [LSPosed](https://github.com/JingMatrix/LSPosed/actions) module (the latest build in the ``action`` page of the ``Jing Matrix`` GitHub repository) in the Magisk layer
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
    - Use the MT Manager to write the date of the 1st day of the current month to ``/data/adb/tricky_store/security_patch.txt`` in the form of ``20250401``
  - Install the [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) module in the Magisk layer if the device does not have a broken TEE
  - Install the [bindhosts](https://github.com/backslashxx/bindhosts) or the built-in ``Systemless hosts`` module in the Magisk layer
    - Please remove the other module if one is selected to be used since they are not compatible
    - After rebooting, click the "Action" button of this module one or more times in the Magisk Manager to make it display "reset" and then click the "Action" button again to apply the latest rules if using the bindhosts module

### Using Magisk Delta

- Install the lastest version of [Magisk Delta](https://github.com/HuskyDG/magisk-files) before it was discontinued
  - It can be out-of-date since it seemed to be discontinued in early 2024
  - Configure Magisk Delta
    - Enable Zygisk (or use [NeoZygisk](https://github.com/JingMatrix/NeoZygisk/actions))
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
    - Use the MT Manager to write the date of the 1st day of the current month to ``/data/adb/tricky_store/security_patch.txt`` in the form of ``20250401``
  - Install the [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) module in the Magisk layer if the device does not have a broken TEE
  - Install the [bindhosts](https://github.com/backslashxx/bindhosts) or the built-in ``Systemless hosts`` module in the Magisk layer
    - Please remove the other module if one is selected to be used since they are not compatible
    - After rebooting, click the "Action" button of this module one or more times in the Magisk Manager to make it display "reset" and then click the "Action" button again to apply the latest rules if using the bindhosts module

### Using Apatch / Apatch Next / KSU / KSU Next

- Install the latest version of [Apatch](https://github.com/bmax121/APatch/actions), [KSU](https://github.com/tiann/KernelSU), or [KSU Next](https://t.me/ksunext)
  - Configure in the Super User tab of the root manager (The Apatch Manager Super User page seems to have a bug and you can {directly use the MT Manager to remove all application configurations except ``bin.mt.plus`` from the file ``/data/adb/ap/package_config`` after granting the MT Manager root privileges $rightarrow$ Reboot the device and use Apatch Manager again to grant root privileges to applications that require them})
    - Grant root privileges to all applications requiring them
    - Use the default configurations for all the applications that do not require root privileges
  - Deploy the kernel module in the root manager layer
    - Using Apatch or one of its branches (please back up the original ``boot.img`` and the current ``boot.img`` before operations): Find the latest version of the module Cherish Peekaboo from [https://t.me/app_process64](https://t.me/app_process64) and embed it as a kernel module (some models require the ``compat`` version)
    - Using KSU or one of its branches: Embed the [SUSFS](https://github.com/sidex15/susfs4ksu-module) module as a kernel module
  - Deploy the system module in the root manager layer
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
    - Use the MT Manager to write the date of the 1st day of the current month to ``/data/adb/tricky_store/security_patch.txt`` in the form of ``20250401``
    - Install the [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) module in the Magisk layer if the device does not have a broken TEE

### Special Cases

#### Momo

##### Package Management Service Exception

Turn off "Disable package manager signature verification" in Core Patcher by referring to [a post in early 2023](https://zhidao.baidu.com/question/633770792883881924.html)

##### Debug mode is enabled

- Turn off debug mode when not in use
- It is not recommended to use plugins for bypassing because it will expose Xposed/Edxposed/LSPosed injection/hooks (confident level), which is not worth the loss though injecting the detection application can pass the debug mode (suspicious level)

##### TWRP File Existence

Rename the TWRP folder under ``/sdcard/`` (for example, .TWRP)

##### Unlocked Bootloader

- Install [Play Integrity Fix](https://github.com/chiteroman/PlayIntegrityFix) module
- It is not recommended to use plugins for bypassing because it will expose Xposed/Edxposed/LSPosed injection/hooks (confident level), which is not worth the loss though the injection of the detected application can pass the debug mode (suspicious level)

#### Ruru

##### syscall finds HMA

- Switch to HMAL

#### Native Test

##### Versions from ``v26.0`` to the invitial ``v30.0`` reports "Malicious Hook"

- It can be a false positive since "Malicious Hook" was redefined in these versions
- Please use the latest version to check the environments. 

##### Others

- Please refer to [https://bbs.kanxue.com/thread-285106-1.htm](https://bbs.kanxue.com/thread-285106-1.htm)

#### Native Root Detector

##### LSPosed traces are detected in the ``odex`` file of GMS or this application

- Backup your plugin configurations in the LSPosed manager settings
- Uninstall Native Root Detector totally
- Disable WeChat and QQ (via Swift Backup or Fridge) if necessary
- Uninstall the original LSPosed in the root manager and reboot your device
- Install the lastest build in [https://github.com/JingMatrix/LSPosed/actions](https://github.com/JingMatrix/LSPosed/actions) in the root manager and reboot your device
- Restore your plugin configurations in the LSPosed manager settings
- Switch to the plugin tab of the LSPosed manager to check whether the restoration of all plugin configurations is finished
- Reboot your device
- Install the latest Native Root Detector for detection (do not restore Native Root Detector from any backup)
- Enable WeChat and QQ only after the detector shows normal environments (except risky applications detected with Code 3)

##### Mount inconsistency detected

- Magisk and its branches: Use Magisk Alpha and install the Shamiko module
- Apatch and its branches: Embed the Cherish Peekaboo module as a kernel module (please check if the ``compat`` version is needed)
- KSU and its branches: Embed the SUSFS module as a kernel module

##### Risky application detected (bypass HMA/HMAL)

- Temporary solution: random package name or uninstall corresponding application
- Permanent solution: None

#### Postal Savings Bank

##### Around September 2023, the latest official mask and the latest Shamiko at that time were used, but the crash still occurred

- Historical issues can be updated
- If you want to continue using the official mask or Alpha mask
- Update to the latest official mask or Alpha mask
- Update to the latest Shamiko
- If you want to switch to the Delta version mask (the Delta version mask at that time would not cause the Postal Savings Bank to crash)
- The solution at that time: the Delta version mask around September 2023 can be effectively inspected
- The current solution: Use the last Delta version mask before the suspension

#### Octopus, Bank of China Hong Kong, and other applications

##### Apatch users crash or open a web page after crashing to inform that the phone environment is abnormal

- Before March 2025: Add to the exclusion list
- In or after March 2025: Use NeoZygisk to implement Zygisk and reset the exclusion list for applications that do not require root

#### WeChat

##### Failed to open the fingerprint payment prompt (but other domestic and foreign applications can use fingerprints normally)

- Temporary solution: Use the WeChat Payment module or the WeChat Payment plugin (the principle is to submit the pre-stored password after passing the fingerprint)
- Essential solution: None

#### QQ

##### Logging out users with no reasons, account login limitations, or temporary account freezing

- Check your mobile QQ version
  - Mobile QQ (Android)
    - If you are using a QQ version affected by the 2021 spring and summer risk control event (``v8.6.0``, ``v8.8.17``] (the phenomenon is most obvious when using the ``v8.8.0`` version)
      - Switch to the ``v8.6.0`` or lower version (if rollback is still allowed)
      - Otherwise
        - Uninstall the QXposed (QX) plugin and the QQ Repeater plugin
        - Disable the red envelope grabbing function
    - If you are using a QQ version affected by the 2024 autumn to 2025 spring risk control event (``v9.1.0``, -) (the phenomenon is most obvious when using the ``v9.1.35`` version)
      - Uninstall XAutoDaily
      - Disable the automatic sign-in function (including daily check-in and group sign-in)
      - Switch to the ``v9.1.0`` or lower versions (if rollback is still allowed)
  - Computer QQ (Windows): Always use the nostalgic version instead of the QQNT version- Solutions (ranked from radical to conservative on the premise of keeping the root and injection environment of Android devices)
- Check your device environments (sorted from radical to conservative while keeping the Android device root and injection environment)
  - Solution 1: Always use old versions of QQ before receiving any warning or being controlled by the cloud, hide root and injection environments, and do not inject plugins for automatic sign-in or group messaging into QQ
  - Solution 2: Always use old versions of QQ before receiving any warning or being controlled by the cloud, hide root and injection environments, and do not inject any plugins into QQ
  - Solution 3: Always use the latest version of QQ, hide the root and injection environment, and do not inject any plugins into QQ

---

## 过检方法

### 正在使用官方版（含发行版、金丝雀版和 Debug 版）或 Alpha 版面具

- 安装最新版 [Alpha 版面具](https://install.appcenter.ms/users/vvb2060/apps/magisk/distribution_groups/public)
  - 配置面具
    - 禁用内置 Zygisk
    - 关闭“遵守排除列表”开关
    - 清空“配置排除列表”列表
    - 启动 MT 管理器和其它需要 root 权限的应用程序并用 Magisk 管理器进行授权
  - 在面具层安装最新版 [Zygisk Next](https://github.com/Dr-TSNG/ZygiskNext) 模块
    - 禁用 Zygisk Next 内的遵守排除列表
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
    - 使用 MT 管理器编辑 ``/data/adb/tricky_store/security_patch.txt`` 并将当月的 1 号的日期按照 ``20250401`` 的格式写入该文件
  - 如果设备不存在 TEE 损坏的情况，可在面具层安装 [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) 模块
  - 在面具层安装 [bindhosts](https://github.com/backslashxx/bindhosts) 或内置的 Systemless hosts 模块
    - 由于两者不兼容，如果决定使用两者中的某一个模块，请移除另一个模块
    - 如果使用 bindhosts，请在重启设备后在面具管理器中点击一次或多次该模块的“操作”按钮使其显示 ``reset`` 后再点一次“操作”按钮使其应用最新规则

### 正在使用 Delta 版面具（小狐狸面具）

- 安装停更前的最后一个版本的 [Delta 面具](https://github.com/HuskyDG/magisk-files)
  - 由于似乎已在 2024 年初停更未来可能跟不上时代潮流
  - 配置面具
    - 打开 Zygisk（或使用 [NeoZygisk](https://github.com/JingMatrix/NeoZygisk/actions)）
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
    - 使用 MT 管理器编辑 ``/data/adb/tricky_store/security_patch.txt`` 并将当月的 1 号的日期按照 ``20250401`` 的格式写入该文件
  - 如果设备不存在 TEE 损坏的情况，可在面具层安装 [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) 模块
  - 在面具层安装 [bindhosts](https://github.com/backslashxx/bindhosts) 或内置的 Systemless hosts 模块
    - 由于两者不兼容，如果决定使用两者中的某一个模块，请移除另一个模块
    - 如果使用 bindhosts，请在重启设备后在面具管理器中点击一次或多次该模块的“操作”按钮使其显示 ``reset`` 后再点一次“操作”按钮使其应用最新规则

### 正在使用 Apatch / Apatch Next / KSU / KSU Next

- 安装最新版 [Apatch](https://github.com/bmax121/APatch/actions)、[KSU](https://github.com/tiann/KernelSU) 或 [KSU Next](https://t.me/ksunext)
  - 在 root 管理器的超级用户页内进行配置（Apatch 管理器超级用户页面似乎有 bug 可直接在授予 MT 管理器 root 权限后使用 MT 管理器从文件 ``/data/adb/ap/package_config`` 中移除除 ``bin.mt.plus`` 以外的所有应用配置并在重启设备后再次使用 Apatch 管理器将 root 权限授予需要 root 权限的应用）
    - 将所有需要 root 的应用程序进行授权
    - 让剩余应用中所有不需要 root 权限的应用使用默认设置（重置设置）
  - 部署 root 管理器层的内核模块
    - 正在使用 Apatch 系列（在操作前请备份好原始 boot.img 和当前 boot.img）：从 [https://t.me/app_process64](https://t.me/app_process64) 中查找最新版模块 Cherish Peekaboo 并以内核模块的形式进行嵌入（部分机型需要 ``compat`` 版本）
    - 正在使用 KSU 系列：以内核模块的形式嵌入 [SUSFS](https://github.com/sidex15/susfs4ksu-module) 模块
  - 部署 root 管理器层的系统模块
    - 在 root 管理器层安装 ``Jing Matrix`` 分支中最后一次 action 生成的 Release 版 [NeoZygisk](https://github.com/JingMatrix/NeoZygisk/actions) 模块
    - 在 root 管理器层安装 ``Jing Matrix`` 分支中最后一次 action 生成的 Release 版 [LSPosed](https://github.com/JingMatrix/LSPosed/actions) 模块
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
    - 使用 MT 管理器编辑 ``/data/adb/tricky_store/security_patch.txt`` 并将当月的 1 号的日期按照 ``20250401`` 的格式写入该文件
    - 如果设备不存在 TEE 损坏的情况，可在面具层安装 [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) 模块

### 特殊情况

#### Momo

##### 包管理服务异常

在核心破解中关闭“禁用软件包管理器签名验证”（参考自[一篇 2023 年初的问答](https://zhidao.baidu.com/question/633770792883881924.html)）

##### 已开启调试模式

- 在不使用调试模式时关闭调试模式
- 不建议使用插件进行过检因为对检测应用注入虽然能够过检掉调试模式（可疑级别）但会暴露 Xposed/Edxposed/LSPosed 注入/钩子（确信级别）反而得不偿失

##### 存在 TWRP 文件

将 ``/sdcard/`` 下的 TWRP 文件夹重命名（例如 .TWRP）

##### Bootloader 未锁定

- 在面具层安装 [Play Integrity Fix](https://github.com/chiteroman/PlayIntegrityFix) 模块
- 不建议使用插件进行过检因为对检测应用注入虽然能够过检掉调试模式（可疑级别）但会暴露 Xposed/Edxposed/LSPosed 注入/钩子（确信级别）反而得不偿失

#### Ruru

##### syscall 找到 HMA

- 换用 HMAL

#### 牛头人

##### 从 ``v26.0`` 到 最初的 ``v30.0`` 版本报 Malicious hook

- 由于在这些版本中 Malicious hook 被重新定义因此它很可能是误报
- 请使用最新版检查环境

##### 其它问题

- 请参阅 [https://bbs.kanxue.com/thread-285106-1.htm](https://bbs.kanxue.com/thread-285106-1.htm)

#### Native Root Detector

##### 检测到 GMS 或本应用的的 ``odex`` 文件中存在 LSPosed 痕迹

- 在 LSPosed 管理器设置中备份您的插件配置
- 彻底卸载 Native Root Detector
- 如有必要请禁用微信和 QQ（可通过 Swift Backup 或冰箱应用）
- 在 root 管理器中卸载原版 LSPosed 并重启设备
- 在 root 管理器中安装 [https://github.com/JingMatrix/LSPosed/actions](https://github.com/JingMatrix/LSPosed/actions) 中的最新版本并重启设备
- 在 LSPosed 管理器设置中恢复您的插件配置
- 切换到 LSPosed 管理器的“插件”选项卡，检查所有插件配置是否已恢复完成
- 重启设备
- 安装最新的 Native Root Detector 进行检测（请勿从任何备份中恢复 Native Root Detector）
- 仅该检测器显示环境正常（以代码 3 显示的检测到风险应用除外）后才可以重新启用微信和 QQ

##### 检测到挂载不一致

- Magisk 系列：安装 Shamiko 模块
- Apatch 系列：以内核模块的形式嵌入 Cherish Peekaboo 模块（请自行排查是否需要 compat 版本）
- KSU 系列：以内核模块的形式嵌入 SUSFS 模块

##### 检测到风险应用（绕过 HMA/HMAL）

- 临时解决方案：随机包名或卸载对应应用
- 永久解决方案：暂无

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

- 2025 年 3 月前的解决办法：添加到排除列表
- 2025 年 3 月开始的解决办法：使用 NeoZygisk 实现 Zygisk 并对无需 root 的应用重置排除列表

#### 微信

##### 开启指纹支付提示失败（但其它境内外应用都能正常使用指纹）

- 临时解决方法：使用微信支付模块或微信支付插件（原理是通过指纹后将预先存储的密码进行提交）
- 本质解决方法：暂无

#### QQ

##### 无故下线用户、限制账号登录或临时冻结账号

- 检查 QQ 版本
  - 手机 QQ（安卓）
    - 正在使用受 2021 年春夏季节风控风波影响的 QQ 版本 (``v8.6.0``, ``v8.8.17``]（使用 ``v8.8.0`` 版本时现象最为明显）
      - 使用 ``v8.6.0`` 或更低版本（如果还允许回滚）
      - 或
        - 卸载 QXposed（QX）模块和 QQ 复读机模块
        - 停用抢红包功能
    - 正在使用受 2024 年秋季至 2025 年春季风控风波影响的 QQ 版本 (``v9.1.0``, -)（使用 ``v9.1.35`` 版本时现象最为明显）
      - 卸载 XAutoDaily
      - 停用自动签到功能（含每日打卡和群签到）
      - 可尝试使用 ``v9.1.0`` 或更低版本（如果还允许回滚）
  - 电脑 QQ（Windows）：始终使用怀旧版而非 QQNT 版本
- 检查环境（保留安卓设备 root 和注入环境的前提下从激进到保守排序）
  - 解决方案 1：在收到任何警告或被云控之前始终使用旧版 QQ，隐藏 root 和注入环境，不向 QQ 注入用于自动签到或群发消息的插件
  - 解决方案 2：在收到任何警告或被云控之前始终使用旧版 QQ，隐藏 root 和注入环境，不向 QQ 注入任何插件
  - 解决方案 3：自始至终使用最新版 QQ，隐藏 root 和注入环境，不向 QQ 注入任何插件
