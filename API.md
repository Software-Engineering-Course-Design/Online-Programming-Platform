# API

## 页面一——登录/注册页面

#### 注册

1.前端->后端

| Column   | Type    | Value                       | Description                                                  |
| -------- | ------- | --------------------------- | ------------------------------------------------------------ |
| username | string  |                             | 用户ID                                                       |
| userType | boolean | true(面试官)  false(面试者) | 用户类型                                                     |
| password | string  |                             | 密码                                                         |
| checkpwd | string  |                             | 确认密码                                                     |
| hr_code  | string  |                             | 面试官编码（该值只有在用户类型为面试官的时候要求输入），相当于面试官注册资格审查 |

2.后端->前端

| Column  | Type    | Value                                                | Description                                                  |
| ------- | ------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| ifExist | boolean | true(用户已存在)                   false(用户未存在) | 已存在：注册失败               未存在：注册成功              |
| msg     | string  | 后端自己设置                                         | 返回相应提示信息（比如ifExist为true则“注册失败，用户已存在”；为false则“注册成功”） |

#### 登录

1.前端->后端

| Column   | Type   | Value | Description |
| -------- | ------ | ----- | ----------- |
| username | string |       | 用户ID      |
| password | string |       | 密码        |

2.后端->前端

| Column   | Type    | Value                                                | Description                                                  |
| -------- | ------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| ifExist  | boolean | true(用户已存在)                   false(用户未存在) | 已存在：登录成功                                未存在：登录失败 |
| userType | boolean | true(面试官)  false(候选人)                          | 用户类型                                                     |
| msg      | string  | 后端自己设置                                         | 返回相应提示信息（比如ifExist为true则“登录成功”；为false则“登录失败，该用户尚未注册”） |

这里userType暂定这样，因为只有用户存在，登录成功才需要userType来判断跳转到相应页面，先暂时想出以下方案，后续看后端怎么写再做决定：

方案一：无论ifExist值是怎样，都返回userType到前端；此时userType类型设为string，值  0：面试官  1：候选人  2：用户不存在，不用跳转

方案二：只有ifExist的值为true，即用户存在，登录成功的时候，才返回userType到前端；此时userType类型设为boolean，值  true：面试官  false：候选人



## 页面二——面试官

#### 面试官首页

后端->前端

| Column          | Type  | Value | Description                                  |
| --------------- | ----- | ----- | -------------------------------------------- |
| question_num    | int   |       | 当前面试题数量                               |
| interviewer_num | int   |       | 当前面试者数量                               |
| h_id_arr        | Array |       | 面试题数组（返回所有面试题标题、questionID） |

**h_id_arr格式如下：[[1,heading_one],[2,heading_two]……]，两层数组，第一个参数是questionID，第二个参数是面试题标题**

#### 面试题详情

此页面即在面试官首页中点击列表中的题目时，跳转到具体题目内容的页面

每个面试题页面的URL，用questionID作为参数，由此实现每个面试题有各自的固定链接

后端->前端（打开页面即返回）

| Column     | Type   | Value | Description                                |
| ---------- | ------ | ----- | ------------------------------------------ |
| username   | string |       | 面试官用户ID                               |
| questionID | int    |       | 面试题ID                                   |
| heading    | string |       | 面试题标题                                 |
| question   |        |       | 面试题内容                                 |
| id_arr     | Array  |       | 面试者数组（返回提交了该题的面试者用户ID） |

***点击某个用户ID即触发请求，显示改面试者提交的代码以及批改结果***

1.前端->后端

| Column     | Type   | Value | Description |
| ---------- | ------ | ----- | ----------- |
| candidate  | string |       | 面试者ID    |
| questionID | int    |       | 面试题ID    |

2.后端->前端

| Column | Type   | Value                       | Description |
| ------ | ------ | --------------------------- | ----------- |
| code   | string |                             | 提交代码    |
| result | string | 0：未批改    1：AC    2：WA | 代码结果    |



#### 面试官新建面试题

1.前端->后端

| Column   | Type   | Value | Description  |
| -------- | ------ | ----- | ------------ |
| username | string |       | 面试官用户ID |
| heading  | string |       | 面试题标题   |
| question |        |       | 面试题内容   |

question是面试官输入的题目，支持富文本格式，类型暂定

**将题目存入数据库之后，将表中的自增ID作为questionID**

2.后端->前端

| Column    | Type    | Value                                                        | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：新建成功                                     false：新建失败 | 判断题目是否成功存入数据库中                                 |
| msg       | string  | 后端自己设置                                                 | 返回相应提示信息（比如ifSuccess为true则“新建成功”；为false则“新建失败，网络发生故障”） |

如果想复杂一点可以遍历数据库中的题目看是否有重复，有重复的就不能新建，这个以后再想

#### 

#### 面试官修改面试题目

1.前端->后端

| Column      | Type   | Value | Description  |
| ----------- | ------ | ----- | ------------ |
| username    | string |       | 面试官用户ID |
| questionID  | string |       | 面试题ID     |
| newHeading  | string |       | 新面试题标题 |
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

| Column    | Type    | Value                           | Description                                                  |
| --------- | ------- | ------------------------------- | ------------------------------------------------------------ |
| ifSuccess | boolean | true：邀请成功  false：邀请失败 | 判断邀请是否成功发送                                         |
| msg       | string  | 后端自己设置                    | 返回相应提示信息（比如ifSuccess为true则“邀请成功”；为false则“邀请失败，网络发生故障或邀请用户不存在”） |



#### 面试官批改提交代码

1.前端->后端

| Column   | Type   | Value                       | Description  |
| -------- | ------ | --------------------------- | ------------ |
| username | string |                             | 面试官用户ID |
| result   | string | 0：未批改    1：AC    2：WA | 代码结果     |

result是提交代码的批改，默认为0，只有当result为0时，批改按钮才是可用的，否则按钮disabled

2.后端->前端

| Column    | Type    | Value                                                        | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：批改成功                                           false：批改失败 | 判断提交代码是否成功批改                                     |
| msg       | string  | 后端自己设置                                                 | 返回相应提示信息（比如ifSuccess为true则“批改成功”；为false则“该代码已被批改过，不可重复批改”） |

后端先判断提交代码的result是否为0，即未批改状态，只有这种情况才可以成功批改

## 页面三——面试者模块

#### 在线编程题目显示页面

一打开页面即触发

后端->前端

| Column       | Type  | Value | Description    |
| ------------ | ----- | ----- | -------------- |
| id_arr       | Array |       | 面试题ID数组   |
| heading_arr  | Array |       | 面试题标题数组 |
| question_arr | Array |       | 面试题题目数组 |



#### 在线编程提交代码页面

可多次保存，但只能提交一次

##### 保存//暂时不知道要不要

1.前端->后端

| Column     | Type   | Value | Description  |
| ---------- | ------ | ----- | ------------ |
| username   | string |       | 面试者用户ID |
| questionID | string |       | 面试题目ID   |
| code       |        |       | 保存代码     |

可以多次保存

2.后端->前端

| Column    | Type    | Value                                                        | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：保存成功                                           false：保存失败 | 判断提交代码是否成功保存                                     |
| msg       | string  | 后端自己设置                                                 | 返回相应提示信息（比如ifSuccess为true则“保存成功”；为false则“保存失败，网络发生故障”） |

##### 提交

1.前端->后端

| Column     | Type   | Value | Description  |
| ---------- | ------ | ----- | ------------ |
| username   | string |       | 面试者用户ID |
| questionID | string |       | 面试题目ID   |
| code       |        |       | 提交代码     |

只能提交一次

2.后端->前端

| Column    | Type    | Value                                                        | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：提交成功                                           false：提交失败 | 判断提交代码是否成功批改                                     |
| msg       | string  | 后端自己设置                                                 | 返回相应提示信息（比如ifSuccess为true则“提交成功”；为false则“提交失败，网络发生故障”） |

#### 查看已提交的题目列表

##### 方案一：

直接按题目显示，页面呈现一个列表，列表中是已提交过代码的题目标题，点击标题可查看面试题内容、提交代码内容以及批改结果

1.前端->后端

| Column   | Type   | Value | Description  |
| -------- | ------ | ----- | ------------ |
| username | string |       | 面试者用户ID |

2.后端->前端

| Column   | Type  | Value | Description                    |
| -------- | ----- | ----- | ------------------------------ |
| h_id_arr | Array |       | 已提交代码的面试题标题和ID数组 |

**h_id_arr格式如下：[[1,heading_one],[2,heading_two]……]，两层数组，第一个参数是questionID，第二个参数是面试题标题**

###### 点击标题后跳转

1.前端->后端

| Column     | Type   | Value | Description  |
| ---------- | ------ | ----- | ------------ |
| username   | string |       | 面试者用户ID |
| questionID | string |       | 面试题目ID   |

2.后端->前端

| Column   | Type   | Value                       | Description |
| -------- | ------ | --------------------------- | ----------- |
| heading  | string |                             | 面试题标题  |
| question | string |                             | 面试题题目  |
| code     | string |                             | 提交的代码  |
| result   | string | 0：未批改    1：AC    2：WA | 代码结果    |

