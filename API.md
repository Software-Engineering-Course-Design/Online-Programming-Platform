# API

## 一——登录/注册页面

#### 注册

1.前端->后端

| Column   | Type    | Value                       | Description                                                  |
| -------- | ------- | --------------------------- | ------------------------------------------------------------ |
| username | string  |                             | 用户ID                                                       |
| userType | boolean | true(面试官)  false(面试者) | 用户类型                                                     |
| password | string  |                             | 密码                                                         |
| checkpwd | string  |                             | 确认密码                                                     |
| hr_code  | string  |                             | 面试官编码（该值只有在用户类型为面试官的时候要求输入，但，无论userType是什么，都会传hr_code到后端），相当于面试官注册资格审查 |

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

//方案一：无论ifExist值是怎样，都返回userType到前端；此时userType类型设为string，值  0：面试官  1：候选人  2：用户不存在，不用跳转

方案二：只有ifExist的值为true，即用户存在，登录成功的时候，才返回userType到前端；此时userType类型设为boolean，值  true：面试官  false：候选人

用方案二



## 二——面试官

#### 面试官首页

后端->前端

| Column        | Type  | Value | Description                                  |
| ------------- | ----- | ----- | -------------------------------------------- |
| question_num  | int   |       | 当前面试题数量                               |
| applicant_num | int   |       | 当前面试者数量                               |
| h_id_arr      | Array |       | 面试题数组（返回所有面试题标题、questionID） |

**h_id_arr格式如下：[[1,heading_one],[2,heading_two]……]，两层数组，第一个参数是questionID，第二个参数是面试题标题**

#### 面试题详情

此页面即在面试官首页中点击列表中的题目时，跳转到具体题目内容的页面

每个面试题页面的URL，用**questionID**作为参数，由此实现每个面试题有各自的固定链接，其中**questionID**是**数据库的问题表中的自增id**

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
| applicant  | string |       | 面试者ID    |
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
| answer   |        |       | 正确答案     |

question是面试官输入的题目，支持富文本格式，类型暂定

**将题目存入数据库之后，将表中的自增ID作为questionID**

2.后端->前端

| Column    | Type    | Value                                                        | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：新建成功                                     false：新建失败 | 判断题目是否成功存入数据库中                                 |
| msg       | string  | 后端自己设置                                                 | 返回相应提示信息（比如ifSuccess为true则“新建成功”；为false则“新建失败，网络发生故障”） |



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

#### 发起一场面试

1.前端->后端

| Column         | Type    | Value                           | Description      |
| -------------- | ------- | ------------------------------- | ---------------- |
| username       | string  |                                 | 面试官用户ID     |
| applicant      | Array   |                                 | 面试者用户ID数组 |
| questionNumber | int     |                                 | 面试题数目       |
| questionID     | Array   |                                 | 面试题ID数组     |
| createWay      | boolean | true：自主命题；false：系统抽题 | 命题方式         |
| startTime      | string  | '2021-05-28 22:50:00'类似这种   | 面试开始时间     |
| endTime        |         |                                 | 面试结束时间     |

**将一场面试存入数据库之后，将表中的自增ID作为sessionID，用来做场次的ID**

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
| status   | string | 0：未批改    1：AC    2：WA | 代码结果     |

status是提交代码的批改，默认为0，只有当result为0时，批改按钮才是可用的，否则按钮disabled

2.后端->前端

| Column    | Type    | Value                                                        | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：批改成功                                           false：批改失败 | 判断提交代码是否成功批改                                     |
| msg       | string  | 后端自己设置                                                 | 返回相应提示信息（比如ifSuccess为true则“批改成功”；为false则“该代码已被批改过，不可重复批改”） |

后端先判断提交代码的status是否为0，即未批改状态，只有这种情况才可以成功批改

## 三——面试者模块

#### 面试者首页

前端->后端

| Column   | Type   | Value | Description  |
| -------- | ------ | ----- | ------------ |
| username | string |       | 面试者用户ID |

后端->前端

| Column          | Type  | Value | Description            |
| --------------- | ----- | ----- | ---------------------- |
| notjoin | Array |       | 未参加的面试场次信息 |
| join | Array | | 已参加的面试场次信息 |

格式如下：

notjoin:  [{"**sessionID**":" ","**hr_username**":" ", "**questionNumber**":" ","**startTime**":" ","**endTime**":" ","**timeUsed**": " "}, {......}],

join:  [{"**sessionID**":" ","**hr_username**":" ", "**questionNumber**":" ","**status**": " ", "**score**":" ","**startTime**":" ","**endTime**":" "}, {......}]

**notjoin**代表未参加的面试信息，里面每一场的信息成为一个json串，

sessionID是场次；

hr_username是发起该场面试的面试官姓名；

questionNumber是该场次的面试题数量；

startTime是面试开始时间；

endTime是面试结束时间；

timeUsed是该场次面试所需的时间，用endTime-startTime（这个timeUsed需要后端自己计算然后发给前端，单位是分钟，数据类型是string,这个类型int还是string随便，反正前端只是显示一下，暂定string，看怎样方便怎样用）。

**join**代表已参加的面试信息，里面每一场的信息成为一个json串，

sessionID是场次；

hr_username是发起该场面试的面试官姓名；

questionNumber是该场次的面试题数量；

status是批改状态，数据类型是bool，false：未批改 true：已批改；

score是面试成绩（这个score需要后端自己计算再发给前端，满分一百分，每道题的分数是 100/questionNumber，计算该面试者在这个场次AC了多少道题，这个后端还要判断一下该场面试是否已批改，未批改则返回0）

startTime是面试开始时间；

endTime是面试结束时间；

**举例**

notjoin: [{

​      "sessionID": 3,

​      "hr_username": "aaa",

​      "questionNumber": 3,

​      "startTime":'2021-05-28 17:50:00',

​      "endTime":'2021-05-28 18:50:00',

​      "timeUsed": 60

​    },

]



#### 在线编程题目显示模块

1.前端->后端

| Column    | Type   | Value | Description |
| --------- | ------ | ----- | ----------- |
| sessionID | int    |       | 面试场次ID  |
| username  | string |       | 用户名      |

2.后端->前端

| Column       | Type  | Value | Description    |
| ------------ | ----- | ----- | -------------- |
| question_list       | Array |       | 面试题信息数组   |

将该场次的面试题返回给前端，并把该用户该场次的面试设为已参加状态
格式：
    "question_list": [
        {
            "body": "write a Stack",
            "heading": "Stack",
            "questionID": 3
        },
        {
            "body": "reverse the Linklist",
            "heading": "Linklsit",
            "questionID": 4
        }
    ]

#### 在线编程代码模块

##### 提交

提交某一道题，每道题只能提交一次

1.前端->后端

| Column         | Type    | Value                       | Description      |
| -------------- | ------- | --------------------------- | ---------------- |
| username       | string  |                             | 面试者用户ID     |
| sessionID      | int     |                             | 面试场次ID       |
| questionID     | int     |                             | 面试题目ID       |
| code           |         |                             | 提交代码         |

questionStatus默认未提交，即false

2.后端->前端

| Column    | Type    | Value                                                        | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：提交成功                                           false：提交失败 | 判断提交代码是否成功提交                                     |
| msg       | string  | 后端自己设置                                                 | 返回相应提示信息（比如ifSuccess为true则“提交成功”；为false则“提交失败，网络发生故障”） |

#### 结束面试（场次）

答题结束之后总交卷

1.前端->后端

| Column      | Type     | Value | Description    |
| ----------- | -------- | ----- | -------------- |
| username    | string   |       | 面试者用户ID   |
| sessionID   | int      |       | 面试场次ID     |
| submit_time | Datetime |       | 交卷的日期时间 |

2.后端->前端

| Column    | Type    | Value                                                        | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ifSuccess | boolean | true：提交成功                                           false：提交失败 | 判断是否成功交卷                                             |
| msg       | string  | 后端自己设置                                                 | 返回相应提示信息（比如ifSuccess为true则“交卷成功，已结束面试”；为false则“提交失败，网络发生故障”） |

#### 查看已参加的面试的结果

按面试场次显示，按场次顺序显示题目标题，点击标题可查看面试题内容、提交代码内容、标准答案以及批改结果

1.前端->后端

| Column    | Type   | Value | Description  |
| --------- | ------ | ----- | ------------ |
| username  | string |       | 面试者用户ID |
| sessionID | int    |       | 面试场次ID   |

2.后端->前端

| Column       | Type   | Value                       | Description        |
| ------------ | ------ | --------------------------- | ------------------ |
|   interview_result_list  | Array |                     |     用户某场次面试的结果         |
将某用户某场次的面试信息返回，格式如下：
    "interview_result_list": [
        {

            "answer": "answer1",

            "body": "body1",

            "code": "#include<iostream>",

            "heading": "Stack",

            "questionID": 1,

            "result": "0"

        },
        {
            "answer": "answer2",

            "body": "body2",

            "code": null,

            "heading": "Queue",

            "questionID": 2,

            "result": "AC"

        }
    ]

其中questionID是面试题ID，heading是面试题题目，body是该面试题内容，answer是标准答案，code是面试者提交的代码，result是代码结果（0：未批改    1：AC    2：WA）




## **四——评论区模块** 

#### **进入后加载页面** 

1.前端->后端 

| Column     | Type    | Value | Description |
| ---------- | ------- | ----- | ----------- |
| username   | string  |       | 用户ID      |
| userType   | boolean |       | 用户类型    |
| questionID | string  |       | 面试题ID    |

2.后端->前端 

| Column      | Type    | Value                          | Description                                                  |
| ----------- | ------- | ------------------------------ | ------------------------------------------------------------ |
| commentList | Array   |                                | 当前题目下的评论内容，存储在数组中。元素为每条评论的相关信息，包括发送用户id、楼层数、评论内容、楼中楼回复。且每条直接评论的评论最多只能有一层楼中楼 |
| questionID  | string  |                                | 面试题ID                                                     |
| ifSuccess   | Boolean | true：加载成功 false：加载失败 | 判断评论是否加载成功                                         |
| msg         | string  |                                | 返回相应提示信息（比如ifSuccess为false则返回“加载失败”）     |

commentList建议格式： 

[ 

{    id: 'testUsr0',//用户id 

layIDX: 1,//主楼层数 

content: 'testComment0',//评论内容 

isSub: true/false,//是否为楼中楼回复 

sublayer: { 

id: 'testUsr1',//用户id 

layIDX: 1,//楼中楼层数 

content: 'testComment1',//评论内容 

}//楼中楼回复列表，如果isSub为true，设置sublayer为空； 

//如果isSub为false，允许给sublayer赋值 

}, 

... 

] 

#### **发送评论** 

1.前端->后端 

| Column         | Type    | Value                        | Description                                            |
| -------------- | ------- | ---------------------------- | ------------------------------------------------------ |
| senderID       | string  |                              | 当前用户（即发送评论者）的id                           |
| commentContent | string  |                              | 评论内容                                               |
| isSublayer     | Boolean | true：楼中楼 false：直接评论 | 是否回复他人评论，楼中楼则为true，直接评论题目为false  |
| layerID        | int     | 0：直接评论 >=1：楼中楼      | 回复楼层的层数，楼中楼则为大于等于1的整数，直接评论为0 |

2.后端->前端 

| Column    | Type    | Value                          | Description                                                  |
| --------- | ------- | ------------------------------ | ------------------------------------------------------------ |
| ifSuccess | Boolean | true：加载成功 false：加载失败 | 判断评论是否加载成功                                         |
| msg       | string  |                                | 返回相应提示信息（比如ifSuccess为true则“评论成功”；为false则“评论失败”） |

- 此处前端是否应该向后端发送questionID