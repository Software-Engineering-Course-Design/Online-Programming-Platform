import axios from "axios";

const ERR_OK = 0;
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
/* 统一封装get请求 */
// export const get = (url, params) => {
//   return new Promise((resolve, reject) => {
//     instance({
//       method: 'get',
//       url,
//       params,
//     }).then(response => {
//       resolve(response)
//     }).catch(error => {
//       reject(error)
//     })
//   })
// }

// /* 统一封装post请求  */
// export const post = (url, data) => {
//   return new Promise((resolve, reject) => {
//     instance({
//       method: 'post',
//       url,
//       data,
//     }).then(response => {
//       resolve(response)
//     }).catch(error => {
//       reject(error)
//     })
//   })
// }
