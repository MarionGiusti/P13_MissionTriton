<template>
  <v-main>
    <v-container>
      <!-- <v-row align="center" justify="center">
        <v-col> -->
          <!-- <v-card class="card-login" color="indigo lighten-5"> -->
            <!-- <v-card-text> -->
              <div class="form-wrap" align="center" justify="center">
              <v-form 
                ref="form"
                v-model="valid"
                lazy-validation
                >
                  <v-text-field
                    label="Nom d'utilisateur"
                    prepend-icon="mdi-account-circle"
                    type="text"
                    color="teal"
                    v-model="form.username"
                    required
                    :rules="[v => !!v || 'Item is required']"
                  />
                  <v-text-field
                    label="Prénom"
                    prepend-icon="mdi-account"
                    type="text"
                    color="teal"
                    v-model="form.firstname"
                    required
                    :rules="[v => !!v || 'Item is required']"
                  />
                  <v-text-field
                    label="Nom"
                    prepend-icon="mdi-account"
                    type="text"
                    color="teal"
                    v-model="form.lastname"
                    required
                    :rules="[v => !!v || 'Item is required']"
                  />
                  <v-text-field
                    label="Email"
                    prepend-icon="mdi-email"
                    type="email"
                    color="teal"
                    v-model="form.email"
                    required
                    :rules="[v => !!v || 'Item is required']"
                  />
                  <v-text-field
                    label="Mot de passe"
                    prepend-icon="mdi-lock"
                    type="password"
                    color="teal"
                    v-model="form.password1"
                    required
                    :rules="[v => !!v || 'Item is required']"
                  />

                  <v-text-field
                    label="Confirmer mot de passe"
                    prepend-icon="mdi-lock"
                    type="password"
                    color="teal"
                    v-model="form.password2"
                    required
                    :rules="[v => !!v || 'Item is required']"
                  />
              </v-form>
            <!-- </v-card-text> -->
            <!-- <v-card-actions> -->
              <v-btn class="btn" :disabled="!valid" outlined @click="register(form)">S'inscrire</v-btn>
            <!-- </v-card-actions> -->
          <!-- </v-card> -->
              </div>

        <!-- </v-col> -->
      <!-- </v-row> -->
    </v-container>
  </v-main>
</template>

<script>
// import { mapActions } from 'vuex'

export default {
  name: 'Register',
  components: {
  },

  data () {
    return {
        valid: false,
        form: {
          username:"",
          firstname:"",
          lastname:"",
          email:"",
          password1:"",
          password2:"",
        }
    }
  },

  methods: {
    async register ({username, password1, email}) {
      console.log(this.valid)
      if (this.$refs.form.validate()) {
        console.log(this.valid)
        // await mapActions(['userLogin'])
        await this.$store
          .dispatch('userRegister', { username, password1, email })
          .then(() => console.log('register ok'))
          .then(() => this.$router.push('/'))
          .catch(err => {
            console.log(err)
          });
      }   
    }
  }
}
</script>

<style lang="scss" scoped>
// .card-login {
//   margin: auto;
//   width: 60%;
// }

.form-wrap {
  width: 60%;
  margin: auto;
}

.btn {
  margin:auto;
  color: rgb(60, 173, 173); 
}
</style>
