<template>
  <v-app-bar
    app
    flat
    shrink-on-scroll
    prominent
    color="#A3D0CA"
  >
    <v-toolbar-title>
      <router-link to="/">
      <v-img
        class="mx-2"
        src="../assets/logo_triton.png"
        max-height="160"
        max-width="160"
        margin-top="6"
        contain
      >
      </v-img></router-link>
    </v-toolbar-title>
    <v-toolbar-title class="d-flex justify-center ml-16 pl-16" >
      <div  >
        <h1 v-if="id && missionD" class="mission-title">{{ missionD.name }}</h1>
        <h3 v-if="id && missionD " class="mission-title">{{ missionD.ship_name }}</h3>
      <!-- <h1 v-if="id">{{missionDetails.name}}</h1> -->
      <!-- <h3 v-if="id">{{missionDetails.ship_name}}</h3> -->
      </div>
    </v-toolbar-title>
 
    
    <v-spacer></v-spacer>

    <v-menu
      bottom
      left
      v-if="token!==null"
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
        <!-- <v-list-item
          v-for="(mission, i) in missionList" 
          :key="i" router :to="{name: 'HomeMission', params: {id: mission.id}}"
        > -->
        <v-list-item
          v-for="(mission, i) in missions" 
          :key="i" router :to="{name: 'HomeMission', params: {id: mission.id}}"
        >
          <v-list-item-title>{{ mission.name }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <v-menu
      bottom
      left
      v-if="token!==null"
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
          v-for="(item, i) in itemsLog"
          :key="i" router :to="{name: item.route, params: {userId: user_id}}" @click="item.action"
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
        itemsLog: [
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
            title:"Ajouter une mission",
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
    watch: {
    //   '$route'(to, from) {
    //     console.log('to', to);
    //     console.log('from', from);
    //     if(to !== from ) {
    //       this.id = this.$route.params.id;
    //       console.log('id', this.id)
    //     }
    //   }, 
    },

    // mounted(){
    //   // this.cuMission()
    // },

    computed: {
      ...mapState([ 'token' ]),
      ...mapState([ 'user_id' ]),
      // ...mapState([ 'missionList' ]),
      //OLD
      // ...mapState([ 'missionDetails' ]),
      ...mapState([ 'missions' ]),
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
      }   
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