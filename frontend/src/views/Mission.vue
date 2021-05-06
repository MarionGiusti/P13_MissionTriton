<template>
  <div>
    <NavLink>
      <NavMission />
    </NavLink>
    <router-view />
  </div>
</template>

<script>
// import {mapState} from 'vuex'
// import { mapActions } from 'vuex'
// import { mapGetters } from 'vuex'

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
  watch: {
    '$route'(to, from) {
      // console.log('to', to);
      // console.log('from', from);
      if(to !== from ) {
        this.currentMission()
        // this.$store.dispatch('loadMissionDetails', this.$route.params.id);
        // console.log('reload loadMissionDetails')
      }
    }
    // id(newValue, oldValue) {
    //     console.log(`lala ${newValue} ${oldValue}`);
    //     this.currentMiss();
    //   }
  },

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
      }
  },

  beforeCreate() {
    this.$store
      .dispatch('loadMissionList')
      .catch(err => {
        console.log(err)
      });
    // this.currentMission()
  },

  computed: {
    // ...mapState([
      // 'allMissions',
      // 'missionDetails',
      // 'missions',
    // ])
  
    // ...mapGetters([ 'currentMission' ]),
    //   missionD() {
    //     return this.currentMission(this.$route.params.id)
    //   }
  },

  methods: {
    // replace getter currentMission
  //   currentMission () {
  //       this.$store
  //         .dispatch('getCurrentMission', this.$route.params.id)
  //         .then(() => console.log('getCurrentMission ok'))
  //         .catch(err => {
  //           console.log(err)
  //         });
  //     }
  },
}

</script>

<style lang="scss" scoped>

</style>