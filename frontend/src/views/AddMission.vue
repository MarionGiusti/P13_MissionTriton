<template>
  <v-main>
    <v-container>
      <div class="form-wrap" align="center" justify="center">
        <v-form 
          ref="form"
          v-model="valid"
          lazy-validation
          >
            <v-text-field
              label="Nom de la mission"
              prepend-icon="mdi-radiobox-marked"
              type="text"
              color="teal"
              v-model="form.name"
              required
              :rules="[v => !!v || 'Item is required']"
            />
            <v-text-field
              label="Nom du navire"
              prepend-icon="mdi-duck"
              type="text"
              color="teal"
              v-model="form.ship"
              required
              :rules="[v => !!v || 'Item is required']"
            />
            <v-text-field
              label="Date de début"
              prepend-icon="mdi-clock-start"
              type="text"
              color="teal"
              v-model="form.start_date"
              required
              :rules="[v => !!v || 'Item is required']"
            />
            <v-text-field
              label="Date de fin"
              prepend-icon="mdi-clock-end"
              type="text"
              color="teal"
              v-model="form.end_date"
              required
              :rules="[v => !!v || 'Item is required']"
            />
        </v-form>
        <v-btn 
          class="btn"
          :disabled="!valid"
          outlined
          @click="addMission(form)"
        >Ajouter</v-btn>
      </div>
    </v-container>
  </v-main>
</template>

<script>
// import { mapActions } from 'vuex'

export default {
  name: 'AddMission',
  components: {
  },

 data () {
    return {
        valid: true,
        form: {
          name:"",
          ship:"",
          start_date:"",
          end_date:"",
        }
    }
  },

  methods: {
    async addMission({name, ship, start_date, end_date }) {
      console.log('form:', {name, ship, start_date, end_date })
      if (this.$refs.form.validate()) {
        console.log(this.valid)
        await this.$store
          .dispatch('missionRegister', { name, ship, start_date, end_date })
          .then(() => console.log('addMission ok'))
          .then(() => this.$router.push('/'))
          .catch(err => {
            console.log(err)
          });
      }
    }
  },
}
</script>

<style lang="scss" scoped>
.form-wrap {
  width: 60%;
  margin: auto;
}

.btn {
  margin:auto;
  color: rgb(60, 173, 173); 
}
</style>
