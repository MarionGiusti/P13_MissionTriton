<template>
  <v-main >
      <HeroBlock/>
      <v-container  class="missions-wrap" fluid >
        <div class="d-flex flex-column mb-4">
          <h2 class="text-center">Nos Missions</h2>
          <v-divider/>
        </div>
      <ScrollAllMissions/>
      </v-container>
  </v-main>
</template>

<script>
import HeroBlock from '@/components/HeroBlock'
import ScrollAllMissions from '@/components/ScrollAllMissions'

export default {
  name: 'Home',
  components: {
    HeroBlock,
    ScrollAllMissions,
  },

  async mounted() {
    await this.$store.dispatch('loadMissionList')
  },
}
</script>

<style lang="scss" scoped>
  .missions-wrap {
    margin-top: 40px;
    background-color:#54658C;
    width: 95%;
  }
</style>