### Frameworks

This folder aims to archive the historical injection frameworks and the latest versions of different branches of the modern injection framework, the LSPosed framework. 

#### Xposed

This is the fundamental injection framework. Most of the upcoming injection frameworks are based on this. 

#### EdXposed

During the EdXposed era, a variety of injection frameworks emerged, which can be categorized into non-virtual frameworks and virtual frameworks based on their working principles. 
Non-virtual frameworks often require root privileges, while virtual frameworks typically do not; hence, virtual frameworks are also known as rootless frameworks. 

Non-virtual frameworks usually perform injection only at runtime, without modifying the target application's stock ``.apk`` file. 
Virtual frameworks typically achieve injection by patching the target application with plugins or by having the plugin and target application run in the framework's virtual environment. 
This inherently makes non-virtual frameworks far more stealthy than virtual frameworks, and this has proven to be true. 
At that time, we recommended using the latest version of EdXposed's YAHFA (YAHFA is older than SandHook by 2 years and outperforms SandHook, as SandHook can make the system heavier than YAHFA). 

- Non-virtual injection frameworks
  - EdXposed: [EdXposed](https://github.com/ElderDrivers/EdXposed) and [EdXposed Manager](https://github.com/ElderDrivers/EdXposedManager)
  - Tai Chi (root)
- Virtual injection frameworks
  - Tai Chi (non-root)
  - 应用转生

#### LSPosed

Compared to historical injection frameworks, LSPosed and LSPatch, as well as their branches, offer superior performance, functionality, stability, and concealment with LSPlant as the core, 
especially the stand-alone scope for each plugin, making it available to activate or deactivate the plugins whose targets do not involve the system framework without rebooting. 
Nowadays, nearly all users rely on LSPosed or one of its branches as their injection framework, a small number use LSPatch, and only a very few continue to use legacy injection frameworks. 
LSPosed and its branches require root privileges and are non-virtual frameworks, while LSPatch and its branches are virtual frameworks based on LSPlant that patch target applications using plugins. 
Based on the analysis in the part of EdXposed and years of experience, we recommend using LSPosed and its branches over LSPatch and its branches. 

Among all the public branches of the LSPosed framework, it is recommended to use the latest release version built in the ``Actions`` page of the ``Jing Matrix`` branch. 
Compared to the original official LSPosed and other LSPosed branches, the ``Jing Matrix``, ``it``, ``Irena``, and ``ReLSPosed`` branches have better performance, functionality, stability, and concealment. 
Compared to the original official LSPosed, the ``npm`` branch disables the logging, and the ``mod`` branch provides the command-line interface (CLI). 
It is said that the members of the LSPosed ``it`` branch, a private branch, are mainly the members from the original official LSPosed. 
If necessary, please apply for joining according to [https://t.me/RootDetected/138/510](https://t.me/RootDetected/138/510) and keep internal information confidential. 
The version here is the latest leaked one fetched from [https://t.me/LSP_Leaks](https://t.me/LSP_Leaks). 
Overall, please disable logging features that may trigger detection, enable Xposed API call protection, and configure the scope for each plugin based on the principle of least privilege. 

Within LSPatch and its branches, we recommend using NPatch. 

- LSPosed and its branches
  - The original official LSPosed: [https://github.com/LSPosed/LSPosed](https://github.com/LSPosed/LSPosed) and [https://t.me/LSPosed](https://t.me/LSPosed)
  - The ``Jing Matrix`` branch: [https://github.com/JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed)
  - The ``it`` branch: This branch is private
  - The ``Irena`` branch: [https://github.com/re-zero001/LSPosed-Irena](https://github.com/re-zero001/LSPosed-Irena)
  - The ``ReLSPosed`` branch: [https://github.com/ThePedroo/ReLSPosed/actions/runs/18026600180](https://github.com/ThePedroo/ReLSPosed/actions/runs/18026600180)
  - The ``mod`` branch: [https://github.com/mywalkb/LSPosed_mod](https://github.com/mywalkb/LSPosed_mod)
  - The ``npm`` branch: No public official GitHub repositories are found. A possible publisher Telegram channel should be [https://t.me/rormzhstjxm](https://t.me/rormzhstjxm). 
- LSPatch and its branches
  - The original official LSPatch: [https://github.com/LSPosed/LSPatch](https://github.com/LSPosed/LSPatch) and [https://t.me/LSPosed](https://t.me/LSPosed)
  - OPatch: [https://github.com/8MiYile/LSPatch-OP](https://github.com/8MiYile/LSPatch-OP)
  - NPatch: [https://github.com/7723mod/NPatch](https://github.com/7723mod/NPatch)

---

### 框架

本文件夹旨在存储历史注入框架和现代注入框架 LSPosed 的各个分支的最新版本。

#### Xposed

这是最基本的注入框架，后来的大多数注入框架都基于该框架实现。

#### EdXposed

在 EdXposed 时代出现了多种注入框架，根据工作原理可被划分为非虚拟框架和虚拟框架两类，
其中非虚拟框架往往需要 root 权限，而虚拟框架往往不需要 root 权限，因此虚拟框架也被称为免 root 框架。

非虚拟框架往往仅在运行时进行注入，不会对目标应用的原始 ``.apk`` 文件做出任何修改，
而虚拟框架通常通过用插件修补目标应用或让插件和目标应用在框架的虚拟环境下运行来实现注入，
这从本质上决定了非虚拟框架的隐蔽性会远优于虚拟框架，而事实也是如此。
在那时，我们推荐使用最新版 EdXposed 的 YAHFA（YAHFA 比 SandHook 早两年且后来 SandHook 的负担会相对较大）。

- 非虚拟框架
  - EdXposed：[EdXposed](https://github.com/ElderDrivers/EdXposed) 和 [EdXposed 管理器](https://github.com/ElderDrivers/EdXposedManager)
  - 太极（阳）
- 虚拟框架
  - 太极（阴）
  - 应用转生

#### LSPosed

与历史注入框架相比，LSPosed 和 LSPatch 及其分支以 LSPlant 为核心在性能上、功能上、稳定性和隐蔽性上均有着更出色的表现，
尤其是其对每个插件独立的作用域实现，使得无需重启就能激活或不激活作用域不含有系统框架的插件成为了可能。
现如今，几乎所有用户都在使用 LSPosed 或其分支之一作为注入框架，少部分用户在使用 LSPatch，极少部分用户依旧在使用历史注入框架。
LSPosed 及其分支需要 root 权限，是非虚拟框架，而 LSPatch 及其分支则是基于 LSPlant 通过使用插件修补目标应用实现的虚拟框架。
参阅 EdXposed 部分与多年来的实践，相比于 LSPatch 及其分支，我们更建议使用 LSPosed 及其分支。

在 LSPosed 的所有公开分支中，推荐使用 Jing Matrix 分支的 ``Actions`` 页中构建的最新发行版本。
与原始官方 LSPosed 及其它 LSPosed 分支相比，``Jing Matrix``、``it``、``Irena`` 和 ``ReLSPosed`` 分支具有更强的性能、功能、稳定性和隐蔽性。
与原始官方 LSPosed 相比，``npm`` 分支禁用了日志功能，``mod`` 版本提供命令行接口。
据悉，LSPosed ``it`` 分支并不公开，其团队成员大多数为原始官方 LSPosed 的团队成员，如有需要，可根据 [https://t.me/RootDetected/138/510](https://t.me/RootDetected/138/510) 申请加入并对内部信息保密；
此处放置的为所有已泄露的版本中的最新版本，一个可能的获取渠道为 [https://t.me/LSP_Leaks](https://t.me/LSP_Leaks)。
总之，请关闭可能会导致被检测的日志功能，启用 Xposed API 调用保护，并基于最小权限原则为每个插件配置作用域。

在 LSPatch 及其分支中，我们建议使用 NPatch。

- LSPosed 及其分支
  - 原始官方 LSPosed：[https://github.com/LSPosed/LSPosed](https://github.com/LSPosed/LSPosed) 和 [https://t.me/LSPosed](https://t.me/LSPosed)
  - ``Jing Matrix`` 分支：[https://github.com/JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed)
  - ``it`` 分支：该分支暂不公开
  - ``Irena`` 分支：[https://github.com/re-zero001/LSPosed-Irena](https://github.com/re-zero001/LSPosed-Irena)
  - ``ReLSPosed`` 分支：[https://github.com/ThePedroo/ReLSPosed/actions/runs/18026600180](https://github.com/ThePedroo/ReLSPosed/actions/runs/18026600180)
  - ``mod`` 分支：[https://github.com/mywalkb/LSPosed_mod](https://github.com/mywalkb/LSPosed_mod)
  - ``npm`` 分支：暂未找到公开的 npm 分支官方 GitHub 链接。一个可能的电报发布频道为 [https://t.me/rormzhstjxm](https://t.me/rormzhstjxm)
- LSPatch 及其分支
  - 原始官方 LSPatch：[https://github.com/LSPosed/LSPatch](https://github.com/LSPosed/LSPatch) 和 [https://t.me/LSPosed](https://t.me/LSPosed)
  - OPatch：[https://github.com/8MiYile/LSPatch-OP](https://github.com/8MiYile/LSPatch-OP)
  - NPatch：[https://github.com/7723mod/NPatch](https://github.com/7723mod/NPatch)
