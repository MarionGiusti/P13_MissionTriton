<template>
  <v-container>
    <v-footer padless color="#A3D0CA">
      <v-row justify="center" no-gutters>
        <v-col align="center">
          <v-btn
            text
            v-for="(item, i) in items"
            :key="i"
            :to="{ name: item.route }"
          >
            {{ item.title }}
          </v-btn>
        </v-col>
        <v-col class="text-center" cols="12" align="center">
          {{ new Date().getFullYear() }} — <strong>Mission Triton</strong>
        </v-col>
      </v-row>
    </v-footer>
  </v-container>
</template>

<script>
export default {
  name: "Footer",
  data: () => ({
    items: [
      {
        title: "Accueil",
        route: "Home"
      },
      {
        title: "Mentions Légales",
        route: "LegalMentions"
      }
    ]
  })
};
</script>

<style lang="scss" scoped>
.btn focus {
  box-shadow: none;
  outline: none;
}
</style>
