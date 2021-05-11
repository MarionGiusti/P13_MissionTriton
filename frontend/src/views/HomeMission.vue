<template>
  <v-main>
    <v-container class="d-flex flex-column background-wrap" fluid>
      <v-row >
        <v-col cols="12">
          <h2>Actu </h2>
          <v-divider/>
        </v-col>
        <v-col cols="12">
          <Actu/>
        </v-col>
        <v-col cols="12">
          <h2>Where is the ship ?</h2>
          <v-divider/>
          <Map/>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import Map from '@/components/Map'
import Actu from '@/components/Actu'

export default {
  name: 'HomeMission',
  components: {
    Map,
    Actu,
  }, 
}
</script>

<style lang="scss" scoped>
  .home-carousel {
    height: 500px !important;
  }
  
  .background-wrap {
    margin-top: 40px;
    background-color:#54658C;
    width: 95%;
  }
</style>