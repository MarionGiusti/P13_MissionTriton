<template>
  <v-container>
    <v-row>
      <v-col
        cols="12"
        md="4"
        v-for="(missionGroup, i) in missionGroups"
        :key="i"
      >
        <div align="center">
          <h3>{{ missionGroup.name }}</h3>
          <v-card class="mission-wrap" elevation="16" width="300">
            <v-virtual-scroll
              :bench="benched"
              :items="missionGroup.missions"
              height="200"
              item-height="60"
            >
              <template v-slot:default="{ item, i }">
                <v-list-item
                  :key="i"
                  router
                  :to="{ name: 'HomeMission', params: { id: item.id } }"
                  @click="loadShippos(item.id)"
                >
                  <v-list-item-content>
                    <v-list-item-title>
                      <strong> {{ item.name }} </strong> / Départ :
                      {{ item.start_date }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-divider></v-divider>
              </template>
            </v-virtual-scroll>
          </v-card>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "ScrollAllMissions",
  data: () => ({
    benched: 0
  }),

  computed: {
    ...mapGetters(["pastMissions", "nowMissions", "futureMissions"]),

    missionGroups() {
      return [
        {
          name: "Archivées",
          missions: this.pastMissions
        },
        {
          name: "En cours",
          missions: this.nowMissions
        },
        {
          name: "À venir",
          missions: this.futureMissions
        }
      ];
    }
  }
};
</script>

<style lang="scss" scoped>
.mission-wrap {
  background-color: #a3b3d5;
}

h3 {
  font: 400 20px "Dosis" !important;
}
</style>
