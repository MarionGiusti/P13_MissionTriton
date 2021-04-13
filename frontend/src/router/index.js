import Vue from 'vue'
import VueRouter from 'vue-router'

import About from '../views/About.vue'
import Account from '../views/Account.vue'
import AddMission from '../views/AddMission.vue'
import Gallery from '../views/Gallery.vue'
import Home from '../views/Home.vue'
import HomeMission from '../views/HomeMission.vue'
import Login from '../views/Login.vue'
import Mediation from '../views/Mediation.vue'
import Mission from '../views/Mission.vue'
import OnBoard from '../views/OnBoard.vue'
import Register from '../views/Register.vue'
import Schedule from '../views/Schedule.vue'



Vue.use(VueRouter)

const routes = [
  {
    name: 'Account',
    path: '/account/:userId',
    component: Account,
  },
  {
    name: 'AddMission',
    path: '/add-mission/:userId',
    component: AddMission,
  },
  {
    name: 'Home',
    path: '/',
    component: Home,
  },
  {
    name: 'Login',
    path: '/login',
    component: Login,
  },
  {
    path: '/mission/:id',
    component: Mission,
    children: [
      {
        name: 'HomeMission',
        path: '/mission/:id/',
        component: HomeMission
      },
      {
        name: 'About',
        path: 'about',
        component: About
      },
      {
        name: 'Mediation',
        path: 'mediation',
        component: Mediation
      },
      {
        name: 'OnBoard',
        path: 'onboard',
        component: OnBoard
      },
      {
        name: 'Gallery',
        path: 'gallery',
        component: Gallery
      },
    ],
  },
  {
    name: 'Register',
    path: '/register',
    component: Register,
  },
  {
    name: 'Schedule',
    path: '/schedule/:userId',
    component: Schedule,
  },
]

const router = new VueRouter({
  routes,
  mode: "history"
})

export default router
