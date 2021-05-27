import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store";

import About from "../views/About.vue";
import Account from "../views/Account.vue";
import AddMission from "../views/AddMission.vue";
import Gallery from "../views/Gallery.vue";
import Home from "../views/Home.vue";
import HomeMission from "../views/HomeMission.vue";
import LegalMentions from "../views/LegalMentions.vue";
import Login from "../views/Login.vue";
import Mediation from "../views/Mediation.vue";
import Mission from "../views/Mission.vue";
import OnBoard from "../views/OnBoard.vue";
import Register from "../views/Register.vue";
import Schedule from "../views/Schedule.vue";

Vue.use(VueRouter);

const routes = [
  {
    name: "Account",
    path: "/account/:userId",
    component: Account,
    beforeEnter: (to, from, next) => {
      if(store.state.token==null) {
        next(false);
      } else {
        next();
      }
    }
  },
  {
    name: "AddMission",
    path: "/add-mission/:userId",
    component: AddMission,
    beforeEnter: (to, from, next) => {
      if(store.state.token==null) {
        next(false);
      } else {
        next();
      }
    }
  },
  {
    name: "Home",
    path: "/",
    component: Home
  },
  {
    name: "LegalMentions",
    path: "/mentions",
    component: LegalMentions
  },
  {
    name: "Login",
    path: "/login",
    component: Login
  },
  {
    path: "/mission/:id",
    component: Mission,
    children: [
      {
        name: "HomeMission",
        path: "/mission/:id/",
        component: HomeMission
      },
      {
        name: "About",
        path: "about",
        component: About
      },
      {
        name: "Mediation",
        path: "mediation",
        component: Mediation
      },
      {
        name: "OnBoard",
        path: "onboard",
        component: OnBoard
      },
      {
        name: "Gallery",
        path: "gallery",
        component: Gallery
      }
    ]
  },
  {
    name: "Register",
    path: "/register",
    component: Register
  },
  {
    name: "Schedule",
    path: "/schedule/:userId",
    component: Schedule,
    beforeEnter: (to, from, next) => {
      if(store.state.token==null) {
        next(false);
      } else {
        next();
      }
    }
  },
  {
    path: "*",
    redirect: "/"
  }
];

const router = new VueRouter({
  routes,
  mode: "history"
});

export default router;
