<template>
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
      >Ajouter</v-btn>
    </div>
  </v-container>
</template>

<script>
import { getAPI } from '../axios-api'

export default {
  name: 'AddMissionuser',
  components: {
  },

 data () {
    return {
        valid: true,
        form: {
          mission:"",
          email:"",
        }
    }
  },

  methods: {
    async addMissionuser({mission, email}) {
      console.log('form:', {mission, email })
      if (this.$refs.form.validate()) {
        console.log(this.valid)
        
        await getAPI.post('/api/users/missionusers/', 
        this.form, {
          headers: { 
            'Authorization': 'Token ' + this.$store.state.token,
            'Content-Type': 'application/json',   
          }
          })
        .then(() => console.log('addMissionuser ok', this.form))
        .then(() => alert("L'utilisateur:"+ email + " a bien été enregistré !"))
        .catch(err => {console.log(err)}); 
      }
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
