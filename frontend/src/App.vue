<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-toolbar-title>Mission Triton</v-toolbar-title>
      </div>

      <v-spacer></v-spacer>

      <v-btn text>Login</v-btn>
    </v-app-bar>

    <v-main>
        <v-form ref="form" v-model="valid">
            <v-text-field
             label="Username"
             prepend-icon="mdi-account-circle"
             type="text"
             v-model="form.username"
             required
             :rules="[v => !!v || 'Item is required']"
            />
            <v-text-field
             label="Password"
             prepend-icon="mdi-lock"
             type="password"
             v-model="form.password"
            />
        </v-form>
        <v-btn :disabled="!valid" color="info" @click="login(form)">Login</v-btn>
        HELLO
        <router-view/>

    </v-main>
  </v-app>
</template>

<script>
// import { mapActions } from 'vuex'

export default {
  name: 'App',

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
    async login ({username, password}) {
      console.log(this.valid)
      if (this.$refs.form.validate()) {
        console.log(this.valid)
        // await mapActions(['userLogin'])
        await this.$store
          .dispatch('userLogin', { username, password })
          .then(() => console.log('login ok'))
          .catch(err => {
            console.log(err)
          });
      }   
    }
  }
};
</script>
