<template>
<v-main>
  <!-- <v-container fluid> -->
    <HeroBlock/>
  <!-- </v-container> -->
</v-main>
</template>

<script>
import {mapState} from 'vuex'
import HeroBlock from '@/components/HeroBlock'

export default {
  name: 'Home',
  components: {
    HeroBlock,
  },

  mounted() {
    this.$store
      .dispatch('loadMissionList')
      .catch(err => {
        console.log(err)
      });
  },
  computed: {
    ...mapState([
      'allMissions'
    ])
  },
}
</script>

<style lang="scss" scoped>

</style>