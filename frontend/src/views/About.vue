<template>
  <v-main>
    <v-container class="d-flex flex-column background-wrap" fluid>
      <h2>Notre mission</h2>
      <v-divider />
      <div class="text-end">
        <v-btn
          class="mt-4 mr-12"
          icon
          outlined
          color="#A3B3D5"
          @click="deleteMission()"
          v-if="verifMember == true"
        >
          <v-icon>
            mdi-delete
          </v-icon>
        </v-btn>
      </div>
      <MissionGoals />
      <h2>Notre Equipe</h2>
      <v-divider />
      <Team />
      <h2 class="hidden-sm-and-down">Nos moments clés</h2>
      <v-divider class="hidden-sm-and-down" />
      <Timeline class="hidden-sm-and-down" />
    </v-container>
  </v-main>
</template>

<script>
import MissionGoals from "@/components/MissionGoals";
import Team from "@/components/Team";
import Timeline from "@/components/Timeline";
import { mapGetters } from "vuex";
import { getAPI } from "../axios-api";

export default {
  name: "About",
  components: {
    MissionGoals,
    Team,
    Timeline
  },

  computed: {
    ...mapGetters(["currentMission"]),
    missionD() {
      return this.currentMission(this.$route.params.id);
    },
    ...mapGetters(["memberMission"]),
    verifMember() {
      return this.memberMission(this.$route.params.id);
    }
  },

  methods: {
    async deleteMission() {
      await getAPI.delete(`/api/missions/${this.missionD.id}/`, {
        headers: { Authorization: "Token " + this.$store.state.token }
      });
      this.$router.push("/");
    }
  }
};
</script>

<style lang="scss" scoped>
.background-wrap {
  margin-top: 40px;
  background-color: #54658c;
  width: 95%;
}
</style>
