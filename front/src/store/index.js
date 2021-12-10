import Vue from 'vue';
import Vuex from 'vuex';
import { loginUser, logoutUser} from '../api/auth';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    isLoggedIn: false,
  },
  mutations: {
    loginSuccess(state, userId) {
      state.user = userId;
      state.isLoggedIn = true;
    },
    logout(state) {
      state.user = null;
      state.isLoggedIn = false;
    },
  },
  actions: {
    login({ commit }, { username, password }) {
      return loginUser(username, password)
        .then((res) => {
          console.log(res);
          if(res == 'success'){
            commit({ type: 'loginSuccess', username });
            return Promise.resolve();
          }
          else{
            return Promise.reject();
          }
        }).catch((error) => {
          commit({ type: 'logout' });
          return Promise.reject(error);
        });
    },
    logout({ commit }) {
      logoutUser();
      commit('logout');
    },
    //listct(){
      //return listcount();
      //commit('listct');
    //}

  },
  modules: {
  },
});