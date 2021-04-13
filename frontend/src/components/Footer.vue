<template>
  <v-container>
    <v-footer
        padless
      >   
      <v-row
        justify="center"
        no-gutters
      >
        <v-col align="center">
          <v-btn
            v-for="link in links"
            :key="link"
            text
          >
            {{ link }}
          </v-btn>
        </v-col>
        <v-col
          class="text-center"
          cols="12"
          align="center"
        >
          {{ new Date().getFullYear() }} — <strong>Mission Triton</strong>
        </v-col>
      </v-row>
    </v-footer>
  </v-container>
</template>

<script>
  export default {
    name: 'Footer',
    data: () => ({
      links: [
        'Accueil',
        'Mission Triton',
        'Contact',
        'Mentions Légales'
      ],
    }),
  }

</script>

<style lang="scss" scoped>

</style>