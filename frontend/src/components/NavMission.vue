<template>
  <v-tabs right>
    <v-tabs right color="#09033E" class="hidden-xs-only">
      <v-tabs-slider color="#09033E"></v-tabs-slider>
      <v-tab
        v-for="item in items"
        :key="item.title"
        router
        :to="{ name: item.name }"
        replace
      >
        {{ item.title }}
      </v-tab>
    </v-tabs>
    <div class="hidden-sm-and-up">
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-app-bar-nav-icon
            v-on="on"
            v-bind="attrs"
            color="#09033E"
          ></v-app-bar-nav-icon>
        </template>
        <v-list>
          <v-list-item
            v-for="(item, index) in items"
            :key="index"
            :to="{ name: item.name }"
            link
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
  </v-tabs>
</template>

<script>
export default {
  name: "NavMission",
  data() {
    return {
      items: [
        {
          title: "Actualité",
          name: "HomeMission"
        },
        {
          title: "À propos",
          name: "About"
        },
        {
          title: "Médiation",
          name: "Mediation"
        },
        {
          title: "À bord",
          name: "OnBoard"
        },
        {
          title: "Photos",
          name: "Gallery"
        }
      ]
    };
  }
};
</script>
