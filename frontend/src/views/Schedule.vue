<template>
  <v-main>
    <v-container class="d-flex flex-column background-wrap" fluid>
      Agenda
      <Calendar/>
    </v-container>
  </v-main>
</template>

<script>
import Calendar from '@/components/Calendar'

  export default {
    name: 'Schedule',
    components: {
      Calendar,
    },
  }
</script>

<style lang="scss" scoped>
  .background-wrap {
    margin-top: 40px;
    background-color:#B6885D;
    width: 95%;
  }
</style>