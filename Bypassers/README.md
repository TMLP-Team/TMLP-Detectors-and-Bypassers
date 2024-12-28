## Bypassers

### Using Official Magisk or Magisk Alpha

- Install the latest Official [Magisk](https://github.com/LSPosed/LSPosed.github.io/releases/) or [Magisk Alpha](https://install.appcenter.ms/users/vvb2060/apps/magisk/distribution_groups/public)
  - Configure the Magisk
    - Enable Zygisk (or use [ZygiskNext](https://github.com/Dr-TSNG/ZygiskNext))
    - Disable Denylist
    - Empty Denylist
    - Launch the applications requiring root privileges like the MT Manager and grant root requests in Magisk
  - Install the [LSPosed](https://github.com/LSPosed/LSPosed) module in the Magisk layer
    - Reboot $\rightarrow$ Open the LSPosed Manager $\rightarrow$ Create the LSPosed parasite $\rightarrow$ Create a desktop shortcut to the LSPosed parasite $\rightarrow$ Disable LSPosed taskbar notification $\rightarrow$ Uninstall the LSPosed Manager
    - Install the [HMAL](https://github.com/pumPCin/HMAL) plugin in the LSPosed layer
    - Set the target scope of the HMAL plugin to **System Framework** only and enable the HMAL plugin in the LSPosed Manager
    - Reboot the device
    - Configure the HMAL
      - Hide HMAL's icon from the launcher in the HMAL's settings page
      - Set the three switches in Data Isolation to ``On``, ``Off``, and ``On`` in sequence in the HMAL's settings page (may require root privileges)
      - Build appropriate whitelist (what applications the detectors can see) or blacklist (what applications the detectors cannot see) templates
      - Except for the Magisk Manager and the plugins, enable hiding for all user applications and system-pre-installed non-critical applications with suitable templates applied
  - Install the [Shamiko](https://github.com/LSPosed/LSPosed.github.io/releases/) module in the Magisk layer
    - Use the MT Manager to create an empty file named ``whitelist`` under ``/data/adb/shamiko/`` (or execute the command ``touch /data/adb/shamiko/whitelist`` as root)
    - Add the package names of the applications that are allowed to obtain root privileges to this file if necessary
  - Install the [Play Integrity FIx](https://github.com/chiteroman/PlayIntegrityFix) module in the Magisk layer
  - Install the [Tricky Store](https://github.com/5ec1cff/TrickyStore) module in the Magisk layer
    - Use the MT Manager to rename the ``keybox.xml`` file in the ``/data/adb/tricky_store/`` directory to ``keybox.xml.bak`` (``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``)
    - Search for a free recent keybox.xml in the Telegram channel [FreeKeyboxShare](https://t.me/FreeKeyboxShare) and use MT the Manager to move it to ``/data/adb/tricky_store/``
    - Use [Key Attestation](https://github.com/vvb2060/KeyAttestation) to check if it passes the Strong integrity $\rightarrow$ Click ``/data/adb/tricky_store/keybox.xml.bak`` in the MT Manager and restore the backup if not
    - Please try to generate a ``keybox.xml`` that can pass the Device integrity via a Python script from [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) if the ``keybox.xml`` signed based on the root certificate from the AOSP is not wished to be used
  - Install the [bindhosts](https://github.com/backslashxx/bindhosts) or the built-in ``Systemless hosts`` module in the Magisk layer
    - Please remove the other module if one is selected to be used since they are not compatible
    - After rebooting, click the "Action" button of this module one or more times in the Magisk Manager to make it display "reset" and then click the "Action" button again to apply the latest rules if using the bindhosts module

---

## 过检方法

### 正在使用官方版或 Alpha 版面具

- 安装最新版[官方版面具](https://github.com/LSPosed/LSPosed.github.io/releases/)或 [Alpha 版面具](https://install.appcenter.ms/users/vvb2060/apps/magisk/distribution_groups/public)
  - 配置面具
    - 打开 Zygisk（或使用 [ZygiskNext](https://github.com/Dr-TSNG/ZygiskNext)）
    - 关闭“遵守排除列表”开关
    - 清空“配置排除列表”列表
    - 启动 MT 管理器和其它需要 root 权限的应用程序并用 Magisk 管理器进行授权
  - 在面具层安装 [LSPosed](https://github.com/LSPosed/LSPosed) 模块
    - 重启设备 $\rightarrow$ 打开 LSPosed 管理器 $\rightarrow$ 创建 LSPosed 寄生器 $\rightarrow$ 创建寄生器快捷方式 $\rightarrow$ 关闭 LSPosed 的任务栏通知 $\rightarrow$ 卸载 LSPosed 管理器
    - 在 LSPosed 层安装 [HAML](https://github.com/pumPCin/HMAL) 插件
    - 设置作用域为仅**系统框架**并启用插件
    - 重启设备
    - 配置 HMAL 插件
      - 在 HMAL 的设置页面将 HMAL 的图标从启动器中隐藏
      - 在 HMAL 的设置页面将数据隔离中的三个开关依次设置为开、关、开（部分修改需要 root 权限）
      - 构建适当的白名单（只想让检测软件检测到哪些应用）或黑名单（让检测软件不能检测到哪些应用）模板
      - 对除面具和插件之外的一切用户应用和系统预装的非关键应用启用隐藏并应用模板
  - 在面具层安装 [Shamiko](https://github.com/LSPosed/LSPosed.github.io/releases/) 模块
    - 使用 MT 管理器在 ``/data/adb/shamiko/`` 目录下创建一个名为 ``whitelist`` 的空文件（可直接在 root 下执行 ``touch /data/adb/shamiko/whitelist`` 命令）
    - 如果需要可以向该文件添加允许获取 root 权限的应用的包名
  - 在面具层安装 [Play Integrity Fix](https://github.com/chiteroman/PlayIntegrityFix) 模块
  - 在面具层安装 [Tricky Store](https://github.com/5ec1cff/TrickyStore) 模块
    - 使用 MT 管理器将 ``/data/adb/tricky_store/`` 目录下的 ``keybox.xml`` 文件重命名为 ``keybox.xml.bak``（``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``）
    - 在电报频道 [FreeKeyboxShare](https://t.me/FreeKeyboxShare) 搜索一个最近的免费 keybox.xml 并使用 MT 管理器将其移动到 ``/data/adb/tricky_store/`` 目录下
    - 使用 [Key Attestation](https://github.com/vvb2060/KeyAttestation) 检验是否通过强完整性（Strong Integrity），如果不是，请在 MT 管理器中单击 ``/data/adb/tricky_store/keybox.xml.bak`` 并恢复备份
    - 如果不希望使用基于安卓开源项目根证书签署的 ``keybox.xml``，请尝试使用来自 [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) 的 Python 脚本来生成一个 可以通过设备完整性的 ``keybox.xml``
  - 在面具层安装 [bindhosts](https://github.com/backslashxx/bindhosts) 或内置的 Systemless hosts 模块
    - 由于两者不兼容，如果决定使用两者中的某一个模块，请移除另一个模块
    - 如果使用 bindhosts，请在重启设备后在面具管理器中点击一次或多次该模块的“操作”按钮使其显示 ``reset`` 后再点一次“操作”按钮使其应用最新规则
