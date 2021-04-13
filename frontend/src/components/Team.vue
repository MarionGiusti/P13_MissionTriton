<template>
  <v-container>
    <!-- <h2 class="text-center">Notre équipe scientifique</h2>
    <v-divider/> -->
    <v-row align="center" >
      <v-col v-for="item in proitems" :key="item.id" cols="4" align="center">
        <v-card
          class="mx-auto"
          flat
        > 
            <v-img
              :src="item.src"
              max-height="100"
              max-width="100"
              contain
            >
            </v-img>
          <!-- <v-avatar
            class="profile"
            color="grey"
            size="164"
            tile
          >
            <v-img :src="item.src"></v-img>
          </v-avatar> -->

          <v-card-subtitle class="pb-0 text-center">
            {{ item.name }}
          </v-card-subtitle>

          <v-card-text class="text--primary text-center">
            <div>{{ item.job }}</div>
          </v-card-text>

          <v-card-actions class="justify-center">
            <v-btn
            icon
            >
              <v-img
                class="mx-2"
                src="../assets/icon_rg.png"
                alt="researchgate_icon"
                max-height="30"
                max-width="30"
                contain
                >
              </v-img>
            </v-btn>
            <v-btn
            icon
            >
              <v-img
                class="mx-2"
                src="../assets/icon_in.png"
                alt="linkedin_icon"
                max-height="30"
                max-width="30"
                contain
              >
              </v-img>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'Team',
    data() {
      return {
        proitems: [
          {
            id:1,
            src:require('../assets/profile.png'),
            name:'Oscar Pellen',
            job:'Chercheur en géophysique marine',
          },
          {
            id:2,
            src:require('../assets/profile.png'),
            name:'Elie Chollon',
            job:'Technicienne acoustique',
          },
          {
            id:3,
            src:require('../assets/profile.png'),
            name:'Sophie Olivarez',
            job:'Chercheur en géochimie',
          },
          {
            id:4,
            src:require('../assets/profile.png'),
            name:'Lucien Heurtevent',
            job:'Ingénieur acousticien',
          },
        ]
      }
    } 
  }

</script>

<style lang="scss" scoped>

</style>