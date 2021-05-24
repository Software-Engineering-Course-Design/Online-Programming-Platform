import axios from "axios";

//post请求封装
export function post(url, postData) {
  return new Promise((resolve, reject) => {
    axios.post(url, postData).then(response => {
      if (response.status === 200) {
        resolve(response.data);
      } else {
        reject(response.data.msg);
      }
    }).catch(e => {
      reject(e);
    })
  })
}

//get请求封装
export function get(url, params) {
  return new Promise((resolve, reject) => {
    axios.get(url, params).then(response => {
      if (response.status === 200) {
        resolve(response.data);
      } else {
        reject(response.data.msg);
      }
    }).catch(e => {
      reject(e);
    })
  })
}

