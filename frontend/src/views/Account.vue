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
                    icon
                    fab
                    outlined
                    @click="$refs.inputUpload.click()"    
                  >
                    <v-icon
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
                <v-img :src= userDetails.profile_image >
                  <v-fade-transition>
                    <v-overlay
                      v-if="hover"
                      absolute
                      color="#8c9297"
                    >
                      <v-btn
                        icon
                        fab
                        outlined
                        @click="$refs.inputUpload.click()"
                      >
                        <v-icon
                        >
                        mdi-camera
                        </v-icon>
                      </v-btn>
                      <input type="file" v-show="false" ref="inputUpload" @change="onFileSelected($event, 0)">
                    </v-overlay>
                  </v-fade-transition>
                </v-img>
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
                    :value="userDetails.first_name"
                  />
                  <v-text-field
                    label="Nom"
                    prepend-icon="mdi-account"
                    type="text"
                    color="teal"
                    v-model="userDetails.last_name"
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
                    :value="userDetails.linkedin_link"
                  />
                  <v-text-field
                    label="Profil Researchgate"
                    prepend-icon="mdi-cat"
                    type="email"
                    color="teal"
                    v-model="userDetails.researchgate_link"
                    :value="userDetails.researchgate_link"
                  />

                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-btn
                  class="btn"
                  :disabled="!valid"
                  outlined
                  @click="patchUser(userDetails)"
                >
                  Modifier
                </v-btn>
                <v-btn
                  class="btn"
                  :disabled="!valid"
                  outlined
                  @click="deleteUser(userDetails.id)"
                >
                  Supprimer
                </v-btn>
              </v-card-actions>
            </v-card>
          </div>
        </div>
      </div>
      <div class="d-flex flex-row" v-if="userDetails.missions && userDetails.missions.length != 0">
        <div class="d-flex flex-column row-wrap-mission">
          <div class="mb-4">
            <h2 class="text-center">Missions </h2>
            <v-divider/>
          </div>
          
          <div class="d-flex flex-row flex-wrap justify-space-between" >
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
                      :counter="150"
                    />
                    <v-text-field
                      label="Laboratoire"
                      type="text"
                      color="teal"
                      v-model="missionUserDetails.team_lab"
                      :value="missionUserDetails.team_lab"
                      :counter="200"

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
                  <v-btn 
                    class="btn"
                    :disabled="!valid"
                    outlined 
                    @click="patchMissionUser(missionUserDetails)"
                  >
                    Modifier
                  </v-btn>
                  <v-btn 
                    class="btn"
                    :disabled="!valid"
                    outlined
                    @click="deleteMissionUser(missionUserDetails.id)"
                  >
                    Supprimer
                  </v-btn>
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

// import { mapFields } from 'vuex-map-fields'
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
    this.initialise()
  },
  
  computed: {
    // ...mapFields([
    //   'userDetails',
    //   'missionUserDetails'
    // ]),
    ...mapState([
      'userDetails',
      'missionUserDetails'
    ]),
    userpic() {
      return this.$store.state.userDetails.profile_image;
    }
  },

  methods: {
    initialise(){
      this.$store.dispatch('getUserDetails');
    },

    showSelectedMission(missionItem) {
      this.missionId = missionItem;
      this.card_mission = true;
      this.getMissionUserDetails(this.missionId);
    },

    onFileSelected(event, photo) {
      this.selectedFile = event.target.files[0];
      if (photo == 0) {
        this.onUpload();
      } else {
        this.onUploadBackground();
      }
    },
    onUpload() {
      const fd = new FormData();
      fd.append('file', this.selectedFile, this.selectedFile.name);
      try {
        getAPI.post('/api/users/profile_picture/', fd, {
          headers: { 
            'Authorization': 'Token ' + this.$store.state.token,
            'Content-Type': 'multipart/form-data',   
          }
        });
        this.$store.dispatch('getUserDetails');
      } catch(err) {
          console.log(`erreur: ${err}`)
      }
    },
    onUploadBackground() {
      const fd = new FormData();
      fd.append('file', this.selectedFile, this.selectedFile.name)
      try {
        getAPI.post('/api/users/background_picture/', fd, {
          headers: { 
            'Authorization': 'Token ' + this.$store.state.token,
            'Content-Type': 'multipart/form-data',   
          }
        });
        this.$store.dispatch('getUserDetails');
      } catch(err) {
          console.log(`erreur: ${err}`)
      }
    },

    ...mapActions(['patchUserProfile']),
    async patchUser({username, first_name, last_name, email, linkedin_link, researchgate_link}) {
      if (this.$refs.formUser.validate()) {
        try {
          await this.patchUserProfile({ username, first_name, last_name, email, linkedin_link, researchgate_link });
        } catch(err) {
          console.log(`erreur: ${err}`)
        }
      }
    },
    ...mapActions(['patchMissionUserProfile']),
    async patchMissionUser({job, team_lab, description}) {
      if (this.$refs.formMission.validate()) {
        try {
          await this.patchMissionUserProfile({job, team_lab, description});
        } catch(err) {
          console.log(`erreur: ${err}`)
        }
      } 
    },

    ...mapActions(['getListMissionUsers']),
    async getMissionUserDetails(missionId){
      await this.getListMissionUsers(missionId);
    },

    async deleteMissionUser(id){
      await getAPI.delete(`/api/users/missionusers/${id}/`, {
        headers: { 'Authorization': 'Token ' + this.$store.state.token,}
      });
      this.card_mission = false;
      this.initialise();
    },

    async deleteUser(id){
      this.$router.push('/');
      this.logout();
      await getAPI.delete(`/api/users/${id}/`, {
        headers: { 'Authorization': 'Token ' + this.$store.state.token,}
      });
    },

    async logout () {
      try {
        await this.$store.dispatch('userLogout');
      } catch(err) {
      console.log(`erreur: ${err}`) 
      }
    },
  }
};
</script>

<style lang="scss" scoped>
  .background-wrap {
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

  @media all and (max-width: 960px) {
    .row-wrap-profile {
      width: 90%;
    }
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

  @media all and (max-width: 960px) {
    .card-mission-details {
      margin: auto;
      width: 300px;
    }
  }

  .form-login {
    width: 85%;
    margin: auto;
  }
</style>
