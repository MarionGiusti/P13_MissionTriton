<template>
  <v-container>
    <div class="mx-8">
      <v-card
        class="mx-auto post-wrap"
        flat
      >
        <v-img
          class="white--text align-end"
          height="200px"
          src= "../assets/compass.jpg"
        >
          <v-card-title class="black--text card-title"><v-spacer></v-spacer>
            <div>
              <h4>Navire : {{ missionD.ship_name }} <br/>
              Du {{ missionD.start_date }} au {{ missionD.end_date }}</h4>
            </div>
          </v-card-title>
        </v-img>
        
        <v-card-text class="post-wrap">
          <v-row>
            <v-col>
              <div class="text-end">
                <v-btn
                  class="mb-4" 
                  icon
                  outlined
                  color="#54658C"
                  @click="dialog=true"
                  v-if="verifMember == true"
                >
                  <v-icon>
                    mdi-grease-pencil
                  </v-icon>
                </v-btn>
              </div>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
          {{ missionD.description }}
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>

    <!-- dialog -->
      <div class="text-center">
        <v-dialog
          v-model="dialog"
          max-width="800"
        >
          <v-card>
            <v-container>            
              <v-form 
                ref="form"
                v-model="valid"
                lazy-validation
                @submit.prevent="updateMission"
              >
                <v-text-field
                  label="Nom de la mission"
                  prepend-icon="mdi-radiobox-marked"
                  type="text"
                  color="teal"
                  v-model="missionD.name"
                  required
                  :rules="[v => !!v || 'Item is required']"
                />
                <v-text-field
                  label="Nom du navire"
                  prepend-icon="mdi-duck"
                  type="text"
                  color="teal"
                  v-model="missionD.ship_name"
                  required
                  :rules="[v => !!v || 'Item is required']"
                />
                <v-menu
                  v-model="menu1"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="missionD.start_date"
                      label="Date de début"
                      prepend-icon="mdi-clock-start"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      required
                      :rules="[v => !!v || 'Item is required']"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                    v-model="missionD.start_date"
                    @input="menu1 = false"
                  ></v-date-picker>
                </v-menu>
                <v-menu
                  v-model="menu2"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="missionD.end_date"
                      label="Date de fin"
                      prepend-icon="mdi-clock-end"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      required
                      :rules="dateRules"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                    v-model="missionD.end_date"
                    @input="menu2 = false"
                  ></v-date-picker>
                </v-menu>
                <v-textarea
                  label="Decription"
                  type="text"
                  color="teal"
                  required
                  v-model="missionD.description"
                ></v-textarea>
              </v-form>
              <v-btn 
                text
                @click.stop="dialog=false"
                @click="updateMission(missionD)"
                :disabled="!valid"
                color="teal"
              >
                Modifier
              </v-btn>
              <v-btn
                text
                @click.stop="dialog = false"
                color="teal"
              >
                Fermer
              </v-btn>
            </v-container>
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
    name: 'MissionGoals',
    data() {
      return {
        dateRules: [
          v => !!v ,
          v => (v && v > this.missionD.start_date) || 'Date de fin avant date début',
        ],
        dialog: false,
        menu1: false,
        menu2: false,
        valid: false,
      }
    },
    
    computed: {
      ...mapGetters([ 'currentMission' ]),
      missionD() {
        return this.currentMission(this.$route.params.id)
      },
      ...mapGetters([ 'memberMission']),
      verifMember() {
        return this.memberMission(this.$route.params.id)
      } 
    },

    methods:{
      async updateMission(missioncredentials) {
        console.log('UPDATE MISSION', missioncredentials)
        await getAPI.patch(`api/missions/${missioncredentials.id}/`, {         
            name: missioncredentials.name,
            ship_name: missioncredentials.ship,
            start_date: missioncredentials.start_date,
            end_date: missioncredentials.end_date,
            description: missioncredentials.description,
        }, {
        headers: { 'Authorization': 'Token ' + this.$store.state.token }})
      },
    }
  }

</script>

<style lang="scss" scoped>
  .post-wrap {
    background-color:#A3B3D5;
  }
</style>