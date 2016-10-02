说一下我想写这个干嘛：
就是能够连接在NAT转发环境下无DNS解析的主机。
由于NAT转发下的主机没有办法通过外网ip直连，所以代理模式必须使用主动模式。
我简单说一下大概思路：
```sequence
Client-->Proxy: 建立连接并发送句柄
Note left of Server:如果没有客户端的句柄\n那么就继续获取
Server-->Proxy:	获取句柄
Proxy-->Server:	返回句柄
Note right of Client:此时客户端等待服务器\n直到其返回代码
Server-->Proxy:	返回结果
Proxy-->Client:	返回结果
```
接下来分别分析一下客户端和目标端的流程：
#客户端：
```flow
st=>start: 开始
e=>end: 结束
input=>operation: 用户输入
send=>operation: 发送指令
wait=>operation: 等待
output=>operation: 输出结果
resp=>condition: 判断有无响应&&无超时
cont=>condition: 是否有输出？
quit=>condition: 判断退出

st->input->send->wait->resp
resp(yes)->cont
resp(no)->wait
cont(yes)->output->quit
cont(no)->send
quit(yes)->e
quit(no)->input
```
#目标端：
```flow
start=>start: start
end=>end: end
init=>operation: 初始化
get=>operation: 获取语句
Qget=>condition: 判断是否获取语句
do=>operation: 执行语句并取得返回值
return=>operation: 返回语句返回值
quit=>condition: 判断退出?


start->init->get->Qget->end
Qget(yes)->do->return->quit
Qget(no)->get
quit(yes)->end
quit(no)->get
```

就先写这么多，其他的日后再补
目前这个设计没有加入代理端，日后再来更