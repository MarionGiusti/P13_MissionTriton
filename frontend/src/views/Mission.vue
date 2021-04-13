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
import {mapState} from 'vuex'
import { mapActions } from 'vuex'

import NavLink from '@/components/NavLink'
import NavMission from '@/components/NavMission'

export default {
  name: 'Mission',
  components: {
    NavLink,
    NavMission,
  },

// created() {
    // this.$store.state.id_mission = this.$route.params.id;
// },

  destroyed() {
    this.$store.missionDetails = {}
  },

  watch: {
    '$route'(to, from) {
      console.log('to', to);
      console.log('from', from);
      if(to !== from ) {
        this.$store.dispatch('loadMissionDetails', this.$route.params.id);
        console.log('reload loadMossionDetails')
      }
    }
  },

  mounted() {
    console.log('CHOUOOOU', this.$route.params.id, "idmission", this.$store.state.id_mission)
    this.$store
      .dispatch('loadMissionDetails', this.$route.params.id)
      .then(() => console.log('loadMissionDetails ok', this.$store.state.missionDetails))
      .catch(err => {
        console.log(err)
      });
},

  data() {
    return {
        id: this.$route.params.id,
      }
  },

  computed: {
    ...mapState([
      'allMissions',
      'missionDetails'
    ])
  },
  methods: {
    ...mapActions([
        'loadIdMission',
      ]),
  },
}

</script>

<style lang="scss" scoped>

</style>