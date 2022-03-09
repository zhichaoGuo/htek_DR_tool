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
#### MainWindow.D1 页面
##### MainWindow.D1.ip 设备信息