<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <router-link to="/" tag="b-navbar-brand">中国科学技术大学论文网站</router-link>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <router-link v-if="!isLoggedIn" to="/login" tag="b-nav-item">Login</router-link>
          <b-nav-item v-else v-on:click="handleLogout" tag="b-nav-item">Logout</b-nav-item>
        </b-navbar-nav>
        
        <b-navbar-nav>
          <router-link v-if="isLoggedIn" to="/mine" tag="b-nav-item">我的主页</router-link>
          <b-nav-item v-else tag="b-nav-item">登录后查看个人主页</b-nav-item>
        </b-navbar-nav>
        
      </b-collapse>
    </b-navbar>
    <router-view v-if="isRouterAlive"></router-view>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'App',//<router-view/>
  computed: {
    ...mapState(['isLoggedIn']),
  },
  provide(){
	return {
		reload: this.reload
	}
  },
  data(){
	return {
		isRouterAlive:true
	}
  }, 
  methods: {
    handleLogout(event) {
      event.preventDefault();
      this.logout();
      this.$router.push('/');
    },
    reload(){
	    this.isRouterAlive=false
		this.$nextTick(()=>this.isRouterAlive=true)
	},
    ...mapActions(['logout']),
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
