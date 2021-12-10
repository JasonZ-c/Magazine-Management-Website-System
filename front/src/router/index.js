import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from '../views/Login.vue';
import About from '../views/About.vue';
import Tasklist from '../views/Tasklist.vue';
import Detail from '../views/Detail.vue';
import Mine from '../views/Mine.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/tasklist/:name',
    name: 'Tasklist',
    component: Tasklist,
  },
  {
    path: '/tasklist/:name/:id',
    name: 'detail',
    component: Detail,
  },
  {
    path: '/mine',
    name: 'mine',
    component: Mine,
  },  
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
