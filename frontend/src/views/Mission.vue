<template>
  <div>
    <NavLink>
      <NavMission />
    </NavLink>
    <router-view />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import NavLink from "@/components/NavLink";
import NavMission from "@/components/NavMission";

export default {
  name: "Mission",
  components: {
    NavLink,
    NavMission
  },

  beforeCreate() {
    try {
      this.$store.dispatch("loadMissionList");
    } catch (err) {
      console.log(`erreur: ${err}`);
    }
  },

  computed: {
    ...mapGetters(["pastMissions", "nowMissions", "futureMissions"])
  }
};
</script>
