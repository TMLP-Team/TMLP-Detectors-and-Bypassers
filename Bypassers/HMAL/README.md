#### HMA/HAML Configuring Tutorial

In LSPosed, only the System Framework should be selected as the scope. After activating the HMA/HMAL with only System Framework as the target (including when HMA/HMAL is updated or downgraded), please be reminded to reboot your device. 

In HMA/HMAL, at least one template should be created first. For example, a blacklist template should be designed, where you should select all the applications that others should not see. 

Subsequently, go to the application manage in HMAL and, for each application that will detect the "Twrp, Magisk, LSPosed, and Plugins" environment, do
1) Enable hiding; 
2) Select the blacklist or whitelist template you wish to use; and
3) Configure additional invisible or visible applications (corresponding to the blacklist or whitelist mode) if necessary. 

These two operations can be configured dynamically without rebooting, configuring in LSPosed Manager, or restarting the specified application. 
- If you want to make an application to be seen or not to be seen, just modify the template or the specified configuration for the specified application in HMA/HMAL. 
- If you want to make an application able or unable to see other applications, just go to the application manage page in HMA/HMAL. 

In this folder, you may see a JSON configuration file, which includes a blacklist and a whitelist template. In the future, we hope to include all package names of apps that may be detected and those that should not be detected in this configuration. Any pull requests are welcome. 

Nonetheless, faithfully speaking, a plugin that can hide the application list without manual configuration would be better. 
- Classifications:
  - Classification $A$: System applications that cannot be launched and system pre-installed applications that can be launched but are not critical; 
  - Classification $B$: TMLP-related applications; 
  - Classification $C$: Applications designed for environment detection; and
  - Classification $D$: Others.
- Examples:
  - $A$: ``com.onlus`` and ``com.android.settings``;
  - $B$: ``io.github.vvb2060.magisk`` and ``com.google.android.hmal``;
  - $C$: ``com.reveny.nativecheck`` and ``com.zhenxi.hunter``;
  - $D$: ``com.tencent.mm`` and `` com.tencent.mobileqq``. 
- Configurations: 
  - $\forall a \in A$: $a$ should ba able to see and be seen by $A$, $B$, $C$, and $D$; 
  - $\forall b \in B$: $b$ should be able to see $A$, $B$, $C$, and $D$ while should be unable to be seen by $C$ and $D$;
  - $\forall c \in C$: $c$ should be able to see and be seen by only $c$;
  - $\forall d \in D$: $d$ should be able to see and be seen by only $D$. 

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

在这个文件夹中，你或许会看到一个 JSON 配置文件，里面包含一个黑名单和白名单模板。在未来，我们希望将所有可能会发起检测的应用包名和应当不被检测到的应用包名都包含在此配置中。欢迎提出任何请求。

尽管如此，事实上，或许一个不需要手动配置就能够完成应用列表隐藏的插件会更好。
- 分类：
  - 分类 $A$：无法启动的系统应用和可以启动但并非关键的系统预装应用；
  - 分类 $B$：TMLP 相关应用；
  - 分类 $C$：用于环境检测的应用；
  - 分类 $D$：其它。
- 示例：
  - $A$: ``com.onlus`` 和 ``com.android.settings``;
  - $B$: ``io.github.vvb2060.magisk`` 和 ``com.google.android.hmal``;
  - $C$: ``com.reveny.nativecheck`` 和 ``com.zhenxi.hunter``;
  - $D$: ``com.tencent.mm`` 和 `` com.tencent.mobileqq``. 
- 配置：
  - $\forall a \in A$：$a$ 应当能够检测到 $A$、$B$、$C$ 和 $D$，并且能够被 $A$、$B$、$C$ 和 $D$ 检测到；
  - $\forall b \in B$：$b$ 应当能够检测到 $A$、$B$、$C$ 和 $D$，但不能被 $C$ 和 $D$ 检测到；
  - $\forall c \in C$：$c$ 应当能够检测到 $c$，并且只能被 $c$ 检测到；
  - $\forall d \in D$：$d$ 应当能够检测到 $D$，并且只能被 $D$ 检测到。
