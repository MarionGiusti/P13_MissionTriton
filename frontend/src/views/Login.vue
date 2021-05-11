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
            :type="show ? 'text' : 'password'"
            color="teal"
            v-model="form.password"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="show = !show"
          />
        </v-form>
        <v-btn 
          class="btn mx-4"
          :disabled="!valid"
          outlined @click="login(form)"
        >
          Se connecter
        </v-btn>
        <v-btn
          class="btn  mx-4"
          outlined to="/register"
        >
          Nous rejoindre
        </v-btn>
      </div>
    </v-container>
  </v-main>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  components: {
  },

  data () {
    return {
      form: {
        username:"",
        password:""
      },
      show: false,
      valid: false,
    }
  },

  methods: {
    ...mapActions(['userLogin']),
    async login ({username, password}) {
      if (this.$refs.form.validate()) {
        try {
          await this.userLogin({ username, password })
          this.$router.push('/')
          this.$store.dispatch('getUserDetails')
        } catch(err) {
            console.log(`erreur: ${err}`)
        }
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
