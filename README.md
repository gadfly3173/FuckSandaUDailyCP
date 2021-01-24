# FuckDailyCP
#### 简介
杉达学院今日校园自动健康打卡脚本。
可以挂服务器上定时自动打卡。
健康的人可以用一下（雾）。
#### 使用说明
使用Fiddler等工具对今日校园进行抓包，手动打卡后找到`http://202.121.174.56:8089/report/report/todayReport`这条记录，从中取出post请求时发送的`ts`和`decodes`两条header，填入代码里，然后再从请求体中找到下面这样的一串json，把它按照python的dict的格式也写到代码里对应的位置就行，然后执行`python3 FUCKDailyReport.py`
```jsonc
{
  "username": "f17xxxxx"
  // etc
}
```
#### 挂服务器提示
请注意系统时间是否设置正确

Linux下可以使用`crontab -e`设置定时任务让程序每天自动打卡
```bash
0 10 * * * python3 FUCKDailyReport.py
```
#### 最后
python脚本撰写与研究都是在某童鞋（等他告诉我他的GitHub仓库就写上来）的帮助下完成的，非常感谢

decodes header的算法还没有找到，只知道是基于时间戳和code（一般是你的学号）生成的。虽然这个算法是写在前端的，但是看起来学校进行webpack打包时没有生成sourcemap，查找原本的算法非常困难，因此把打包后的那个js也丢上来，有兴趣的小伙伴可以试试找找，最好找到以后给我来提个ISSUE，233333。

index.js是我用jsnice.org处理之后的，index.ab0f794f.js则是原本的js。
