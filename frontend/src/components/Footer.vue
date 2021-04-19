<template>
  <v-container>
    <v-footer
        padless
        color="#A3D0CA"
      >   
      <v-row
        justify="center"
        no-gutters
      >
        <v-col align="center">
            <v-btn text
            v-for="(item, i) in items"
            :key="i" :to="{name: item.route}"
          >
            {{ item.title }}
          </v-btn>
          <!-- <v-list>
            <v-list-item
              v-for="item in items"
            :key="i" router :to="{name: item.route}"
            >
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list> -->
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
      items: [
        {
          title:"Accueil",
          route:"Home",
          action: "",
        },
        {
          title:"Mission Triton",
          route:"Home",
          action: "",
        },
        {
          title:"Contact",
          route:"Home",
          action: "",
        },
        {
          title:"Mentions Légales",
          route:"LegalMentions",
          action: "",
        },
      ]
    }),
  }

</script>

<style lang="scss" scoped>

</style>