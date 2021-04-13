<template>
  <v-main>
    <v-container>
      <v-row>
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
}
</script>

<style lang="scss" scoped>
.home-carousel {
  height: 500px !important;
}
</style>