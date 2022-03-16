# Htek D&R test tool
## 简介
- 用于进行htek话机的研发测试工作
- 简化重复性操作，优化工作效率
## 功能
### 功能区
- AutoTest：enable_auto_test_api
- 调试模式：enable_ftp & enable_telnet
- 重启话机
- 恢复出厂设置
- log server：打开界面实时接收话机log
- 待开发
### 升级
- 支持一键升级，自动skip rom check
- 在绑定时更新fw path 和 cfg path
### P值配置
- 支持根据P值查询对应的value
- 支持一键设置P值
### 注册信息
- 支持一键注册账号
- 支持在register_date.yml文件中配置可注册账号信息
### 保存区
- 支持保存截图
- 支持保存syslog
- 支持保存配置

## 定义
### MainWindow 主窗口类
- self.D1
- self.D2
- self.D3
- self.D4
#### MainWindow.D1 页面类
- self.device 当前页面绑定设备
- self.btn_  当前页面btn控件
- self.text_ 当前页面text控件
- self.box_ 当前页面box控件
- self.lab_ 点前页面lab控件
##### MainWindow.D1.device 设备类
- self.ip
- self.user
- self.password
- self.mac
- self.model
- self.version
# Release Note
## 0.0.1
- 基本界面搭建及绑定功能实现
- 支持P值查询
- 支持指派升级
- 支持auto test、telnet、reboot、factory
## 0.0.2
- 支持log server
- 支持截图保存
## 0.1.0
- 重构整体代码
- 优化性能
## 0.1.1
- 优化导入
- 整理目录结构
## 0.1.2
- 支持syslog保存
- 支持xml cfg保存
## 0.1.3
- 优化整理信号机制
- 防范保存截图时主线程卡死
- 更新title为HlTT
- 合并重构分支到主分支