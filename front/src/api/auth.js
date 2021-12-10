import axios from 'axios';
axios.defaults.baseURL = '/api';
// this base url will be change based on
// if you need to point to production.
//const BASE_URL = 'http://127.0.0.1:8080'; //后端地址的前缀


const tokenRequest = axios.create({
  //baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    accept: 'application/json',
  },
});

const loginUser = (username, password) => {
    const formData = new FormData();
    const path = '/login';
	formData.append('username',username);
	formData.append('password',password); 
	let config = {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    };
    return axios.post(path,formData,config).then(function (response) {
        console.log(response);
        return Promise.resolve(response.data);
    }).catch(function (error) {
        return Promise.reject(error);
    })
};

const logoutUser = () => { 
  const path = '/logout';
  return axios.post(path)
    .then((response) => {
      return Promise.resolve(response.data);
    }).catch((error) => {
      console.log(error);
      return Promise.reject(error);
    });
};

const listcount = () => { 
  const path = '/list_count';
  return axios.post(path)
    .then((response) => {
      return response.data;
    }).catch((error) => {
      alert(error);
    });
};

export {
  tokenRequest, loginUser, logoutUser,listcount
};
