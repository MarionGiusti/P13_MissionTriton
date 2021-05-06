<template>
  <v-app-bar
    app
    flat
    shrink-on-scroll
    prominent
    color="#A3D0CA"
  >
    <!-- <v-toolbar-title> -->
      <!-- <router-link to="/">
      <v-img
        class="mx-2"
        src="../assets/logo_triton.png"
        max-height="160"
        max-width="160"
        margin-top="6"
        contain
      >
      </v-img></router-link> -->
    <!-- </v-toolbar-title> -->
    <!-- <v-toolbar-title class="d-flex justify-center ml-16 pl-16"> -->
    <v-toolbar-title >

      <v-row >
        <v-col cols="12" sm="6">
          <router-link to="/">
          <v-img
            class="mx-2"
            src="../assets/logo_triton.png"
            max-width="160"
            contain
          >
          </v-img></router-link>
        </v-col>
        <v-col cols="6" class="hidden-xs-only" v-if="this.$route.params.id && missionD">
      <!-- <div  class="justify-center"> -->
        <h1 class="mission-title">{{ missionD.name }}</h1>
        <h3 class="mission-title">{{ missionD.ship_name }}</h3>
      <!-- </div> -->
        </v-col>
      </v-row>
    </v-toolbar-title>
 
    
    <v-spacer></v-spacer>

    <div class="d-flex flex-row flex-wrap justify-space-between" >

      <v-menu
        bottom
        left
        v-if="token!==null && userDetails.missions.length!==0"
        > 
        
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            dark
            v-bind="attrs"
            v-on="on"
            color="teal"
            fab
            large
          >
            <v-icon x-large>mdi-magnify</v-icon>
          </v-btn>
        </template>
        <v-list>
          <!-- GOOD <v-list-item
            v-for="(mission, i) in missions" 
            :key="i" router :to="{name: 'HomeMission', params: {id: mission.id}}"
          > -->
          <v-list-item
            v-for="(mission, i) in userDetails.missions" 
            :key="i" router :to="{name: 'HomeMission', params: {id: mission.id}}"
          >
            <v-list-item-title>{{ mission.name }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-menu
        bottom
        left
        v-if="(token && userId)"
        >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            dark
            v-bind="attrs"
            v-on="on"
            color="teal"
            fab
            large
          >
            <v-icon x-large>mdi-account-circle</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="(item, i) in items"
            :key="i" router :to="{name: item.route, params: {userId: userId}}" @click="item.action"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-btn
        icon
        large
        fab
        id="no-background-hover" 
        to="/login" 
        v-if="token==null"
      >
        <v-icon x-large>mdi-login-variant</v-icon>
      </v-btn>
    </div>

    <template v-slot:extension>
      <slot></slot>
    </template> 
  </v-app-bar>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

  export default {
    name: 'NavLink',
    components:{
    },
    data() {
      return {
        id: this.$route.params.id,
        items: [
          {
            title:"Mon compte",
            route:"Account",
            action: "",
          },
          {
            title:"Mon agenda",
            route:"Schedule",
            action: "",
          },
          {
            title:"Ajouter une mission / participant",
            route:"AddMission",
            action: "",
          },
          {
            title:"Se déconnecter",
            route:"Home",
            action: this.logout,
          },
        ],
      }
    },

// Plus besoin des watchs avec getter ?
    // watch: {
    //   '$route'(to, from) {
    //     // console.log('to', to);
    //     // console.log('from', from);
    //     if(to !== from ) {
    //       this.currentMission()
    //     }
    //   }, 

    computed: {
      ...mapState([ 'token', 'userId' ]),
      ...mapState([ 'userDetails' ]),
      ...mapGetters([ 'currentMission' ]),
      missionD() {
        return this.currentMission(this.$route.params.id)
      },
    },

    methods: {
      logout () {
        this.$store
          .dispatch('userLogout')
          .then(() => console.log('logout ok', this.token ))
          .catch(err => {
            console.log(err)
          });
      },     
    },    
  }
</script>

<style scoped>
  #no-background-hover::before {
    background-color: transparent;
  }
  .mission-title{
    color:#09033E;
  }
</style>