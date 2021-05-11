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
              label="Nom d'utilisateur"
              prepend-icon="mdi-account-circle"
              type="text"
              color="teal"
              v-model="form.username"
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
              :type="show ? 'text' : 'password'"
              color="teal"
              v-model="form.password1"
              :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
              required
              :rules="[v => !!v || 'Item is required',
                v => v.length >= 8 || '8 charactères minimum']"
              @click:append="show = !show"
            />

            <v-text-field
              label="Confirmer mot de passe"
              prepend-icon="mdi-lock"
              :type="show2 ? 'text' : 'password'"
              color="teal"
              v-model="form.password2"
              :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
              required
              :rules="pwdRules"
              @click:append="show2 = !show2"
            />
        </v-form>
        <v-btn class="btn" :disabled="!valid" outlined @click="register(form)">S'inscrire</v-btn>
      </div>
    </v-container>
  </v-main>
</template>

<script>
export default {
  name: 'Register',

data () {
    return {
      form: {
        username:"",
        email:"",
        password1:"",
        password2:"",
      },
      pwdRules: [
        v => !!v ,
        v => (v && v === this.form.password1) || 'Les mots de passe ne correspondent pas',
      ],
      show: false,
      show2: false,
      valid: false,
    }
  },

  methods: {
    async register ({username, password1, password2, email}) {
      if (this.$refs.form.validate()) {
        try {
          await this.$store.dispatch('userRegister', { username, password1, password2, email });
          alert( `L'utilisateur ${email} a bien été enregistré !` );
          this.$router.push('/login');
        } catch(err) {
            console.log(`erreur: ${err}`)
        }         
      }   
    }
  }
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
