<template>
  <div>
    <NavLink>
      <NavMission/>
    </NavLink>
    <!-- <v-container class="fill-height" fluid> -->
    <router-view />
      <!-- <router-view :key="$route.fullPath"/> -->
    <!-- </v-container> -->
  </div>
</template>

<script>
// import {mapState} from 'vuex'
// import { mapActions } from 'vuex'
import { mapGetters } from 'vuex'

import NavLink from '@/components/NavLink'
import NavMission from '@/components/NavMission'

export default {
  name: 'Mission',
  components: {
    NavLink,
    NavMission,
  },

  // destroyed() {
  //   this.$store.missionDetails = {}
  // },

// Plus besoin des watchs avec getter ?
  // watch: {
  //   '$route'(to, from) {
  //     console.log('to', to);
  //     console.log('from', from);
  //     if(to !== from ) {
  //       // this.$store.dispatch('loadMissionDetails', this.$route.params.id);
  //       this.$store.getters.currentMission(this.$route.params.id)
  //       console.log('reload loadMossionDetails')
  //     }
  //   }
  // },

  // mounted() {
    // console.log('CHOUOOOU', this.$route.params.id, "idmission", this.$store.state.id_mission)
    // this.$store
    //   .dispatch('loadMissionDetails', this.$route.params.id)
    //   .then(() => console.log('loadMissionDetails ok', this.$store.state.missionDetails))
    //   .catch(err => {
    //     console.log(err)
    //   });

    // console.log('geeeet', this.$store.getters.currentMission(this.$route.params.id))
  // },

  data() {
    return {
        id: this.$route.params.id,
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
      }

  },

  methods: {
    // ...mapActions([
    //     'loadIdMission',
    //   ]),
  },
}

</script>

<style lang="scss" scoped>

</style>