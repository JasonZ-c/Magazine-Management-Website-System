import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./plugins/element.js";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(ElementUI);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.config.productionTip = false;
Vue.prototype.$http = axios;

axios.defaults.baseURL = '/api';

let getCookie = function (cookie) {
    let reg = /csrftoken=([\w]+)[;]?/g;
    return reg.exec(cookie)[1];
};

axios.interceptors.request.use(
  function(config) {
    // 在post请求前统一添加X-CSRFToken的header信息
    let cookie = document.cookie;
    if(cookie && config.method == 'post'){
      config.headers['X-CSRFToken'] = getCookie(cookie);
    }
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
