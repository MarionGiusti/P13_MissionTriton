<template>
  <v-main>
    <div class="d-flex flex-column ">
      <div class="top-back">
        <v-img
          height="300px"
          src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
        </v-img>
      </div>
      <div class="bottom-back">
        <v-sheet
          color="white"
          elevation="12"
          height="100"
          width="100"
        ><v-avatar
            class="profile"
            color="grey"
            size="230"
            tile
          >
            <v-img :src= userDetails.profile_image ></v-img>
          </v-avatar></v-sheet>
      </div>
    </div>
    <div>
      
      <input type="file" @change="onFileSelected">
      <button @click="onUpload">Upload</button>
    </div>

    <v-container class="d-flex flex-column background-wrap cyan lighten-5" fluid>
      <div class="d-flex flex-row-reverse">
        <div class="d-flex flex-column row-wrap">
          <div class="mb-4">
            <h2 class="text-center">Profil</h2>
            <v-divider/>
          </div>
          <div class="">
            <v-card class="card-login" color="blue lighten-4">
              <v-card-text>
                <v-form class="form-login" ref="form" v-model="valid">
                  <v-text-field
                    label= "Nom d'utilisateur"
                    prepend-icon="mdi-account-circle"
                    type="text"
                    color="teal"
                    v-model="userDetails.username"
                    required
                    :rules="[v => !!v || 'Item is required']"
                    :value="userDetails.username"
                  />
                  <v-text-field
                    label="Prénom"
                    prepend-icon="mdi-account"
                    type="text"
                    color="teal"
                    v-model="userDetails.first_name"
                    required
                    :rules="[v => !!v || 'Item is required']"
                    :value="userDetails.first_name"
                  />
                  <v-text-field
                    label="Nom"
                    prepend-icon="mdi-account"
                    type="text"
                    color="teal"
                    v-model="userDetails.last_name"
                    required
                    :rules="[v => !!v || 'Item is required']"
                    :value="userDetails.last_name"
                  />
                  <v-text-field
                    label="Email"
                    prepend-icon="mdi-email"
                    type="email"
                    color="teal"
                    v-model="userDetails.email"
                    required
                    :rules="[v => !!v || 'Item is required']"
                    :value="userDetails.email"
                  />
                  <v-text-field
                    label="Profil Linkedin"
                    prepend-icon="mdi-linkedin"
                    type="text"
                    color="teal"
                    v-model="userDetails.linkedin_link"
                    required
                    :rules="[v => !!v || 'Item is required']"
                    :value="userDetails.linkedin_link"
                  />
                  <v-text-field
                    label="Profil Researchgate"
                    prepend-icon="mdi-cat"
                    type="email"
                    color="teal"
                    v-model="userDetails.researchgate_link"
                    required
                    :rules="[v => !!v || 'Item is required']"
                    :value="userDetails.researchgate_link"
                  />

                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-btn class="btn" :disabled="!valid" outlined @click="patchValue(userDetails)">Modifier</v-btn>
              </v-card-actions>
            </v-card>
          </div>
        </div>
      </div>
      <div class="d-flex flex-row">
        <div class="d-flex flex-column row-wrap2">
          <div class="mb-4">
            <h2 class="text-center">Missions</h2>
            <v-divider/>
          </div>
          <div class="">
            <v-card class="card-login2" color="blue lighten-4">
              <v-card-text>
                <!-- <v-form class="form-login" ref="form" v-model="valid">
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
                </v-form> -->
              </v-card-text>
              <v-card-actions>
                <!-- <v-btn class="btn" :disabled="!valid" outlined @click="login(form)">Se connecter</v-btn> -->
              </v-card-actions>
            </v-card>
          </div>
        </div>
      </div>
        <!-- </v-col> -->
      <!-- </v-row> -->
      <!-- <div class="d-flex flex-row "> -->
        <!-- <v-card
          class="d-flex flex-row-reverse"
          max-width="800"
          outlined
        >
        </v-card> -->
      <!-- </div> -->
    </v-container>
  </v-main>

   <!-- <v-container class="fill-height" fluid>
    <v-row class="row-wrap" align="center" justify="center">
      <v-col>
    <p>profiil</p>
    <v-btn @click="account_user">User</v-btn>
    <v-btn @click="account_profile">Profile</v-btn>
      </v-col>
    </v-row>
    <v-card v-if="$store.state.profileDetails.picture!=''">
      <p> blabla </p>
      <p> {{ $store.state.profileDetails.picture }} </p>
      <v-img :src= $store.state.profileDetails.picture ></v-img>
    </v-card>
  </v-container> -->
    
    <!-- <v-btn @click="account_user">Lala</v-btn> -->
</template>

<script>
import {mapState} from 'vuex'
import { mapActions } from 'vuex'

import { mapFields } from 'vuex-map-fields'
import axios from 'axios'

export default {
  name: 'Account',
  components: {
  },
  data() {
    return {
      valid: false,
      selectedFile: null,
    }
  },
  
  mounted() {
    this.$store
      .dispatch('loadUserDetails')
      .catch(err => {
        console.log(err)
      });
  },
  
  computed: {
    ...mapFields([
       'userDetails'
    ]),
    ...mapState([
      'userDetails'
    ]),
  },

  methods: {
    
    

    onFileSelected(event) {
      console.log(event)
      this.selectedFile = event.target.files[0]
    },
    onUpload() {
      const fd = new FormData();
      fd.append('file', this.selectedFile, this.selectedFile.name)

      axios.post('http://127.0.0.1:8000/api/users/profile_picture/', 
      fd, {
      headers: { 
        'Authorization': 'Token ' + this.$store.state.token,
        'Content-Type': 'multipart/form-data',   
      }
      
      })
      .then(() => console.log('patch image ok', fd))
      .catch(err => {console.log(err)});
    },

    ...mapActions(['patchUserProfile']),
    async patchValue({username, first_name, last_name, email, linkedin_link, researchgate_link}) {
      console.log(this.valid)
      if (this.$refs.form.validate()) {
        console.log(this.valid)
        await this.patchUserProfile({ username, first_name, last_name, email, linkedin_link, researchgate_link })
          .then(() => console.log('patch ok'))
          .catch(err => {console.log(err)});
      }
    },
  }
};

</script>

<style lang="scss" scoped>
.background-wrap {
  // background-color: teal;
  width: 95%;
}

.card-wrap {
  margin-top:0;
}

.bottom-back {
  margin-top: -60px;
  margin-left: 60px;
}

.row-wrap {
  // background-color: #062546;  
  width: 60%;
  // margin-right:60px;
}

.card-login {
  margin: auto;
  width: 90%;
}

.row-wrap2 {
  // background-color: #062546;  
  width: 60%;
}

.card-login2 {
  margin: auto;
  width: 90%;
}

.form-login {
  width: 85%;
  margin: auto;
}

</style>
