<template>
  <v-main>
    <div class="d-flex flex-column ">
      <v-hover>
          <template v-slot:default="{ hover }">
      <div class="top-back">
        
            <v-img
              height="300px"
              :src= userDetails.profile_background_image>
              <v-fade-transition>
                  <v-overlay
                    v-if="hover"
                    absolute
                    color="#8c9297"
                  >
                    <v-btn
                    :color="transparent"
                      icon
                      fab
                      outlined
                      @click="$refs.inputUpload.click()"    
                    >
                      <v-icon
                      :color="transparent"
                      >
                      mdi-camera
                      </v-icon>
                    </v-btn>
                    <input type="file" v-show="false" ref="inputUpload" @change="onFileSelected($event, 1)">
                  </v-overlay>
                </v-fade-transition>
            </v-img>
            
            
      </div>
      </template>
        </v-hover>
      <div class="bottom-back">
        <v-hover>
          <template v-slot:default="{ hover }">
            <v-sheet
              color="white"
              elevation="12"
              height="100"
              width="100"
            >
              <v-avatar
                color="grey"
                size="230"
                tile
                :class="{ 'on-hover': hover }"
              >
                <v-img :src= userDetails.profile_image ></v-img>
                <v-fade-transition>
                  <v-overlay
                    v-if="hover"
                    absolute
                    color="#8c9297"
                  >
                    <v-btn
                    :color="transparent"
                      icon
                      fab
                      outlined
                      @click="$refs.inputUpload.click()"
                    >
                      <v-icon
                      :color="transparent"
                      >
                      mdi-camera
                      </v-icon>
                    </v-btn>
                    <input type="file" v-show="false" ref="inputUpload" @change="onFileSelected($event, 0)">
                  </v-overlay>
                </v-fade-transition>
              </v-avatar>
            </v-sheet>
          </template>
        </v-hover>
      </div>
    </div>

    <v-container class="d-flex flex-column background-wrap" fluid>
      <div class="d-flex flex-row-reverse">
        <div class="d-flex flex-column row-wrap-profile">
          <div class="mb-4">
            <h2 class="text-center">Profil</h2>
            <v-divider/>
          </div>
          <div class="">
            <!-- <v-card class="card-user" color="#B75724"> -->
            <v-card class="card-user" color="#2AC9B2">
              <v-card-text>
                <v-form class="form-login" ref="formUser" v-model="valid">
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
                <v-btn class="btn" :disabled="!valid" outlined @click="patchUser(userDetails)">Modifier</v-btn>
              </v-card-actions>
            </v-card>
          </div>
        </div>
      </div>
      <div class="d-flex flex-row">
        <div class="d-flex flex-column row-wrap-mission">
          <div class="mb-4">
            <h2 class="text-center">Missions</h2>
            <v-divider/>
          </div>
          
          <div class="d-flex flex-row justify-space-between">
            <div class="">
              <v-card class="card-mission" color="#2AC9B2">
                <v-card-text>

                  <v-list-item-group
                    color="#002D26"
                  >
                    <v-list-item
                      v-for="(mission, i) in userDetails.missions"
                      :key="i" @click="showSelectedMission(mission.id)"
                    >
                      <v-list-item-content>
                        <v-list-item-title v-text="mission.name"></v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-item-group>
                  
                </v-card-text>
              </v-card>
            </div>
            <div class="" v-if="card_mission">
              <v-card class="card-mission-details" color="#8AEEDF">
                <v-card-text>

                  <v-form class="form-login" ref="formMission" v-model="valid">
                  <v-text-field
                    label= "Job"
                    type="text"
                    color="teal"
                    v-model="missionUserDetails.job"
                    :value="missionUserDetails.job"
                  />
                  <v-text-field
                    label="Laboratoire"
                    type="text"
                    color="teal"
                    v-model="missionUserDetails.team_lab"
                    :value="missionUserDetails.team_lab"
                  />
                  <v-textarea
                    label="Description"
                    type="text"
                    color="teal"
                    v-model="missionUserDetails.description"
                    :value="missionUserDetails.description"
                  ></v-textarea>

                </v-form>
                  
                </v-card-text>
                <v-card-actions>
                <v-btn class="btn" :disabled="!valid" outlined  @click="patchMissionUser(missionUserDetails)">Modifier</v-btn>
                </v-card-actions>
              </v-card>
            </div>
          </div>


        </div>
      </div>
    </v-container>
  </v-main>
</template>

<script>
import {mapState} from 'vuex'
import { mapActions } from 'vuex'

import { mapFields } from 'vuex-map-fields'
import { getAPI } from '../axios-api'

export default {
  name: 'Account',
  components: {
  },
  data() {
    return {
      overlay: false,
      valid: false,
      selectedFile: null,
      card_mission: false,
      missionId: "",
    }
  },
  
  mounted() {
    this.$store
      .dispatch('loadUserDetails')
      .catch(err => {console.log(err)});
  },
  
  computed: {
    ...mapFields([
      'userDetails',
      'missionUserDetails'
    ]),
    ...mapState([
      'userDetails',
      'missionUserDetails'
    ]),
    userpic() {
      return this.$store.state.userDetails.profile_image
    }
  },

  methods: {
    showSelectedMission(missionItem) {
      this.missionId = missionItem
      this.card_mission = true
      console.log("yooo", this.card_mission, this.missionId)
      this.getMissionUserDetails(this.missionId)
      console.log("yuu token", this.$store.state.token)
    },

    onFileSelected(event, photo) {
      this.selectedFile = event.target.files[0]
      if (photo == 0) {
        this.onUpload()
      } else {
        this.onUploadBackground()
  }
    },
    onUpload() {
      const fd = new FormData();
      fd.append('file', this.selectedFile, this.selectedFile.name)
      getAPI.post('/api/users/profile_picture/', 
      fd, {
      headers: { 
        'Authorization': 'Token ' + this.$store.state.token,
        'Content-Type': 'multipart/form-data',   
      }
      })
      .then(() => console.log('patch image ok', fd))
      .then(() => this.$store.dispatch('loadUserDetails'))
      .catch(err => {console.log(err)});
    },
    onUploadBackground() {
      const fd = new FormData();
      fd.append('file', this.selectedFile, this.selectedFile.name)
      getAPI.post('/api/users/background_picture/', 
      fd, {
      headers: { 
        'Authorization': 'Token ' + this.$store.state.token,
        'Content-Type': 'multipart/form-data',   
      }
      })
      .then(() => console.log('patch background image ok', fd))
      .then(() => this.$store.dispatch('loadUserDetails'))
      .catch(err => {console.log(err)});
    },

    

    ...mapActions(['patchUserProfile']),
    async patchUser({username, first_name, last_name, email, linkedin_link, researchgate_link}) {
      console.log(this.valid)
      if (this.$refs.formUser.validate()) {
        console.log(this.valid)
        await this.patchUserProfile({ username, first_name, last_name, email, linkedin_link, researchgate_link })
          .then(() => console.log('method patch user ok'))
          .catch(err => {console.log(err)});
      }
    },
    ...mapActions(['patchMissionUserProfile']),
    async patchMissionUser({job, team_lab, description}) {
      console.log(this.valid)
      if (this.$refs.formMission.validate()) {
        console.log(this.valid)
        await this.patchMissionUserProfile({job, team_lab, description})
          .then(() => console.log('method patch mission user ok'))
          .catch(err => {console.log(err)});
      }
    },

    ...mapActions(['get_listmissionusers']),
    async getMissionUserDetails(missionId){
      await this.get_listmissionusers(missionId)
        .then(() => console.log('get list ok'))      
        .catch(err => {console.log(err)});
    },

    // getMissionUserDetails() {
    //   const{data} = getAPI.get('/api/users/missionusers/?missionid=1',
    //   // getAPI.get(`/api/users/missionusers/?missionid={$this.missionId}`,
    //   // const {data} = getAPI.get('/api/users/missionusers/',
    //     // { params: { missionid: this.missionId, userid: this.userDetails.id },
    //     {headers: { 'Authorization': 'Token ' + this.$store.state.token }})
    //     .then(() => console.log('dataaa', data))     
    //   .then(() => console.log('get missionuser ok', data))
    //   .catch(err => {console.log(err)});
    // },   
  }
};

</script>

<style lang="scss" scoped>
.background-wrap {
  // background-color: #D0D0A3;#54658C#B6885D#EBA165#F2BDA0#FCA678
  background-color:#03584B;
  width: 95%;
}

.bottom-back {
  margin-top: -60px;
  margin-left: 60px;
}

.row-wrap-profile {
  width: 60%;
}

.card-user {
  margin: auto;
  width: 90%;
}

.row-wrap-mission {
  width: 80%;
}

.card-mission {
  margin: auto;
  margin-left: 10%;
  width: 100%;
}

.card-mission-details {
  margin: auto;
  width: 700px;
}

.form-login {
  width: 85%;
  margin: auto;
}

</style>
