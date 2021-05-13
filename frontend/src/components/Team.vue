<template>
  <v-container>
    <div class="mx-8">
      <v-btn
        color="#198F8F"
        @click="dialog = true "
        class="mb-4"
        v-if="verifMember == true"
      >
        Nouveau participant
      </v-btn>
      <v-row align="center" >
        <v-col v-for="member in team" :key="member.id" cols="12" md="4" align="center">
          <v-card
            class="mx-auto"
            flat
            color="#54658C"
          > 
            <v-img
              width="250px"
              height="250px"
              :src= static_url(member.picture)
              class="mt-4"
            >
            </v-img>
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
                  <span v-if="member.email">email: {{ member.email }}</span>
                  <br/>
                  <span v-if="member.description">rôle: {{ member.description }}</span>
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
              >
                Ajouter
              </v-btn>
              <v-btn
                text
                class="mb-4"
                @click.stop="dialog = false"
                color="teal"
              >
                Fermer
              </v-btn>
            </div>
          </v-card>
        </v-dialog>
      </div>
    </div>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
import { getAPI, baseURL } from '../axios-api'

  export default {
    name: 'Team',
    data() {
      return {
        dialog: false,
        form: {
          missionId: this.$route.params.id,
          email:"",
        },
        show: false,
        team: {},
        valid: true,
      }
    },

    computed: {
      ...mapGetters([ 'currentMission', 'memberMission' ]),
      missionD() {
        return this.currentMission(this.$route.params.id)
      },
      verifMember() {
        return this.memberMission(this.$route.params.id)
      },
      static_url() {
        return item => {
          return `${baseURL}/media/${item}`
        }
      }
    },

    mounted(){
      this.load_team()
    },

    methods:{
      async load_team(){
        let miss = this.$route.params.id;
        const data = await getAPI.get(`/api/users/missionusers/get_team/?missionId=${miss}`, 
          {
          headers: { 
            'Authorization': 'Token ' + this.$store.state.token,
          }
        });
        this.team = data.data;
      },

      async addMissionuser() {
        if (this.$refs.form.validate()) {
          try {
            await getAPI.post('/api/users/missionusers/', this.form, {
              headers: { 
                'Authorization': 'Token ' + this.$store.state.token,
                'Content-Type': 'application/json',   
              }
            })
            this.load_team();
            alert( `L'utilisateur ${this.form.email} a bien été ajouté à la mission ${this.missionD.name} !` );
            this.resetForm();
          } catch(err) {
            console.log(`erreur: ${err}`)
          }
        }
      },
      resetForm() {
        this.$refs.form.reset()
      },
      
    },
  }
</script>