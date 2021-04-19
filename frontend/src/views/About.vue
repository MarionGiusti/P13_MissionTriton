<template>
  <v-main>
    <v-container  class="d-flex flex-column background-wrap" fluid >
      <h2>Notre mission</h2>
      <v-divider/>
      <MissionGoals/>
      <h2>Notre Equipe</h2>
      <v-divider/>
      <Team/>
      <h2>Nos moments clés</h2>
      <v-divider/>
      <Timeline/>
    </v-container>
  </v-main>
</template>

<script>
import MissionGoals from '@/components/MissionGoals'
import Team from '@/components/Team'
import Timeline from '@/components/Timeline'

  export default {
    name: 'About',
    components: {
      MissionGoals,
      Team,
      Timeline,
    },

    data () {
      return {

      }
    },
  }
</script>

<style lang="scss" scoped>

.background-wrap {
  margin-top: 40px;
  background-color:#54658C;
  width: 95%;
}
</style>
