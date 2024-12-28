## Bypassers

### Using Official Magisk

- Install the latest Official [Magisk](https://github.com/LSPosed/LSPosed.github.io/releases/)
  - Configure the Magisk
    - Enable Zygisk (or use [ZygiskNext](https://github.com/Dr-TSNG/ZygiskNext))
    - Disable Denylist
    - Empty Denylist
    - Launch the applications requiring root privileges like the MT Manager and grant root requests in Magisk
  - Install the [Shamiko](https://github.com/LSPosed/LSPosed.github.io/releases/) module in the Magisk layer
  - Install the [LSPosed](https://github.com/LSPosed/LSPosed) module in the Magisk layer
    - Install the [HMAL](https://github.com/pumPCin/HMAL) plugin in the LSPosed layer
    - Set the target scope of the HMAL plugin to **System Framework** only and enable the HMAL plugin in the LSPosed manager
    - Reboot the device
    - Configure the HMAL
      - Hide HMAL's icon from the launcher in HMAL's settings page
      - 

---

## 过检方法

### 正在使用官方版面具

- 安装最新版[官方版面具](https://github.com/LSPosed/LSPosed.github.io/releases/)
  - 配置面具
    - 打开 Zygisk（或使用 [ZygiskNext](https://github.com/Dr-TSNG/ZygiskNext)）
    - 关闭“遵守排除列表”开关
    - 清空“配置排除列表”列表
    - 启动 MT 管理器和其它需要 root 权限的应用程序并用 Magisk 管理器进行授权
  - 在面具层安装 [Shamiko](https://github.com/LSPosed/LSPosed.github.io/releases/) 模块
  - 在面具层安装 [LSPosed](https://github.com/LSPosed/LSPosed) 模块
    - 在 LSPosed 层安装 [HAML](https://github.com/pumPCin/HMAL) 插件
    - 设置作用域为仅**系统框架**并启用插件
    - 重启设备
    - 配置 HMAL 插件
      - 在 HMAL 的设置页面将 HMAL 的图标从启动器中隐藏
      - 构建适当的白名单（只想让检测软件检测到哪些应用）或黑名单（让检测软件不能检测到哪些应用）模板
      - 对
