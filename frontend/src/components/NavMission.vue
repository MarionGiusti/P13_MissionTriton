<template>
  <v-tabs right>
    <v-tab v-for="item in items" :key="item.title" router :to="{name: item.name}" replace>
    {{ item.title }}
    </v-tab>
  </v-tabs>
</template>


<script>
  export default {
    name: 'NavMission',
    data() {
      return {
        items: [
          {
            title:"Actualité",
            name: "HomeMission"
          },
          {
            title:"À propos",
            name: "About"
          },
          {
            title:"Médiation",
            name: "Mediation"
          },
          {
            title:"À bord",
            name: "OnBoard"
          },
          {
            title:"Photos",
            name: "Gallery"
          },
        ]
      }
    },
    
  }

</script>

<style scoped>


</style>
