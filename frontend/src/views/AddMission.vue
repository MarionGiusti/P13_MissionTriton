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
            <v-menu
              v-model="menu1"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="form.start_date"
                  label="Date de début"
                  prepend-icon="mdi-clock-start"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  required
                  :rules="[v => !!v || 'Item is required']"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="form.start_date"
                @input="menu1 = false"
              ></v-date-picker>
            </v-menu>
            <v-menu
              v-model="menu2"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="form.end_date"
                  label="Date de fin"
                  prepend-icon="mdi-clock-end"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  required
                  :rules="dateRules"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="form.end_date"
                @input="menu2 = false"
              ></v-date-picker>
            </v-menu>
        </v-form>
        <v-btn 
          class="btn"
          :disabled="!valid"
          outlined
          @click="addMission(form)"
        >Ajouter</v-btn>
      </div>
       <!-- <AddMissionuser/> -->

    </v-container>
  </v-main>
</template>

<script>
// import { mapActions } from 'vuex'
// import AddMissionuser from '@/components/AddMissionuser'

export default {
  name: 'AddMission',
  components: {
    // AddMissionuser,
  },

 data () {
    return {
        menu1: false,
        menu2: false,

        valid: true,
        form: {
          name:"",
          ship:"",
          start_date:"",
          end_date:"",
        },
        dateRules: [
          v => !!v ,
          v => (v && v > this.form.start_date) || 'Date de fin avant date début',
        ],
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
          // .then(() => this.$router.push('/'))
          .then(() => alert(`La mission: ${name} a bien été enregistrée !`))
          .then(() => this.resetForm())
          .then(() => this.$store.dispatch('loadMissionList'))
          .catch(err => {
            console.log(err)
          });
      }
    },
    resetForm(){
      this.$refs.form.reset()
    },
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
