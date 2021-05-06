<template>
  <v-main>
    <v-container>
      <div class="form-wrap" align="center" justify="center">
        <v-form 
        class="form-login"
        ref="form"
        v-model="valid"
        lazy-validation
        >
            <v-text-field
              label="Username"
              prepend-icon="mdi-account-circle"
              type="text"
              color="teal"
              v-model="form.username"
              required
              :rules="[v => !!v || 'Item is required']"
            />
            <v-text-field
              label="Password"
              prepend-icon="mdi-lock"
              type="password"
              color="teal"
              v-model="form.password"
            />
        </v-form>
        <v-btn class="btn mx-4" :disabled="!valid" outlined @click="login(form)">Se connecter</v-btn>
        <v-btn class="btn  mx-4" outlined to="/register">Nous rejoindre</v-btn>
              <!-- <v-btn 
                  :disabled="!valid" 
                  outlined
                  @click="login(form)"
                >Se connecter</v-btn>

                <v-btn  
                  outlined
                  text
                >Nous rejoindre</v-btn> -->
<!-- 
<v-btn
        color="orange"
        text
      >
        Share
      </v-btn>

      <v-btn
        color="orange"
        text
      >
        Explore
      </v-btn> -->
      </div>
    </v-container>
  </v-main>

<!-- <v-main>
  <v-container class="fill-height login-wrap" fluid>
    <v-row class="row-wrap" align="center" justify="center">
      <v-col>
        <v-card class="card-login " color="blue lighten-4">
          <v-card-text>
            <v-form class="form-login" ref="form" v-model="valid">
                <v-text-field
                  label="Username"
                  prepend-icon="mdi-account-circle"
                  type="text"
                  color="teal"
                  v-model="form.username"
                  required
                  :rules="[v => !!v || 'Item is required']"
                />
                <v-text-field
                  label="Password"
                  prepend-icon="mdi-lock"
                  type="password"
                  color="teal"
                  v-model="form.password"
                />
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn class="btn" :disabled="!valid" outlined @click="login(form)">Se connecter</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</v-main> -->
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  components: {
  },

  data () {
    return {
        valid: false,
        form: {
          username:"",
          password:""
        }
    }
  },

  methods: {
    ...mapActions(['userLogin']),
    async login ({username, password}) {
      console.log(this.valid)
      if (this.$refs.form.validate()) {
        console.log(this.valid)
        await this.userLogin({ username, password })
          .then(() => console.log('login ok'))      
          .then(() => this.$router.push('/'))
          .then(() => this.$store
            .dispatch('getUserDetails')
            .catch(err => {console.log(err)}))
          .catch(err => {console.log(err)})
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
  color: rgb(60, 173, 173); 
}
</style>
