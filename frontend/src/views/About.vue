<template>
  <v-main>
    <v-container>
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
