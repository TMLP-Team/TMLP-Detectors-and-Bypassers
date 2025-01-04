#### HMA/HAML Configuring Tutorial

In LSPosed, only the System Framework should be selected as the scope. After activating the HMA/HMAL with only System Framework as the target (including when HMA/HMAL is updated or downgraded), please be reminded to reboot your device. 

In HMA/HMAL, at least one template should be created first. For example, a blacklist template should be designed, where you should select all the applications that others should not see. 

Subsequently, go to the application manage in HMAL and, for each application that will detect the "Twrp, Magisk, LSPosed, and Plugins" environment, do
1) Enable hiding; 
2) Select the blacklist or whitelist template you wish to use; and
3) Configure additional invisible or visible applications (corresponding to the blacklist or whitellist mode) if necessary. 

These two operations can be configured dynamically without rebooting, configuring in LSPosed Manager, or restarting the specified application. 
- If you want to make an application to be seen or not to be seen, just modify the template or the specified configuration for the specified application in HMA/HMAL. 
- If you want to make an application able or unable to see other applications, just go to the application manage page in HMA/HMAL. 

---

#### 配置 HMA/HMAL 教程

在LSPosed中，只应选择系统框架作为范围。在仅以系统框架为目标激活HMA/HMAL后（包括HMA/HMAL更新或降级时），请记住重新启动您的设备。

在HMA/HMAL中，应首先创建至少一个模板。例如，应设计一个黑名单模板，其中应选择所有其他人不应看到的应用程序。

随后，转到HMAL中的应用程序管理，对于将检测“Twrp，Magisk，LSPosed和Plugins”环境的每个应用程序，执行
1) 启用隐藏；
2) 选择要使用的黑名单或白名单模板；
3) 如有需要，配置额外不可见或可见的应用程序（分别对应黑名单或白名单模式）。

这两个操作可以动态配置，而无需重新启动，在LSPosed Manager中配置或重新启动指定的应用程序。
- 如果您想让应用程序可见或不可见，只需修改 HMA/HMAL 中指定应用程序的模板或指定配置即可。
- 如果您想让某个应用程序能够或无法看到其他应用程序，只需转到 HMA/HMAL 中的应用程序管理页面。
