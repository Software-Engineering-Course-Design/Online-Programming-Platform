import axios from "axios";

const ERR_OK = 0;


function getFromServer(url, params) {
  return new Promise((resolve, reject) => {
    //统计指定对象的属性组成的数组的长度
    if (Object.getOwnPropertyNames(params).length > 0) {
      url += '?';
      for (const f in params) {
        url += f + '=' + params[f] + '&';
      }
      //构建get请求的字符串
      // url?a=1&b=3
      url = url.substring(0, url.length - 1);
    }
    axios.get(url).then((response) => {
      if (response.status === 200) {
        resolve(response.data)
      } else {
        reject(response.data.msg)
      }
    }).catch((error) => {
      reject(error)
    })
  })
}

//post请求封装
export function post(url, postData) {
  return new Promise((resolve, reject) => {
    axios.post(url, postData).then(response => {
      if (response.status === 200) {
        resolve(response.data);
      } else {
        reject(response.data.msg);
      }
    }).catch(err => {
      reject(err);
    })
  })
}

//get请求封装
export function get(url) {
  return function (params) {
    return axios.get(url).then(res => {
      console.log(res.data);
      const {
        errno,
        data
      } = res.data;
      if (errno == ERR_OK) { //请求成功
        console.log(data);
        return data;
      }
    }).catch(e => {

    })
  }

}
// export function get(url, form = {}, cache = false) {
//   if (cache) {
//     const key = url + form.toString();
//     const sessionData = window.sessionStorage.getItem(key);
//     return new Promise((resolve, reject) => {
//       if (sessionData) {
//         //在session中已经存储了相关的数据，避免第二次请求
//         resolve(JSON.parse(sessionData))
//       } else {
//         getFromServer(url, form).then(data => {
//           window.sessionStorage.setItem(key, JSON.stringify(data));
//           resolve(data)
//         }).catch(err => {
//           reject(err);
//         })
//       }
//     })
//   } else {
//     //cache为false的情况下
//     return getFromServer(url, form)
//   }
// }
