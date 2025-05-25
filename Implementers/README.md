## Implementers

Related implementers related to Magisk, Zygisk, and LSPosed are stored here. 

The following tutorial is applicable to the deployment of Magisk (and its branches) and Apatch (and its branches) on Android devices. If you have completed a step, please skip it directly. 

- Install the necessary adb, fastboot, and corresponding mobile device drivers on the computer
- Connect the Android device to the computer via USB
- Unlock the bootloader of the Android device (need to clear the data of the Android device)
  - Enable developer mode on the Android device
  - Enable the switch to allow OEM unlocking in the developer options of the Android device
  - Reboot the Android device to fastboot mode
  - Execute ``fastboot oem unlock`` or ``fastboot flashing unlock`` on the computer (different fastboot versions and devices will have different instructions)
  - Reboot the Android device
- First root
  - Prepare your root manager (latest)
  - Route 1: By patching the ``boot.img``
    - Extract boot.img from the 9008 package or full package with the same system version as the target Android device
    - Copy the extracted boot.img to the external storage of the phone
    - Patching boot.img
      - Install the root manager
      - Open the root manager
      - Select Install
      - Select Patching an image
      - Use the file manager to select the boot.img copied from the computer to the Android device above
      - Click Patching and wait for the patching to complete
    - Flash the patched boot.img
      - Find the patched boot.img in the download directory of the Android device and copy it to the computer
      - Execute ``fastboot boot "boot_patched.img"`` on the computer and observe whether it can boot (here ``boot_patched.img`` is the computer file path of the patched boot.img)
      - Execute ``fastboot getvar current-slot`` on the computer to view the current active partition
      - If it is a: Execute ``fastboot flash boot_a "boot_patched.img"`` on the computer to flash the partition (here ``boot_patched.img`` is the computer file path of the patched boot.img)
      - If it is b: Execute ``fastboot flash boot_b "boot_patched.img"`` on the computer to flash the partition (here ``boot_patched.img`` is the computer file path of the patched boot.img)
  - Route 2: Via a third-party recovery (only applicable to Magisk and its branches)
    - Find and download the TWRP image for the current Android device and system
    - Reboot the Android device to fastboot mode
    - Use ``fastboot boot twrp.img`` to boot the Android device to temporary TWRP mode (here ``twrp.img`` is the downloaded TWRP image)
    - If necessary, you can choose to permanently flash the current TWRP in the TWRP interface of the Android device
    - Rename the latest version of the Magisk application to magisk.zip and copy it to the Android device
    - Select Install in the TWRP interface
    - Select the imported magisk.zip in the TWRP interface and flash it
- Subsequent root
  - Refer to the first root
  - Install directly in the root manager
- After the deployment is complete, please restart the Android device to normal mode

Among them, rebooting means rebooting into the normal mode by default. For the implementation of restarting the Android device to fastboot mode, please refer to the following content. 

- Reboot the Android device to fastboot mode
  - Use adb
    - Put the Android device in the unlocked screen state of normal boot
    - Enable USB debugging in the developer options of the Android device
    - Run ``adb devices`` on the computer
    - If the Android device requires USB debugging authorization, please authorize it
    - Run ``adb reboot bootloader`` on the computer to restart to fastboot mode
  - Through advanced reboot
    - Some Android devices (such as OnePlus) can enable the function of adding advanced reboot options to the long-press of the power button in the developer options
    - Enable this function and long press the power button to reboot to the bootloader
  - Through the combination of keys in the off state
    - Turn off the Android device
    - Disconnect the Android device from the USB connection with the computer
    - Long press the combination of keys according to the phone model (for example, long press the power button and two volume buttons together) to enter the bootloader (if it fails, please wait patiently for the screen to be unlocked after the power is turned on and then turn it off and try again)
    - Reconnect the Android device to the computer through USB

---

## 部署工具

与 Magisk、Zygisk 和 LSPosed 相关的部署工具在此处存储。

以下教程适用于 Magisk 及其分支 和 Apatch 及其分支在安卓设备上的部署，如已完成请直接跳过。

- 在计算机上安装必要的 adb、fastboot 和对应的手机设备驱动
- 将安卓设备与计算机进行 USB 连接
- 为安卓设备解除 bootloader 锁（需要清空安卓设备数据）
  - 在安卓设备中打开开发者模式
  - 在安卓设备的开发者选项中打开允许 oem 解锁开关
  - 重启安卓设备至 fastboot 模式
  - 在计算机中执行 ``fastboot oem unlock`` 或 ``fastboot flashing unlock``（不同 fastboot 版本和设备会有不同指令）
  - 重启安卓设备
- 首次 root
  - 准备好你的 root 管理器（最新版）
  - 修补 boot.img 路线
    - 从与目标安卓设备系统版本相同的 9008 包或全量包中提取 boot.img
    - 将提取的 boot.img 复制到手机的外部存储中
    - 修补 boot.img
      - 安装 root 管理器应用
      - 打开 root 管理器应用
      - 选择安装
      - 选择通过修补一个镜像
      - 利用文件管理器选择上述从计算机复制到安卓设备的 boot.img
      - 点击修补并等待修补完成
    - 刷入修补后的 boot.img
      - 在安卓设备的下载目录找到修补后的 boot.img 并将其拷贝到计算机中
      - 在计算机中执行 ``fastboot boot "boot_patched.img"`` 并观察能否开机（此处 ``boot_patched.img`` 为修补后的 boot.img 的计算机文件路径）
      - 在计算机中执行 ``fastboot getvar current-slot`` 查看当前活跃分区
      - 若为 a：在计算机中执行 ``fastboot flash boot_a "boot_patched.img"`` 刷入分区（此处 ``boot_patched.img`` 为修补后的 boot.img 的计算机文件路径）
      - 若为 b：在计算机中执行 ``fastboot flash boot_b "boot_patched.img"`` 刷入分区（此处 ``boot_patched.img`` 为修补后的 boot.img 的计算机文件路径）
  - 第三方 Rec 路线（仅适用于 Magisk 及其分支）
    - 寻找并下载适用于当前安卓设备和系统的 TWRP 镜像
    - 重启安卓设备至 fastboot 模式
    - 使用 ``fastboot boot twrp.img`` 启动安卓设备至临时 TWRP 模式（此处 ``twrp.img`` 为下载的 TWRP 镜像）
    - 如有需要可在安卓设备的 TWRP 界面选择永久刷入当前 TWRP
    - 将最新版 Magisk 应用重命名为 magisk.zip 并复制到安卓设备中
    - 在 TWRP 界面选择安装
    - 在 TWRP 界面选中导入的 magisk.zip 并刷入
- 后续 root
  - 参阅首次 root
  - 在 root 管理器中直接安装
- 部署完成后请重启安卓设备至正常模式

其中，重启安卓设备默认是重启至正常模式。有关重启安卓设备至 fastboot 模式的实现，可参阅以下内容。

- 重启安卓设备至 fastboot 模式
  - 利用 adb
    - 让安卓设备出于正常开机的屏幕解锁状态下
    - 在安卓设备的开发者选项中打开 USB 调试
    - 在计算机上执行 ``adb devices``
    - 若安卓设备需要 USB 调试授权请授权
    - 在计算机上执行 ``adb reboot bootloader`` 实现重启到 fastboot 模式
  - 通过高级重启
    - 部分安卓设备（如一加）在开发者选项中可以启用向长按电源键添加高级重启选项的功能
    - 启用该功能并长按电源键重启至 bootloader
  - 通过关机状态下的组合键
    - 将安卓设备关机
    - 将安卓设备断开与计算机的 USB 连接
    - 根据手机型号长按组合键（例如电源键与两个音量键一起长按）进入 bootloader（如果失败请耐心等待开机解锁屏幕后关机再来一次）
    - 重新将安卓设备与计算机进行 USB 连接

