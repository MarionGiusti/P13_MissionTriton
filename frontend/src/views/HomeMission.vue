<template>
  <v-main>
    <v-container class="d-flex flex-column background-wrap" fluid>
      <v-row >
        <v-col cols="12">
          <h1>Actu</h1>
          <v-divider/>
        </v-col>
        <v-col cols="12">
          <Post/>
        </v-col>
        <v-col cols="12">
          <h1>Where is the ship ?</h1>
          <v-divider/>
          <Map/>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>

import Map from '@/components/Map'
import Post from '@/components/Post'
import { mapGetters } from 'vuex'

export default {
  name: 'HomeMission',
  components: {
    Map,
    Post,
  },
  data() {
      return {
        items: [
          {
            src: require("../assets/seascape.jpg"),
          },
          {
            src:require("../assets/logo.png"),
          },
        ]
      }
  },

  computed: {
    // ...mapState([
      // 'allMissions',
      // 'missionDetails'
    // ])
    ...mapGetters([ 'currentMission' ]),
      missionD() {
        return this.currentMission(this.$route.params.id)
      },

  },
}
</script>

<style lang="scss" scoped>
.home-carousel {
  height: 500px !important;
}
// #98ACD7
.background-wrap {
  margin-top: 40px;
  background-color:#54658C;
  width: 95%;
}
</style>