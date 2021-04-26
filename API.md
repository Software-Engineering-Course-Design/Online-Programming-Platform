# API

## 页面一

#### 注册

1.前端->后端

| Column   | Type    | Value                       | Description |
| -------- | ------- | --------------------------- | ----------- |
| username | string  |                             | 用户ID      |
| userType | boolean | true(面试官)  false(候选人) | 用户类型    |
| password | string  |                             | 密码        |
| checkpwd | string  |                             | 确认密码    |

2.后端->前端

| Column  | Type    | Value                                                | Description                                                  |
| ------- | ------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| ifExist | boolean | true(用户已存在)                   false(用户未存在) | 已存在：注册失败               未存在：注册成功              |
| msg     | string  | 后端自己设置                                         | 返回相应提示信息（比如ifExist为true则“注册成功”；为false则“注册失败，用户已存在”） |

#### 登录

1.前端->后端

| Column   | Type   | Value | Description |
| -------- | ------ | ----- | ----------- |
| username | string |       | 用户ID      |
| password | string |       | 密码        |

2.后端->前端

| Column   | Type    | Value                                                | Description                                                  |
| -------- | ------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| ifExist  | boolean | true(用户已存在)                   false(用户未存在) | 已存在：登录成功                               未存在：登录失败 |
| userType | boolean | true(面试官)  false(候选人)                          | 用户类型                                                     |

这里userType暂定这样，因为只有用户存在，登录成功才需要userType来判断跳转到相应页面，先暂时想出以下方案，后续看后端怎么写再做决定：

方案一：无论ifExist值是怎样，都返回userType到前端；此时userType类型设为string，值  0：面试官  1：候选人  2：用户不存在，不用跳转

方案二：只有ifExist的值为true，即用户存在，登录成功的时候，才返回userType到前端；此时userType类型设为boolean，值  true：面试官  false：候选人



## 页面二——面试官

#### 面试官新建面试题

1.前端->后端

| Column   | Type   | Value | Description  |
| -------- | ------ | ----- | ------------ |
| username | string |       | 面试官用户ID |
| question |        |       | 题目         |

question是面试官输入的题目，支持富文本格式，类型暂定

2.后端->前端

| Column    | Type    | Value                                                        | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：新建成功                                     false：新建失败 | 判断题目是否成功存入数据库中                                 |
| msg       | string  | 后端自己设置                                                 | 返回相应提示信息（比如ifSuccess为true则“新建成功”；为false则“新建失败，网络发生故障”） |

如果想复杂一点可以遍历数据库中的题目看是否有重复，有重复的就不能新建

#### 面试官修改面试题目

1.前端->后端

| Column      | Type   | Value | Description  |
| ----------- | ------ | ----- | ------------ |
| username    | string |       | 面试官用户ID |
| questionID  | string |       | 面试题ID     |
| newQuestion | string |       | 新面试题     |

每个面试官只能修改自己建立的题目

2.后端->前端

| Column    | Type    | Value                                                        | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：修改成功                                     false：修改失败 | 判断题目是否修改成功并存入数据库中                           |
| msg       | string  | 后端自己设置                                                 | 返回相应提示信息（比如ifSuccess为true则“修改成功”；为false则“修改失败……”） |

#### 邀请一个候选人编程

1.前端->后端

| Column    | Type   | Value | Description  |
| --------- | ------ | ----- | ------------ |
| username  | string |       | 面试官用户ID |
| candidate | string |       | 候选人用户ID |

2.后端->前端

| Column    | Type    | Value                          | Description                                                  |
| --------- | ------- | ------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：邀请成功 false：邀请失败 | 判断邀请是否成功发送                                         |
| msg       | string  | 后端自己设置                   | 返回相应提示信息（比如ifSuccess为true则“邀请成功”；为false则“邀请失败，网络发生故障或邀请用户不存在”） |

这里预设在点击选取候选人按钮时，立即向发送请求，返回数据库中所有

#### 面试官批改提交代码

1.前端->后端

| Column   | Type   | Value                       | Description  |
| -------- | ------ | --------------------------- | ------------ |
| username | string |                             | 面试官用户ID |
| result   | string | 0：未批改    1：AC    2：WA | 代码结果     |

result是提交代码的属性，默认为0

2.后端->前端

| Column    | Type    | Value                                                        | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：批改成功                                           false：批改失败 | 判断提交代码是否成功批改                                     |
| msg       | string  | 后端自己设置                                                 | 返回相应提示信息（比如ifSuccess为true则“批改成功”；为false则“该代码已被批改过，不可重复批改”） |

后端先判断提交代码的result是否为0，即未批改状态，只有这种情况才可以成功批改

## 页面三——候选人模块

#### 在线编程提交代码

1.前端->后端

| Column     | Type   | Value            | Description  |
| ---------- | ------ | ---------------- | ------------ |
| username   | string |                  | 候选人用户ID |
| questionID | string |                  | 面试题目ID   |
| code       |        |                  | 提交代码     |
| status     | string | 0：保存  1：提交 | 状态         |

只能提交一次，暂时这么设置

2.后端->前端

| Column    | Type    | Value                                                        | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：提交成功                                           false：提交失败 | 判断提交代码是否成功批改                                     |
| msg       | string  | 后端自己设置                                                 | 返回相应提示信息（比如ifSuccess为true则“提交成功”；为false则“提交失败，网络发生故障”） |

#### 查看已提交的题目列表

1.前端->后端

| Column   | Type   | Value | Description  |
| -------- | ------ | ----- | ------------ |
| username | string |       | 候选人用户ID |
|          |        |       |              |
|          |        |       |              |

