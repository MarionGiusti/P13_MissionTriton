<template>
  <v-container>
    <!-- <h2 class="text-center">Notre équipe scientifique</h2>
    <v-divider/> -->
    <div class="mx-8">

      <v-btn
        color="#198F8F"
        @click="dialog = true "
        class="mb-4"
      >
        Nouveau participant
      </v-btn>
      <v-row align="center" >
        <!-- <v-col v-for="item in proitems" :key="item.id" cols="4" align="center"> -->
        <v-col v-for="member in team" :key="member.id" cols="12" md="4" align="center">
          <v-card
            class="mx-auto"
            flat
            color="#54658C"
          > 
          <v-hover>
          <template v-slot:default="{ hover }">

          <!-- <v-avatar
            tile
            size="250"
            color="#A3D0CA"
            :class="{ 'on-hover': hover } "
            class="mt-4"
          > -->
            <v-img
              width="250px"
              height="250px"
              :src="`http://127.0.0.1:8000/media/${member.picture}`" 
              :class="{ 'on-hover': hover } "
              class="mt-4"
            >
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
                    @click="deleteMember(member.missionuser_id)"
                  >
                    <v-icon>
                      mdi-delete
                    </v-icon>
                  </v-btn>
                <!-- <a :href=item.linkedin target="_blank" v-if="item.linkedin!==null">
                  <v-avatar class="mx-2">
                    <img
                      src="../assets/in.png"
                    >
                  </v-avatar>
                </a>
                <a :href=item.researchgate target="_blank" v-if="item.researchgate!==null">
                  <v-avatar class="mx-2">
                    <img
                      src="../assets/index.png"
                    >
                  </v-avatar>
                </a> -->
                </v-overlay>
              </v-fade-transition>
            </v-img>
          <!-- </v-avatar> -->
          </template>
          </v-hover>

            <v-card-subtitle class="pb-0 text-center">
              {{ member.first_name }} {{ member.last_name }}
              <br/>
              {{ member.job }} {{ member.team_lab }}
            </v-card-subtitle>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                icon
                @click="show = !show"
              >
                <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
              </v-btn>
            </v-card-actions>

            <v-expand-transition>
              <div v-show="show">
                <v-divider></v-divider>

                <v-card-text>
                  email: {{ member.email }}
                  <br/>
                  rôle: {{ member.description }}
                  <div>
                    <a :href=member.linkedin target="_blank" v-if="member.linkedin!==null">
                      <v-avatar class="mx-2">
                        <img src="../assets/logo_linkedin.png">
                      </v-avatar>
                    </a>
                    <a :href=member.researchgate target="_blank" v-if="member.researchgate!==null">
                      <v-avatar class="mx-2">
                        <img src="../assets/logo_rg.png">
                      </v-avatar>
                    </a>
                  </div>
                </v-card-text>
              </div>
            </v-expand-transition>
          </v-card>
        </v-col>
      </v-row>

      <!-- Add member dialog -->
      <div class="text-center">
        <v-dialog
          v-model="dialog"
          max-width="500"
        >
          <v-card>
            <div class="form-wrap" align="center" justify="center">
              <v-form 
                ref="form"
                v-model="valid"
                lazy-validation
                >
                  <v-text-field
                    label="Email du participant"
                    prepend-icon="mdi-email"
                    type="email"
                    color="teal"
                    v-model="form.email"
                    :value="form.email"
                    required
                    :rules="[v => !!v || 'Item is required']"
                  />
              </v-form>
              <v-btn 
                :disabled="!valid"
                type="submit"
                color="teal"
                class="mb-4"
                @click.stop="addMissionuser(form); dialog=false"
                text
              >Ajouter</v-btn>
            </div>
          </v-card>
        </v-dialog>
      </div>
    </div>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
import { getAPI } from '../axios-api'

  export default {
    name: 'Team',
    data() {
      return {
        team: {},
        show: false,
        dialog: false,
        valid: true,
        form: {
          missionId: this.$route.params.id,
          email:"",
        },
      }
    },

    computed: {
      ...mapGetters([ 'currentMission' ]),
      missionD() {
        return this.currentMission(this.$route.params.id)
      },
    },

    mounted(){
      this.load_team()
    },

    methods:{
      async load_team(){
        let miss = this.$route.params.id
        const data = await getAPI.get(`/api/users/missionusers/get_team/?missionId=${miss}`, 
          {
          headers: { 
            'Authorization': 'Token ' + this.$store.state.token,
          }
        })
        this.team = data.data
        console.log('load_team', this.team)

      },

      async addMissionuser() {
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
          this.load_team()
          alert( `L'utilisateur ${this.form.email} a bien été ajouté à la mission ${this.missionD.name} !` )
          this.resetForm()
          .catch(err => {console.log(err)}); 
        }
      },
      resetForm() {
        this.$refs.form.reset()
      },

      async deleteMember(id){
        console.log('DELETE', id)
      await getAPI.delete(`/api/users/missionusers/${id}/`, {
        headers: { 'Authorization': 'Token ' + this.$store.state.token,}
      })
      
      await this.load_team()
    },
      
      
    },
    
  }

</script>

<style lang="scss" scoped>

</style>