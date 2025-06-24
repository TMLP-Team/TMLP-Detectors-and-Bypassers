## Bypassers

Currently, SukiSU + ReZygisk + SUSFS is the optimal solution, follwed by Magisk Alpha + Zygisk Next + Shamiko, Apatch + Cherish Peekaboo + NoHello, and Magisk Delta. 

By defining Magisk fork as rooting solutions including Magisk, KSU, Apatch, and their branches, the development of bypassing can be briefly described as follows. 

- Magisk + Xposed (2018 and before), 
- Magisk + Edxposed (2019), 
- Magisk + Edxposed + Anti-blocking plugins (2020), 
- Magisk + LSPosed (2021), 
- Magisk Fork + LSPosed (2022), 
- Magisk Fork + LSPosed + Shamiko (2023), 
- Magisk Fork + LSPosed + Shamiko + PIF + TS (2024), and
- Magisk Fork + LSPosed + SUSFS/Shamiko/NoHello + PIF + TS + VBMeta Fixer + Cleaning up (2025). 

Currently, even with the state-of-the-art bypassing techniques, the following problems still cannot be solved with appropriate solutions. 

- Hide custom ROMs
- Hide USB debugging and even developer options without injection traces detected
- Hide accessibility mode (even the affected application cannot detect accessibility mode) without injection traces detected
- Solve the problem that WeChat fails to enable fingerprint payment while all other applications can use it normally
- Solve the problem that the STRONG integrity check cannot be passed on devices with the bootloader unlocked when there is no valid keybox
- Hide injection traces for applications injected at the application level

While following the tutorials, please also consider referring to the documentation and the ``Actions`` tab of the GitHub repositories for each rooting solution, module, and plugin, if there are. 

### Using KernelSU (KSU) / KSU Next (KSUN) / SukiSU

- Install the latest [SukiSU](https://github.com/SukiSU-Ultra/SukiSU-Ultra/actions) (the latest build in the last successful CI construction action in the ``Actions`` tab of its GitHub repository)
  - Configure in the Super User tab of the SukiSU Manager
    - Grant root privileges to all applications requiring them
    - Use the default configurations for all the applications that do not require root privileges
    - Launch the applications requiring root privileges like the MT Manager and grant requests for root privileges in SukiSU
  - Deploy the system modules in the SukiSU layer
    - Install the latest [ReZygisk](https://github.com/PerformanC/ReZygisk/actions) module (the latest build in the last successful CI construction action in the ``Actions`` tab of its GitHub repository) in the SukiSU layer
    - Install the latest [SUSFS](https://github.com/sidex15/susfs4ksu-module) module in the SukiSU layer
    - Install the latest [LSPosed](https://github.com/JingMatrix/LSPosed/actions) module (the latest Release version in the last successful CI construction action in the ``Actions`` tab of the GitHub repository of the ``Jing Matrix`` fork) in the SukiSU layer
      - Reboot $\rightarrow$ Open the LSPosed Manager $\rightarrow$ Create the LSPosed parasite $\rightarrow$ Create a desktop shortcut to the LSPosed parasite $\rightarrow$ Disable the logs which could make LSPosed being detected and the LSPosed taskbar notification in the setting page of the LSPosed parasite $\rightarrow$ Uninstall the LSPosed Manager
      - Input ``*#*#5776733#*#*`` in the dialer (do not call) to open the LSPosed parasite if necessary (in case the desktop shortcut is missing)
      - Install the latest [HMA](https://t.me/HideMyApplist) plugin (the latest build in its Telegram) in the LSPosed layer
      - Set the target scope of the HMA plugin to **System Framework** only and enable the HMA plugin in the LSPosed Manager
      - Reboot the device
      - Configure the HMA
        - Hide HMA's icon from the launcher in the HMA's settings page
        - Set the three switches in Data Isolation to ``On``, ``Off``, and ``On`` in sequence in the HMA's settings page (may require root privileges)
        - Build appropriate whitelist (what applications the detectors can see) or blacklist (what applications the detectors cannot see) templates (can refer to [this tutorial](./HMA(L).md))
        - Except for the SukiSU Manager and the plugins, enable hiding for all user applications and system-pre-installed non-critical applications with suitable templates applied
    - Install the latest [Play Integrity FIx](https://github.com/KOWX712/PlayIntegrityFix) module in the SukiSU layer (See [https://github.com/TMLP-Team/TMLP-Detectors-and-Bypassers/tree/main/Implementers/Others](https://github.com/TMLP-Team/TMLP-Detectors-and-Bypassers/tree/main/Implementers/Others) if the original repository is unavailable)
    - Install the latest [Tricky Store](https://github.com/5ec1cff/TrickyStore) module in the SukiSU layer
      - Use the MT Manager to rename the ``keybox.xml`` file in the ``/data/adb/tricky_store/`` directory to ``keybox.xml.bak`` (``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``)
      - Search for a free recent ``keybox.xml`` in the Telegram channel [FreeKeyboxShare](https://t.me/FreeKeyboxShare) and use the MT Manager to move it to ``/data/adb/tricky_store/``
      - Use [Key Attestation](https://github.com/vvb2060/KeyAttestation) to check if it passes the Device (old Strong) integrity $\rightarrow$ Click ``/data/adb/tricky_store/keybox.xml.bak`` in the MT Manager and restore the backup if not
      - Please try to generate a ``keybox.xml`` that can pass the Basic (old Device) integrity via a Python script from [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) if the free ``keybox.xml`` does not work or the ``keybox.xml`` signed based on the root certificate from the AOSP is not wished to be used
      - Never buy a ``keybox.xml`` unless the seller guarantees to offer you a new valid one once the previous one is revoked since each ``keybox.xml`` will be revoked by Google in a short period usually
      - Use the MT Manager to extract the installation package names of the detectors (long press to copy) and add them to ``/data/adb/tricky_store/target.txt`` (blacklist mode)
    - Use the MT Manager to write the date of the 1st day of the current month to ``/data/adb/tricky_store/security_patch.txt`` in the form of ``20250401``
    - Install the latest [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) module in the SukiSU layer if the device does not have a proper vbmeta digest
- View [https://www.reddit.com/r/Magisk/comments/1i7sowe/tutorial_susfs_best_root_hiding_method_currently/](https://www.reddit.com/r/Magisk/comments/1i7sowe/tutorial_susfs_best_root_hiding_method_currently/) in English if necessary. 

### Using Official Magisk (Including Release, Beta, Canary, Debug, and Nightly Versions) or Magisk Alpha

- Install the latest [Magisk Alpha](https://install.appcenter.ms/users/vvb2060/apps/magisk/distribution_groups/public)
  - Configure the Magisk
    - Disable built-in Zygisk
    - Disable Denylist
    - Empty Denylist
    - Launch the applications requiring root privileges like the MT Manager and grant requests for root privileges in Magisk
  - Install the latest [Zygisk Next](https://github.com/Dr-TSNG/ZygiskNext) module in the Magisk layer
    - Disable the Denylist in Zygisk Next
  - Install the latest [Shamiko](https://github.com/LSPosed/LSPosed.github.io/releases/) module in the Magisk layer
    - Use the MT Manager to create an empty file named ``whitelist`` under ``/data/adb/shamiko/`` (or execute the command ``touch /data/adb/shamiko/whitelist`` as root)
  - Install the latest [LSPosed](https://github.com/JingMatrix/LSPosed/actions) module (the latest Release version in the last successful CI construction action in the ``Actions`` tab of the GitHub repository of the ``Jing Matrix`` fork) in the Magisk layer
    - Reboot $\rightarrow$ Open the LSPosed Manager $\rightarrow$ Create the LSPosed parasite $\rightarrow$ Create a desktop shortcut to the LSPosed parasite $\rightarrow$ Disable the logs which could make LSPosed being detected and the LSPosed taskbar notification in the setting page of the LSPosed parasite $\rightarrow$ Uninstall the LSPosed Manager
    - Input ``*#*#5776733#*#*`` in the dialer (do not call) to open the LSPosed parasite if necessary (in case the desktop shortcut is missing)
    - Install the latest [HMA](https://t.me/HideMyApplist) plugin (the latest build in its Telegram) in the LSPosed layer
    - Set the target scope of the HMA plugin to **System Framework** only and enable the HMA plugin in the LSPosed Manager
    - Reboot the device
    - Configure the HMA
      - Hide HMA's icon from the launcher in the HMA's settings page
      - Set the three switches in Data Isolation to ``On``, ``Off``, and ``On`` in sequence in the HMA's settings page (may require root privileges)
      - Build appropriate whitelist (what applications the detectors can see) or blacklist (what applications the detectors cannot see) templates (can refer to [this tutorial](./HMA(L).md))
      - Except for the Magisk Manager and the plugins, enable hiding for all user applications and system-pre-installed non-critical applications with suitable templates applied
  - Install the latest [Play Integrity FIx](https://github.com/KOWX712/PlayIntegrityFix) module in the Magisk layer (See [https://github.com/TMLP-Team/TMLP-Detectors-and-Bypassers/tree/main/Implementers/Others](https://github.com/TMLP-Team/TMLP-Detectors-and-Bypassers/tree/main/Implementers/Others) if the original repository is unavailable)
  - Install the latest [Tricky Store](https://github.com/5ec1cff/TrickyStore) module in the Magisk layer
    - Use the MT Manager to rename the ``keybox.xml`` file in the ``/data/adb/tricky_store/`` directory to ``keybox.xml.bak`` (``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``)
    - Search for a free recent ``keybox.xml`` in the Telegram channel [FreeKeyboxShare](https://t.me/FreeKeyboxShare) and use the MT Manager to move it to ``/data/adb/tricky_store/``
    - Use [Key Attestation](https://github.com/vvb2060/KeyAttestation) to check if it passes the Device (old Strong) integrity $\rightarrow$ Click ``/data/adb/tricky_store/keybox.xml.bak`` in the MT Manager and restore the backup if not
    - Please try to generate a ``keybox.xml`` that can pass the Basic (old Device) integrity via a Python script from [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) if the free ``keybox.xml`` does not work or the ``keybox.xml`` signed based on the root certificate from the AOSP is not wished to be used
    - Never buy a ``keybox.xml`` unless the seller guarantees to offer you a new valid one once the previous one is revoked since each ``keybox.xml`` will be revoked by Google in a short period usually
    - Use the MT Manager to extract the installation package names of the detectors (long press to copy) and add them to ``/data/adb/tricky_store/target.txt`` (blacklist mode)
    - Use the MT Manager to write the date of the 1st day of the current month to ``/data/adb/tricky_store/security_patch.txt`` in the form of ``20250401``
  - Install the latest [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) module in the Magisk layer if the device does not have a proper vbmeta digest
  - Install the latest [bindhosts](https://github.com/backslashxx/bindhosts) or the built-in ``Systemless hosts`` module in the Magisk layer
    - Please remove the other one if one is selected to be used since they are not compatible
    - After rebooting, click the "Action" button of this module one or more times in the Magisk Manager to make it display "reset" and then click the "Action" button again to apply the latest rules if using the bindhosts module

### Using Apatch / Apatch Next

- Install the latest [Apatch](https://github.com/bmax121/APatch/actions) (the latest build in the last successful CI construction action in the ``Actions`` tab of its GitHub repository)
  - Configure in the Super User tab of the Apatch Manager
    - Grant root privileges to all applications requiring them
    - Use the default configurations for all the applications that do not require root privileges
      - The Apatch Manager Super User page seems to have a bug and you can: 
        - Grant root privileges to the MT Manager
        - Directly use the MT Manager to remove all application configurations except ``bin.mt.plus`` from the file ``/data/adb/ap/package_config``
        - Reboot the device and use Apatch Manager again to grant root privileges to applications that require them
  - Deploy the kernel module in the Apatch layer
    - Pease back up the original ``boot.img`` and the current ``boot.img`` before operations
    - Find the latest version of the module Cherish Peekaboo from [https://t.me/app_process64](https://t.me/app_process64)
    - Embed the non-``compat`` version of the Cherish Peekaboo as a kernel module and reboot
    - If devices cannot boot, then
      - Flash the ``boot.img`` that is backed up before in the fastboot mode to restore
      - Embed the latest ``compat`` version of the Cherish Peekaboo
      - Reboot
      - If devices cannot boot, then flash the ``boot.img`` that is backed up before in the fastboot mode to restore
  - Deploy the system modules in the Apatch layer
    - Install the latest [ReZygisk](https://github.com/PerformanC/ReZygisk/actions) module (the latest build in the last successful CI construction action in the ``Actions`` tab of its GitHub repository) in the Apatch layer
    - Install the latest [NoHello](https://github.com/MhmRdd/NoHello) module in the Apatch layer
      - Use the MT Manager to create an empty file named ``whitelist`` under ``/data/adb/nohello/`` (or execute the command ``touch /data/adb/nohello/whitelist`` as root)
    - Install the latest [LSPosed](https://github.com/JingMatrix/LSPosed/actions) module (the latest Release version in the last successful CI construction action in the ``Actions`` tab of the GitHub repository of the ``Jing Matrix`` fork) in the Apatch layer
      - Reboot $\rightarrow$ Open the LSPosed Manager $\rightarrow$ Create the LSPosed parasite $\rightarrow$ Create a desktop shortcut to the LSPosed parasite $\rightarrow$ Disable the logs which could make LSPosed being detected and the LSPosed taskbar notification in the setting page of the LSPosed parasite $\rightarrow$ Uninstall the LSPosed Manager
      - Input ``*#*#5776733#*#*`` in the dialer (do not call) to open the LSPosed parasite if necessary (in case the desktop shortcut is missing)
      - Install the latest [HMA](https://t.me/HideMyApplist) plugin (the latest build in its Telegram) in the LSPosed layer
      - Set the target scope of the HMA plugin to **System Framework** only and enable the HMA plugin in the LSPosed Manager
      - Reboot the device
      - Configure the HMA
        - Hide HMA's icon from the launcher in the HMA's settings page
        - Set the three switches in Data Isolation to ``On``, ``Off``, and ``On`` in sequence in the HMA's settings page (may require root privileges)
        - Build appropriate whitelist (what applications the detectors can see) or blacklist (what applications the detectors cannot see) templates (can refer to [this tutorial](./HMA(L).md))
        - Except for the Apatch Manager and the plugins, enable hiding for all user applications and system-pre-installed non-critical applications with suitable templates applied
    - Install the latest [Play Integrity FIx](https://github.com/KOWX712/PlayIntegrityFix) module in the Apatch layer (See [https://github.com/TMLP-Team/TMLP-Detectors-and-Bypassers/tree/main/Implementers/Others](https://github.com/TMLP-Team/TMLP-Detectors-and-Bypassers/tree/main/Implementers/Others) if the original repository is unavailable)
    - Install the latest [Tricky Store](https://github.com/5ec1cff/TrickyStore) module in the Apatch layer
      - Use the MT Manager to rename the ``keybox.xml`` file in the ``/data/adb/tricky_store/`` directory to ``keybox.xml.bak`` (``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``)
      - Search for a free recent ``keybox.xml`` in the Telegram channel [FreeKeyboxShare](https://t.me/FreeKeyboxShare) and use the MT Manager to move it to ``/data/adb/tricky_store/``
      - Use [Key Attestation](https://github.com/vvb2060/KeyAttestation) to check if it passes the Device (old Strong) integrity $\rightarrow$ Click ``/data/adb/tricky_store/keybox.xml.bak`` in the MT Manager and restore the backup if not
      - Please try to generate a ``keybox.xml`` that can pass the Basic (old Device) integrity via a Python script from [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) if the free ``keybox.xml`` does not work or the ``keybox.xml`` signed based on the root certificate from the AOSP is not wished to be used
      - Never buy a ``keybox.xml`` unless the seller guarantees to offer you a new valid one once the previous one is revoked since each ``keybox.xml`` will be revoked by Google in a short period usually
      - Use the MT Manager to extract the installation package names of the detectors (long press to copy) and add them to ``/data/adb/tricky_store/target.txt`` (blacklist mode)
    - Use the MT Manager to write the date of the 1st day of the current month to ``/data/adb/tricky_store/security_patch.txt`` in the form of ``20250501``
    - Install the latest [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) module in the Apatch layer if the device does not have a proper vbmeta digest

### Using Magisk Delta

- Install the last version of [Magisk Delta](https://github.com/HuskyDG/magisk-files) before it was discontinued
  - Please consider switching to Magisk Alpha since it is already out-of-date (discontinued in early 2024) and the versions before Magisk 27007 have a privilege escalation vulnerability
  - Configure Magisk Delta
    - Enable Zygisk (or use [NeoZygisk](https://github.com/JingMatrix/NeoZygisk/actions))
    - Enable whitelist mode on the setting page of the Magisk Delta
    - Select the package of the application that requires root privileges (you can only select the necessary packages in the applications)
  - Install the latest [LSPosed](https://github.com/JingMatrix/LSPosed/actions) module (the latest Release version in the last successful CI construction action in the ``Actions`` tab of the GitHub repository of the ``Jing Matrix`` fork) in the Magisk layer
    - Reboot $\rightarrow$ Open the LSPosed Manager $\rightarrow$ Create the LSPosed parasite $\rightarrow$ Create a desktop shortcut to the LSPosed parasite $\rightarrow$ Disable the logs which could make LSPosed being detected and the LSPosed taskbar notification in the setting page of the LSPosed parasite $\rightarrow$ Uninstall the LSPosed Manager
    - Input ``*#*#5776733#*#*`` in the dialer (do not call) to open the LSPosed parasite if necessary (in case the desktop shortcut is missing)
    - Install the latest [HMA](https://t.me/HideMyApplist) plugin (the latest build in its Telegram) in the LSPosed layer
    - Set the target scope of the HMA plugin to **System Framework** only and enable the HMA plugin in the LSPosed Manager
    - Reboot the device
    - Configure the HMA
      - Hide HMA's icon from the launcher in the HMA's settings page
      - Set the three switches in Data Isolation to ``On``, ``Off``, and ``On`` in sequence in the HMA's settings page (may require root privileges)
      - Build appropriate whitelist (what applications the detectors can see) or blacklist (what applications the detectors cannot see) templates (can refer to [this tutorial](./HMA(L).md))
      - Except for the Magisk Manager and the plugins, enable hiding for all user applications and system-pre-installed non-critical applications with suitable templates applied
  - Install the latest [Play Integrity FIx](https://github.com/KOWX712/PlayIntegrityFix) module in the Magisk layer (See [https://github.com/TMLP-Team/TMLP-Detectors-and-Bypassers/tree/main/Implementers/Others](https://github.com/TMLP-Team/TMLP-Detectors-and-Bypassers/tree/main/Implementers/Others) if the original repository is unavailable)
  - Install the latest [Tricky Store](https://github.com/5ec1cff/TrickyStore) module in the Magisk layer
    - Use the MT Manager to rename the ``keybox.xml`` file in the ``/data/adb/tricky_store/`` directory to ``keybox.xml.bak`` (``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``)
    - Search for a free recent ``keybox.xml`` in the Telegram channel [FreeKeyboxShare](https://t.me/FreeKeyboxShare) and use the MT Manager to move it to ``/data/adb/tricky_store/``
    - Use [Key Attestation](https://github.com/vvb2060/KeyAttestation) to check if it passes the Device (old Strong) integrity $\rightarrow$ Click ``/data/adb/tricky_store/keybox.xml.bak`` in the MT Manager and restore the backup if not
    - Please try to generate a ``keybox.xml`` that can pass the Basic (old Device) integrity via a Python script from [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) if the free ``keybox.xml`` does not work or the ``keybox.xml`` signed based on the root certificate from the AOSP is not wished to be used
    - Never buy a ``keybox.xml`` unless the seller guarantees to offer you a new valid one once the previous one is revoked since each ``keybox.xml`` will be revoked by Google in a short period usually
    - Use the MT Manager to extract the installation package names of the detectors (long press to copy) and add them to ``/data/adb/tricky_store/target.txt`` (blacklist mode)
    - Use the MT Manager to write the date of the 1st day of the current month to ``/data/adb/tricky_store/security_patch.txt`` in the form of ``20250401``
  - Install the latest [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) module in the Magisk layer if the device does not have a proper vbmeta digest
  - Install the latest [bindhosts](https://github.com/backslashxx/bindhosts) or the built-in ``Systemless hosts`` module in the Magisk layer
    - Please remove the other one if one is selected to be used since they are not compatible
    - After rebooting, click the "Action" button of this module one or more times in the Magisk Manager to make it display "reset" and then click the "Action" button again to apply the latest rules if using the bindhosts module

### Special Cases

#### Momo

##### Package management service exception

Turn off "Disable package manager signature verification" in Core Patcher by referring to [a post in early 2023](https://zhidao.baidu.com/question/633770792883881924.html)

##### Debugging mode is enabled

- Turn off the debugging mode when not in use
- It is not recommended to use plugins for bypassing because it will expose Xposed/Edxposed/LSPosed injection/hooks (confident level), which is not worth the loss though injecting the detection application can pass the debug mode (suspicious level)

##### Detect the existence of TWRP file(s)

Rename the TWRP folder under ``/sdcard/`` (for example, .TWRP)

##### Unlocked bootloader

- Install [Play Integrity FIx](https://github.com/KOWX712/PlayIntegrityFix) module
- It is not recommended to use plugins for bypassing because it will expose Xposed/Edxposed/LSPosed injection/hooks (confident level), which is not worth the loss though the injection of the detected application can pass the debug mode (suspicious level)

#### Ruru

##### Found HMA in ``syscall``

- Before June 24th, 2025: Switch to HMAL
- On or after June 24th, 2025: Install the latest HMA plugin

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

##### Mount inconsistency detected / Magic Mount Detected

- Magisk and its branches: Use Magisk Alpha and install the latest Shamiko module
- Apatch and its branches: Embed the Cherish Peekaboo module as a kernel module (please check if the ``compat`` version is needed)
- KSU and its branches: Use SukiSU and Install the latest SUSFS module as a system module

##### Risky application detected (bypassed HMA(L) with Code 3)

The logic of this detection is to start an activity of the target application under Android 13. This detection is handled by ``HMA_v3.5`` from June 24th, 2025. 

##### Risky application detected (bypassed HMA(L) with Code 4)

The logic of this detection is to find folders named by the application package names recorded in the library under certain specific directories. Please try to check whether there is a folder named by the listed package names found by the detector in ``/sdcard/Android/data``. If the folder is empty, you can try to delete it. 
If necessary, please assign the listed application package names found by the detector to the variable ``packageNames`` with a space character as the separator. Subsequently, execute the following script as a non-root user to observe which folders named by the package names can be detected by applications without root permissions. 

```
#!/system/bin/sh
readonly EXIT_SUCCESS=0
readonly EXIT_FAILURE=1
exitCode=${EXIT_SUCCESS}
folders="/data/data /data/user/0 /data/user_de/0 /sdcard/Android/data"
packageNames="bin.mt.plus bin.mt.termex com.rifsxd.ksunext com.sukisu.ultra com.topjohnwu.magisk io.github.huskydg.magisk io.github.vvb2060.magisk me.bmax.apatch me.garfieldhan.apatch.next me.weishu.kernelsu"
for packageName in ${packageNames}
do
	for folder in ${folders}
	do
		if [[ -e "${folder}/${packageName}" ]];
		then
			exitCode=${EXIT_FAILURE}
			echo "Found \"${folder}/${packageName}\". "
		fi
	done
done
exit ${exitCode}
```

#### Native Test

##### Versions from ``v26.0`` to the invitial ``v30.0`` reports "Malicious Hook"

- It can be a false positive since "Malicious Hook" was redefined in these versions
- Please use the latest version to check the environments. 

##### Others

Please refer to [https://bbs.kanxue.com/thread-285106-1.htm](https://bbs.kanxue.com/thread-285106-1.htm)

#### Postal Savings Bank

##### Around September 2023, the latest official mask and the latest Shamiko at that time were used, but the crash still occurred

- Caused by historical issues, updating can solve the problem
- Using the official Magisk or Magisk Alpha
  - If you were using the official Magisk or Magisk Alpha in around September 2023, please switch to the latest Magisk Delta
  - If you are using the official Magisk or Magisk Alpha today, please install the latest Magisk Alpha and the latest Shamiko module
- Using the Magisk Delta
  - If you were using the Magisk Delta in around September 2023, please install the latest Magisk Delta (the Magisk Delta at that time would not cause the Postal Savings Bank to crash)
  - If you are using the Magisk Delta today, please switch to the latest Magisk Alpha and install the latest Shamiko module

#### QQ

##### Logging out users with no reasons, account login limitations, or temporary account freezing

- Mobile QQ (Android)
  - The definition of downgrading: Do not expose any suspicious environment (including root and injection environment) or perform any injection to QQ and use the core patcher plugin to downgrade QQ after 15 days (and observe for another 15 days)
  - If you are using a QQ version at or below ``v8.6.0``
    - Never upgrade the QQ until the update is a must
    - Upgrade to the minimum version above the current version if the update is a must
  - If you are using a QQ version within the interval (``v8.6.0``, ``v8.8.17``] that is affected by the 2021 spring and summer risk control event (the phenomenon is most obvious when using the ``v8.8.0`` version)
    - If you want to use the QXposed (QX) plugin or the QQ Repeater plugin while you can still downgrade your QQ
      - Switch to the ``v8.6.0`` or lower version (if rollback is still allowed)
    - Otherwise
      - Uninstall the QXposed (QX) plugin and the QQ Repeater plugin
      - Disable the red envelope grabbing, automatic group sign-in, and the group messaging functions
      - Uninstall any QQ plugin that is not adapted to the Xposed API calling protection of LSPosed
  - If you are using a QQ version within the interval (``v8.8.17``, ``v8.9.56``]
    - Never upgrade the QQ until the update is a must
    - Upgrade to the minimum version above the current version if the update is a must
    - Uninstall the QXposed (QX) plugin and the QQ Repeater plugin
    - Disable the red envelope grabbing, automatic group sign-in, and the group messaging functions
    - Uninstall any QQ plugin that is not adpated to the Xposed API calling protection of LSPosed
  - If you are using a QQ version above ``v8.9.56`` that is affected by the 2024 autumn to 2025 spring risk control event (the phenomenon is most obvious when using the ``v9.1.35`` version)
    - Please refer to the issues mentioned in (``v8.8.17``, ``v8.9.56``]
    - If you want to use the XAutoDaily (XA) plugin or the QAuxiliary (QA) plugin while you can still downgrade your QQ
      - Make sure that you have already hidden the rooting and injection environments according to the common procedures shown in this page
      - In the QAuxiliary (QA) plugin, turn on the "disable QQ hot patch" switch and turn off the "environment detection package (trpc.o3.*) interception" switch
      - Switch to the ``v9.1.31`` or lower versions, 
      - Switch to the ``v9.0.95`` or lower versions, or
      - Switch to the ``v8.9.56`` or lower versions (if accepting non-NT architecture)
    - Otherwise
      - Uninstall all the QQ plugins
      - Disable the red envelope grabbing, automatic group sign-in, and the group messaging functions
      - Do not expose any suspicious environment (including root and injection environment) or perform any injection to QQ (remember to disable QQ in advance when switching environments) when using versions above ``v9.1.31``
- Computer QQ (Windows): Always use the nostalgic version instead of the QQNT version

#### WeChat

##### Failed to open the fingerprint payment prompt (but other domestic and foreign applications can use fingerprints normally)

- Temporary solution: Use the WeChat Payment module or the WeChat Payment plugin (the principle is to submit the pre-stored password after passing the fingerprint)
- Essential solution: None

---

## 过检方法

目前，SukiSU + ReZygisk + SUSFS 是最好的解决方案，其次为 Magisk Alpha + Zygisk Next + Shamiko、Apatch + Cherish Peekaboo + NoHello 和 Magisk Delta。

通过将 Magisk Fork 定义为包括 Magisk、KSU、Apatch 及其分支在内的 root 方案，过检的发展历程可以简要描述如下。

- Magisk + Xposed（2018 年及之前版本）；
- Magisk + Edxposed（2019 年）；
- Magisk + Edxposed + 各系防封检测插件（2020 年）；
- Magisk + LSPosed（2021 年）；
- Magisk Fork + LSPosed（2022 年）；
- Magisk Fork + LSPosed + Shamiko（2023 年）；
- Magisk Fork + LSPosed + Shamiko + PIF + TS（2024 年）；以及
- Magisk Fork + LSPosed + SUSFS/Shamiko/NoHello + PIF + TS + VBMeta Fixer + 残留清理（2025 年）。

目前，即使使用了最先进的过检技术，以下问题依旧无法使用合适的方案解决。

- 隐藏自定义 ROM
- 隐藏 USB 调试甚至开发者选项
- 隐藏无障碍模式（甚至被作用的应用也无法检测到无障碍模式）
- 解决微信指纹支付开启失败而其它应用软件都能正常使用的问题
- 解决无合法 keybox 时无法在已解锁 bootloader 的设备上通过 STRONG 完整性检验
- 对被应用层注入的应用隐藏注入痕迹

在遵循教程的同时，还请考虑参考每个 root 方案、模块和插件的使用文档和 GitHub 存储库的 ``Actions`` 选项卡（如有）。

### 正在使用 KernelSU (KSU) / KSU Next (KSUN) / SukiSU

- 安装 SukiSU GitHub 存储库的 ``Actions`` 选项卡中最后一次成功生成构建的 action 内生成的最新版 [SukiSU](https://github.com/SukiSU-Ultra/SukiSU-Ultra/actions)
  - 在 SukiSU 管理器的超级用户页内进行配置
    - 将所有需要 root 的应用程序进行授权
    - 让剩余应用中所有不需要 root 权限的应用使用默认设置（重置设置）
    - 启动 MT 管理器和其它需要 root 权限的应用程序并用 SukiSU 管理器进行授权
  - 在 SukiSU 层部署系统模块
    - 在 SukiSU 层安装 GitHub 存储库的 ``Actions`` 选项卡中最后一次成功生成构建的 action 内生成的最新版 [ReZygisk](https://github.com/PerformanC/ReZygisk/actions) 模块
    - 在 SukiSU 层安装最新版 [SUSFS](https://github.com/sidex15/susfs4ksu-module) 模块
    - 在 SukiSU 层安装 ``Jing Matrix`` 分支 GitHub 存储库的 ``Actions`` 选项卡中最后一次成功生成构建的 action 内生成的最新 Release 版的 [LSPosed](https://github.com/JingMatrix/LSPosed/actions) 模块
      - 重启设备 $\rightarrow$ 打开 LSPosed 管理器 $\rightarrow$ 创建 LSPosed 寄生器 $\rightarrow$ 创建寄生器快捷方式 $\rightarrow$ 关闭可能导致 LSPosed 被检测到的日志功能和 LSPosed 的任务栏通知 $\rightarrow$ 卸载 LSPosed 管理器
      - 如有需要可使用拨号键拨号 ``*#*#5776733#*#*``（不用呼叫）打开 LSPosed 寄生器（例如在桌面快捷方式丢失的情况下）
      - 在 LSPosed 层安装 HMA 官方 Telegram 发布的最新版 [HMA](https://t.me/HideMyApplist) 插件
      - 设置作用域为仅**系统框架**并启用插件
      - 重启设备
      - 配置 HMA 插件
        - 在 HMA 的设置页面将 HMA 的图标从启动器中隐藏
        - 在 HMA 的设置页面将数据隔离中的三个开关依次设置为开、关、开（部分修改需要 root 权限）
        - 构建适当的白名单（只想让检测软件检测到哪些应用）或黑名单（让检测软件不能检测到哪些应用）模板（可参照[该教程](./HMA(L).md)）
        - 对除面具和插件之外的一切用户应用和系统预装的非关键应用启用隐藏并应用模板
    - 在 SukiSU 层安装 [Play Integrity FIx](https://github.com/KOWX712/PlayIntegrityFix) 模块
    - 在 SukiSU 层安装 [Tricky Store](https://github.com/5ec1cff/TrickyStore) 模块
      - 使用 MT 管理器将 ``/data/adb/tricky_store/`` 目录下的 ``keybox.xml`` 文件重命名为 ``keybox.xml.bak``（``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``）
      - 在电报频道 [FreeKeyboxShare](https://t.me/FreeKeyboxShare) 搜索一个最近的免费 ``keybox.xml`` 并使用 MT 管理器将其移动到 ``/data/adb/tricky_store/`` 目录下
      - 使用 [Key Attestation](https://github.com/vvb2060/KeyAttestation) 检验是否通过 Device（旧 Strong）完整性等级，如果不是，请在 MT 管理器中单击 ``/data/adb/tricky_store/keybox.xml.bak`` 并恢复备份
      - 如果免费 ``keybox.xml`` 无效或不希望使用基于安卓开源项目根证书签署的 ``keybox.xml``，请尝试使用来自 [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) 的 Python 脚本来生成一个 可以通过 Basic（旧 Device）完整性等级的 ``keybox.xml``
      - 永远不要购买 ``keybox.xml``，除非卖家保证在之前的 ``keybox.xml`` 被撤销后立即为您提供一个新的且有效的 ``keybox.xml`` 因为每个 ``keybox.xml`` 通常会在短时间内被 Google 撤销
      - 使用 MT 管理器提取检测应用的安装包包名（可以长按复制）并编辑 ``/data/adb/tricky_store/target.txt`` 将所有目标应用的包名添加进去（黑名单模式）
    - 使用 MT 管理器编辑 ``/data/adb/tricky_store/security_patch.txt`` 并将当月的 1 号的日期按照 ``20250401`` 的格式写入该文件
    - 若设备的 vbmeta digest 不正确可在 SukiSU 层安装 [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) 模块
- 如有需要，请参阅英文帖子 [https://www.reddit.com/r/Magisk/comments/1i7sowe/tutorial_susfs_best_root_hiding_method_currently/](https://www.reddit.com/r/Magisk/comments/1i7sowe/tutorial_susfs_best_root_hiding_method_currently/)。

### 正在使用官方版（含发行版、Beta 版、金丝雀版、Debug 版和每夜版）或 Alpha 版面具

- 安装最新版 [Alpha 版面具](https://install.appcenter.ms/users/vvb2060/apps/magisk/distribution_groups/public)
  - 配置面具
    - 禁用内置 Zygisk
    - 关闭“遵守排除列表”开关
    - 清空“配置排除列表”列表
    - 启动 MT 管理器和其它需要 root 权限的应用程序并用 Magisk 管理器进行授权
  - 在面具层安装最新版 [Zygisk Next](https://github.com/Dr-TSNG/ZygiskNext) 模块
    - 禁用 Zygisk Next 内的遵守排除列表
  - 在面具层安装最新版 [Shamiko](https://github.com/LSPosed/LSPosed.github.io/releases/) 模块
    - 使用 MT 管理器在 ``/data/adb/shamiko/`` 目录下创建一个名为 ``whitelist`` 的空文件（或直接在 root 下执行 ``touch /data/adb/shamiko/whitelist`` 命令）
  - 在面具层安装 ``Jing Matrix`` 分支 GitHub 存储库的 ``Actions`` 选项卡中最后一次成功生成构建的 action 内生成的最新 Release 版的 [LSPosed](https://github.com/JingMatrix/LSPosed/actions) 模块
    - 重启设备 $\rightarrow$ 打开 LSPosed 管理器 $\rightarrow$ 创建 LSPosed 寄生器 $\rightarrow$ 创建寄生器快捷方式 $\rightarrow$ 关闭可能导致 LSPosed 被检测到的日志功能和 LSPosed 的任务栏通知 $\rightarrow$ 卸载 LSPosed 管理器
    - 如有需要可使用拨号键拨号 ``*#*#5776733#*#*``（不用呼叫）打开 LSPosed 寄生器（例如在桌面快捷方式丢失的情况下）
    - 在 LSPosed 层安装 HMA 官方 Telegram 发布的最新版 [HMA](https://t.me/HideMyApplist) 插件
    - 设置作用域为仅**系统框架**并启用插件
    - 重启设备
    - 配置 HMA 插件
      - 在 HMA 的设置页面将 HMA 的图标从启动器中隐藏
      - 在 HMA 的设置页面将数据隔离中的三个开关依次设置为开、关、开（部分修改需要 root 权限）
      - 构建适当的白名单（只想让检测软件检测到哪些应用）或黑名单（让检测软件不能检测到哪些应用）模板（可参照[该教程](./HMA(L).md)）
      - 对除面具和插件之外的一切用户应用和系统预装的非关键应用启用隐藏并应用模板
  - 在面具层安装 [Play Integrity FIx](https://github.com/KOWX712/PlayIntegrityFix) 模块
  - 在面具层安装 [Tricky Store](https://github.com/5ec1cff/TrickyStore) 模块
    - 使用 MT 管理器将 ``/data/adb/tricky_store/`` 目录下的 ``keybox.xml`` 文件重命名为 ``keybox.xml.bak``（``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``）
    - 在电报频道 [FreeKeyboxShare](https://t.me/FreeKeyboxShare) 搜索一个最近的免费 ``keybox.xml`` 并使用 MT 管理器将其移动到 ``/data/adb/tricky_store/`` 目录下
    - 使用 [Key Attestation](https://github.com/vvb2060/KeyAttestation) 检验是否通过 Device（旧 Strong）完整性等级，如果不是，请在 MT 管理器中单击 ``/data/adb/tricky_store/keybox.xml.bak`` 并恢复备份
    - 如果免费 ``keybox.xml`` 无效或不希望使用基于安卓开源项目根证书签署的 ``keybox.xml``，请尝试使用来自 [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) 的 Python 脚本来生成一个 可以通过 Basic（旧 Device）完整性等级的 ``keybox.xml``
    - 永远不要购买 ``keybox.xml``，除非卖家保证在之前的 ``keybox.xml`` 被撤销后立即为您提供一个新的且有效的 ``keybox.xml`` 因为每个 ``keybox.xml`` 通常会在短时间内被 Google 撤销
    - 使用 MT 管理器提取检测应用的安装包包名（可以长按复制）并编辑 ``/data/adb/tricky_store/target.txt`` 将所有目标应用的包名添加进去（黑名单模式）
    - 使用 MT 管理器编辑 ``/data/adb/tricky_store/security_patch.txt`` 并将当月的 1 号的日期按照 ``20250401`` 的格式写入该文件
  - 若设备的 vbmeta digest 不正确可在面具层安装 [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) 模块
  - 在面具层安装 [bindhosts](https://github.com/backslashxx/bindhosts) 或内置的 Systemless hosts 模块
    - 由于两者不兼容，如果决定使用两者中的某一个模块，请移除另一个模块
    - 如果使用 bindhosts，请在重启设备后在面具管理器中点击一次或多次该模块的“操作”按钮使其显示 ``reset`` 后再点一次“操作”按钮使其应用最新规则

### 正在使用 Apatch / Apatch Next

- 安装 Apatch GitHub 存储库的 ``Actions`` 选项卡中最后一次成功生成构建的 action 内生成的最新版 [Apatch](https://github.com/bmax121/APatch/actions)
  - 在 Apatch 管理器的超级用户页内进行配置
    - 将所有需要 root 的应用程序进行授权
    - 让剩余应用中所有不需要 root 权限的应用使用默认设置（重置设置）
      - Apatch 管理器超级用户页面似乎有 bug，若在重置过程中遇到，可：
        - 直接在授予 MT 管理器 root 权限
        - 使用 MT 管理器从文件 ``/data/adb/ap/package_config`` 中移除除 ``bin.mt.plus`` 以外的所有应用配置
        - 在重启设备后再次使用 Apatch 管理器将 root 权限授予需要 root 权限的应用
- 在 Apatch 层部署内核模块
  - 请在操作前备份原始的 ``boot.img`` 和当前的 ``boot.img``
  - 从 [https://t.me/app_process64](https://t.me/app_process64) 查找 Cherish Peekaboo 模块的最新版本
  - 将非 ``compat`` 版本的 Cherish Peekaboo 以内核模块的形式嵌入并重新启动
  - 如果设备无法启动，那么
    - 请在 fastboot 模式下刷入先前备份的 ``boot.img`` 进行还原
    - 重启进入系统后在 Apatch 管理器中嵌入最新 ``compat`` 版本的 Cherish Peekaboo 并重启设备
    - 如果设备无法启动，请在 fastboot 模式下刷入先前备份的 ``boot.img`` 进行还原并放弃内核模块部署
  - 在 Apatch 层部署系统模块
    - 在 Apatch 层安装 GitHub 存储库的 ``Actions`` 选项卡中最后一次成功生成构建的 action 内生成的最新版 [ReZygisk](https://github.com/PerformanC/ReZygisk/actions) 模块
    - 在 Apatch 层安装最新版 [NoHello](https://github.com/MhmRdd/NoHello) 模块
      - 使用 MT 管理器在 ``/data/adb/nohello/`` 目录下创建一个名为 ``whitelist`` 的空文件（或直接在 root 下执行 ``touch /data/adb/nohello/whitelist`` 命令）
    - 在 Apatch 层安装 ``Jing Matrix`` 分支 GitHub 存储库的 ``Actions`` 选项卡中最后一次成功生成构建的 action 内生成的最新 Release 版的 [LSPosed](https://github.com/JingMatrix/LSPosed/actions) 模块
      - 重启设备 $\rightarrow$ 打开 LSPosed 管理器 $\rightarrow$ 创建 LSPosed 寄生器 $\rightarrow$ 创建寄生器快捷方式 $\rightarrow$ 关闭可能导致 LSPosed 被检测到的日志功能和 LSPosed 的任务栏通知 $\rightarrow$ 卸载 LSPosed 管理器
      - 如有需要可使用拨号键拨号 ``*#*#5776733#*#*``（不用呼叫）打开 LSPosed 寄生器（例如在桌面快捷方式丢失的情况下）
      - 在 LSPosed 层安装 HMA 官方 Telegram 发布的最新版 [HMA](https://t.me/HideMyApplist) 插件
      - 设置作用域为仅**系统框架**并启用插件
      - 重启设备
      - 配置 HMA 插件
        - 在 HMA 的设置页面将 HMA 的图标从启动器中隐藏
        - 在 HMA 的设置页面将数据隔离中的三个开关依次设置为开、关、开（部分修改需要 root 权限）
        - 构建适当的白名单（只想让检测软件检测到哪些应用）或黑名单（让检测软件不能检测到哪些应用）模板（可参照[该教程](./HMA(L).md)）
        - 对除面具和插件之外的一切用户应用和系统预装的非关键应用启用隐藏并应用模板
    - 在 Apatch 层安装 [Play Integrity FIx](https://github.com/KOWX712/PlayIntegrityFix) 模块
    - 在 Apatch 层安装 [Tricky Store](https://github.com/5ec1cff/TrickyStore) 模块
      - 使用 MT 管理器将 ``/data/adb/tricky_store/`` 目录下的 ``keybox.xml`` 文件重命名为 ``keybox.xml.bak``（``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``）
      - 在电报频道 [FreeKeyboxShare](https://t.me/FreeKeyboxShare) 搜索一个最近的免费 ``keybox.xml`` 并使用 MT 管理器将其移动到 ``/data/adb/tricky_store/`` 目录下
      - 使用 [Key Attestation](https://github.com/vvb2060/KeyAttestation) 检验是否通过 Device（旧 Strong）完整性等级，如果不是，请在 MT 管理器中单击 ``/data/adb/tricky_store/keybox.xml.bak`` 并恢复备份
      - 如果免费 ``keybox.xml`` 无效或不希望使用基于安卓开源项目根证书签署的 ``keybox.xml``，请尝试使用来自 [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) 的 Python 脚本来生成一个 可以通过 Basic（旧 Device）完整性等级的 ``keybox.xml``
      - 永远不要购买 ``keybox.xml``，除非卖家保证在之前的 ``keybox.xml`` 被撤销后立即为您提供一个新的且有效的 ``keybox.xml`` 因为每个 ``keybox.xml`` 通常会在短时间内被 Google 撤销
      - 使用 MT 管理器提取检测应用的安装包包名（可以长按复制）并编辑 ``/data/adb/tricky_store/target.txt`` 将所有目标应用的包名添加进去（黑名单模式）
    - 使用 MT 管理器编辑 ``/data/adb/tricky_store/security_patch.txt`` 并将当月的 1 号的日期按照 ``20250401`` 的格式写入该文件
    - 若设备的 vbmeta digest 不正确可在 Apatch 层安装 [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) 模块

### 正在使用 Delta 版面具（小狐狸面具）

- 安装停更前的最后一个版本的 [Delta 面具](https://github.com/HuskyDG/magisk-files)
  - 请考虑使用 Magisk Alpha 因为 Magisk Delta 已在 2024 年初停更且面具 27007 之前的版本存在提权漏洞
  - 配置面具
    - 打开 Zygisk（或使用 [NeoZygisk](https://github.com/JingMatrix/NeoZygisk/actions)）
    - 在设置界面启用白名单模式
    - 选定需要 root 权限的应用的包（可以不选定某个应用程序内的所有包）
  - 在面具层安装 ``Jing Matrix`` 分支 GitHub 存储库的 ``Actions`` 选项卡中最后一次成功生成构建的 action 内生成的最新 Release 版的 [LSPosed](https://github.com/JingMatrix/LSPosed/actions) 模块
    - 重启设备 $\rightarrow$ 打开 LSPosed 管理器 $\rightarrow$ 创建 LSPosed 寄生器 $\rightarrow$ 创建寄生器快捷方式 $\rightarrow$ 关闭可能导致 LSPosed 被检测到的日志功能和 LSPosed 的任务栏通知 $\rightarrow$ 卸载 LSPosed 管理器
    - 如有需要可使用拨号键拨号 ``*#*#5776733#*#*``（不用呼叫）打开 LSPosed 寄生器（例如在桌面快捷方式丢失的情况下）
    - 在 LSPosed 层安装 HMA 官方 Telegram 发布的最新版 [HMA](https://t.me/HideMyApplist) 插件
    - 设置作用域为仅**系统框架**并启用插件
    - 重启设备
    - 配置 HMA 插件
      - 在 HMA 的设置页面将 HMA 的图标从启动器中隐藏
      - 在 HMA 的设置页面将数据隔离中的三个开关依次设置为开、关、开（部分修改需要 root 权限）
      - 构建适当的白名单（只想让检测软件检测到哪些应用）或黑名单（让检测软件不能检测到哪些应用）模板（可参照[该教程](./HMA(L).md)）
      - 对除面具和插件之外的一切用户应用和系统预装的非关键应用启用隐藏并应用模板
  - 在面具层安装 [Play Integrity FIx](https://github.com/KOWX712/PlayIntegrityFix) 模块
  - 在面具层安装 [Tricky Store](https://github.com/5ec1cff/TrickyStore) 模块
    - 使用 MT 管理器将 ``/data/adb/tricky_store/`` 目录下的 ``keybox.xml`` 文件重命名为 ``keybox.xml.bak``（``mv /data/adb/tricky_store/keybox.xml /data/adb/tricky_store/keybox.xml.bak``）
    - 在电报频道 [FreeKeyboxShare](https://t.me/FreeKeyboxShare) 搜索一个最近的免费 ``keybox.xml`` 并使用 MT 管理器将其移动到 ``/data/adb/tricky_store/`` 目录下
    - 使用 [Key Attestation](https://github.com/vvb2060/KeyAttestation) 检验是否通过 Device（旧 Strong）完整性等级，如果不是，请在 MT 管理器中单击 ``/data/adb/tricky_store/keybox.xml.bak`` 并恢复备份
    - 如果免费 ``keybox.xml`` 无效或不希望使用基于安卓开源项目根证书签署的 ``keybox.xml``，请尝试使用来自 [https://github.com/TMLP-Team/keyboxGenerator](https://github.com/TMLP-Team/keyboxGenerator) 的 Python 脚本来生成一个 可以通过 Basic（旧 Device）完整性等级的 ``keybox.xml``
    - 永远不要购买 ``keybox.xml``，除非卖家保证在之前的 ``keybox.xml`` 被撤销后立即为您提供一个新的且有效的 ``keybox.xml`` 因为每个 ``keybox.xml`` 通常会在短时间内被 Google 撤销
    - 使用 MT 管理器提取检测应用的安装包包名（可以长按复制）并编辑 ``/data/adb/tricky_store/target.txt`` 将所有目标应用的包名添加进去（黑名单模式）
    - 使用 MT 管理器编辑 ``/data/adb/tricky_store/security_patch.txt`` 并将当月的 1 号的日期按照 ``20250401`` 的格式写入该文件
  - 若设备的 vbmeta digest 不正确可在面具层安装 [VBMeta Fixer](https://github.com/reveny/Android-VBMeta-Fixer) 模块
  - 在面具层安装 [bindhosts](https://github.com/backslashxx/bindhosts) 或内置的 Systemless hosts 模块
    - 由于两者不兼容，如果决定使用两者中的某一个模块，请移除另一个模块
    - 如果使用 bindhosts，请在重启设备后在面具管理器中点击一次或多次该模块的“操作”按钮使其显示 ``reset`` 后再点一次“操作”按钮使其应用最新规则

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

- 在面具层安装 [Play Integrity FIx](https://github.com/KOWX712/PlayIntegrityFix) 模块
- 不建议使用插件进行过检因为对检测应用注入虽然能够过检掉调试模式（可疑级别）但会暴露 Xposed/Edxposed/LSPosed 注入/钩子（确信级别）反而得不偿失

#### Ruru

##### ``syscall`` 找到 HMA

- 2025 年 6 月 24 日前：换用 HMAL
- 2025 年 6 月 25 日及之后：安装最新版 HMA 插件

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

##### 检测到挂载不一致 / 检测到 Magic Mount

- Magisk 系列：使用 Magisk Alpha 并安装最新版 Shamiko 模块
- Apatch 系列：以内核模块的形式嵌入 Cherish Peekaboo 模块（请自行排查是否需要 compat 版本）
- KSU 系列：使用 SukiSU 并安装最新版 SUSFS 模块

##### 检测到风险应用（绕过 HMA(L) 的代码 3）

该检测适用于安卓 13 以下的操作系统，通过启动目标应用的 Activity 实现检测，已于 2025 年 6 月 25 日在 ``HMA_v3.5.r449.1d951a3 (449)`` 中得到修复。

##### 检测到风险应用（绕过 HMA(L) 的代码 4）

该检测原理为找到了某些特定目录下存在以与库中记录的应用包名命名的文件夹，请尝试查看 ``/sdcard/Android/data`` 下是否存在以所列出包名命名的文件夹，如果该文件夹为空可尝试将其删除；
如有必要，请将所列出的应用包名以空格为分隔符赋值为变量 ``packageNames``，随后以普通用户身份执行以下脚本观察无 root 权限的应用可以检测到哪些以包名命名的文件夹。

```
#!/system/bin/sh
readonly EXIT_SUCCESS=0
readonly EXIT_FAILURE=1
exitCode=${EXIT_SUCCESS}
folders="/data/data /data/user/0 /data/user_de/0 /sdcard/Android/data"
packageNames="bin.mt.plus bin.mt.termex com.rifsxd.ksunext com.sukisu.ultra com.topjohnwu.magisk io.github.huskydg.magisk io.github.vvb2060.magisk me.bmax.apatch me.garfieldhan.apatch.next me.weishu.kernelsu"
for packageName in ${packageNames}
do
	for folder in ${folders}
	do
		if [[ -e "${folder}/${packageName}" ]];
		then
			exitCode=${EXIT_FAILURE}
			echo "Found \"${folder}/${packageName}\". "
		fi
	done
done
exit ${exitCode}
```

#### 牛头人

##### 从 ``v26.0`` 到 最初的 ``v30.0`` 版本报 Malicious hook

- 由于在这些版本中 Malicious hook 被重新定义因此它很可能是误报
- 请使用最新版检查环境

##### 其它问题

请参阅 [https://bbs.kanxue.com/thread-285106-1.htm](https://bbs.kanxue.com/thread-285106-1.htm)

#### 邮储银行

##### 2023 年 9 月左右使用了当时最新版官方面具和最新版 Shamiko 依旧闪退

- 由历史问题引起，更新即可解决问题
- 使用官方 Magisk 或 Magisk Alpha
  - 如果您在 2023 年 9 月左右使用官方 Magisk 或 Magisk Alpha，请切换到最新的 Magisk Delta
  - 如果您现在正在使用官方 Magisk 或 Magisk Alpha，请安装最新的 Magisk Alpha 和最新的 Shamiko 模块
- 使用 Magisk Delta
  - 如果您在 2023 年 9 月左右使用 Magisk Delta，请安装最新的 Magisk Delta（当时的 Magisk Delta 不会导致邮政储蓄银行闪退）
  - 如果您现在正在使用 Magisk Delta，请切换到最新的 Magisk Alpha 并安装最新的 Shamiko 模块

#### QQ

##### 无故下线用户、限制账号登录或临时冻结账号

- 手机 QQ（安卓版）
  - 定义降级：不向 QQ 暴露任何可疑环境（含 root 和注入环境）或执行任何注入 15 天后利用核心破解插件降级 QQ（后再观察 15 天）
  - 如果您使用的 QQ 版本低于 ``v8.6.0``
    - 除非被云控强制升级否则请勿升级 QQ
    - 如被云控强制升级请升级到高于当前版本的最低版本
  - 如果您使用的 QQ 版本处于 2021 年春夏季节风控事件影响区间 (``v8.6.0``, ``v8.8.17``) 内（此现象在使用 ``v8.8.0`` 版本时最为明显）
    - 如果您想继续使用 QXposed（QX）插件或 QQ 复读机插件且 QQ 能够降级
      - 请切换到 ``v8.6.0`` 或更低版本
    - 否则
      - 请卸载 QXposed（QX）插件或 QQ 复读机插件
      - 请禁用抢红包、自动群签到和消息群发功能
      - 请卸载所有不适配 LSPosed 的 Xposed API 调用保护的 QQ 插件
  - 如果您使用的 QQ 版本处于 (``v8.8.17``, ``v8.9.56``] 区间内
    - 除非被云控强制升级否则请勿升级 QQ
    - 如被云控强制升级请升级到高于当前版本的最低版本
    - 请卸载 QXposed（QX）插件或 QQ 复读机插件
    - 请禁用抢红包、自动群签到和消息群发功能
    - 请卸载所有不适配 LSPosed 的 Xposed API 调用保护的 QQ 插件
  - 如果您使用的 QQ 版本高于 ``v8.9.56`` 且受 2024 年秋季至 2025 年春季风控事件影响（使用 ``v9.1.35`` 版本时现象最为明显）
    - 请参阅 (``v8.8.17``, ``v8.9.56``]
    - 如果您想使用 XAutoDaily（XA）插件或 QAuxiliary（QA）插件，并且仍然可以降级您的 QQ，请
      - 确保您已按照本页的通用流程隐藏 root 和注入环境
      - 在 QAuxiliary（QA）插件中打开禁用 QQ 热补丁开关并关闭环境检测包（trpc.o3.*）拦截开关
      - 切换到 ``v9.1.31`` 或更低版本，
      - 切换到 ``v9.0.95`` 或更低版本，或者
      - 切换到 ``v8.9.56`` 或更低版本（如果接受非 NT 架构）
    - 否则
      - 请卸载所有 QQ 插件
      - 请禁用抢红包、自动群签到和消息群发功能
      - 高于 ``v9.1.31`` 版本时切勿向 QQ 暴露（切换环境时记得提前禁用 QQ）任何可疑环境（含 root 和注入环境）或执行任何注入
- 电脑 QQ（Windows）：始终使用最新怀旧版而非 QQNT 版本

#### 微信

##### 开启指纹支付提示失败（但其它境内外应用都能正常使用指纹）

- 临时解决方法：使用微信支付模块或微信支付插件（原理是通过指纹后将预先存储的密码进行提交）
- 本质解决方法：暂无
