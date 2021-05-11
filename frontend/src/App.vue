<template>
  <v-app>
    <NavLink/>
      <router-view/>
    <v-footer color="#A3D0CA">
      <Footer/>
    </v-footer> 
  </v-app> 
</template>

<script>
import NavLink from './components/NavLink.vue'
import Footer from './components/Footer.vue'
import {mapState} from 'vuex'

export default {
  name: 'App',
  components: {
    NavLink,
    Footer,
  },

  async mounted() {
    await this.$store.dispatch('loadMissionList')

    if (this.token) {
      await this.$store.dispatch('getUserDetails')
    }
  },

  computed: {
    ...mapState(['token'])
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Dosis:wght@200;400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Amatic+SC:wght@400;700&display=swap');

/* html, body {
  font-family: 'Dosis';
  font-weight: 400;
} */

h2 {
  font: 500 40px  'Amatic SC' !important;
}

#app {
  font-family: 'Dosis';
  font-weight: 400;
}
</style>
