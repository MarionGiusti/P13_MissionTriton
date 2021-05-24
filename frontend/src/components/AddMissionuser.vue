<template>
  <v-container>
    <div class="form-wrap" align="center" justify="center">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          label="Nom de la mission"
          prepend-icon="mdi-radiobox-marked"
          type="text"
          color="teal"
          v-model="form.mission"
          required
          :rules="[v => !!v || 'Item is required']"
        />
        <v-text-field
          label="Email du participant"
          prepend-icon="mdi-email"
          type="email"
          color="teal"
          v-model="form.email"
          required
          :rules="[v => !!v || 'Item is required']"
        />
      </v-form>
      <v-btn
        class="btn"
        :disabled="!valid"
        outlined
        @click="addMissionuser(form)"
      >
        Ajouter
      </v-btn>
    </div>
  </v-container>
</template>

<script>
import { getAPI } from "../axios-api";

export default {
  name: "AddMissionuser",

  data() {
    return {
      form: {
        mission: "",
        email: ""
      },
      valid: true
    };
  },

  methods: {
    async addMissionuser({ mission, email }) {
      if (this.$refs.form.validate()) {
        await getAPI.post("/api/users/missionusers/", this.form, {
          headers: {
            Authorization: "Token " + this.$store.state.token,
            "Content-Type": "application/json"
          }
        });
        alert(
          `L'utilisateur ${email} a bien été ajouté à la mission ${mission} !`
        );
        this.resetForm();
      }
    },
    resetForm() {
      this.$refs.form.reset();
    }
  }
};
</script>

<style lang="scss" scoped>
.form-wrap {
  width: 60%;
  margin: auto;
}

.btn {
  margin: auto;
  color: rgb(60, 173, 173);
}
</style>
