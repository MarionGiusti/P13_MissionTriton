<template>
  <v-app>
    <NavLink/>
    <!-- <v-main > -->
    <!-- <v-container class="fill-height" fluid> -->
      <router-view/>
    <!-- </v-container> -->
    <!-- </v-main> -->
    <v-footer color="#A3D0CA">
      <Footer/>
    </v-footer> 
  </v-app> 
</template>

<script>
import NavLink from './components/NavLink.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    NavLink,
    Footer,
  },

  mounted() {
    this.$store
      .dispatch('loadMissionList')
      .catch(err => {
        console.log(err)
      });
  },

};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Dosis:wght@200;400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Amatic+SC:wght@400;700&display=swap');

html, body {
  font-family: 'Dosis';
  font-weight: 400;
}

#app {
  font-family: 'Dosis';
}
</style>
