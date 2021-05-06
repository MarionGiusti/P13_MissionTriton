<template>
  <v-container>
    <!-- <h2 class="text-center">Nos moments clés</h2>
    <v-divider/> -->
    <div class="mx-8">
      <v-btn
        color="#198F8F"
        @click="dialog = true "
        class="mb-4"
      >
        Nouvel évènement
      </v-btn>
      <v-timeline v-if="timelines.length !==0">
        <v-timeline-item
          v-for="(event, i) in timelines"
          :key="i"
          :color="event.color"
          fill-dot
        >
        <!-- <v-btn
                  class="mb-4" 
                  icon
                  outlined
                  color="#54658C"
                  
                >
                  
                </v-btn> -->

          <template v-slot:opposite>
            <span
              v-if="event.end_date==null"
              class="font-weight-bold`"
              v-text="
              new Date(event.start_date).toLocaleDateString('fr-FR', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
              "
            ></span>
            <span
              v-if="event.end_date!==null"
              class="font-weight-bold`"
              v-text="`Du 
              ${ 
                new Date(event.start_date).toLocaleDateString('fr-FR', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
              }
              au ${
                new Date(event.end_date).toLocaleDateString('fr-FR', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
              }`"
            ></span>
          </template>
          <div class="py-4">
            <v-btn @click="selectItem(event); dialog_update = true" text>
              <h3 class="mb-4`">
              {{event.name}}
              </h3>
            </v-btn>
            <div>
              {{event.description}}
            </div>
          </div>
        </v-timeline-item>
      </v-timeline>

      <!-- Add event timeline dialog -->
      <div class="text-center">
        <v-dialog
          v-model="dialog"
          max-width="500"
        >
          <v-card>
            <v-container>
            <v-form ref="form" v-model="valid" @submit.prevent="addTimeline">
              <v-text-field
                label="Titre"
                type="text"
                color="teal"
                v-model="send_form.form.name"
                required
                :rules="[v => !!v || 'Item is required']"
              />
              <v-textarea
                label="Détails"
                type="text"
                color="teal"
                v-model="send_form.form.description"
              ></v-textarea>
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
                    v-model="send_form.form.start_date"
                    label="Date de début"
                    prepend-icon="mdi-clock-start"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                    color="teal"
                    required
                    :rules="[v => !!v || 'Item is required']"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="send_form.form.start_date"
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
                    v-model="send_form.form.end_date"
                    label="Date de fin"
                    prepend-icon="mdi-clock-end"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                    color="teal"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="send_form.form.end_date"
                  @input="menu2 = false"
                ></v-date-picker>
              </v-menu>
              <v-text-field
                label="Couleur"
                type="color"
                color="teal"
                v-model="send_form.form.color"
              />
            </v-form>
            <v-btn
              type="submit"
              color="teal"
              :disabled="!valid"
              class="mb-4"
              text
              @click.stop="dialog=false"
              @click="addTimeline"
            >
              Créer
            </v-btn>
            </v-container>
            </v-card>
        </v-dialog>
      </div>

      <!-- Update event timeline dialog -->
      <div class="text-center">
        <v-dialog
          v-model="dialog_update"
          max-width="500"
        >
          <v-card>
            <v-container>
            <v-form ref="form" v-model="valid" @submit.prevent="updateTimeline">
              <v-text-field
                label="Titre"
                type="text"
                color="teal"
                v-model="selectedItem.name"
                required
                :rules="[v => !!v || 'Item is required']"
              />
              <v-textarea
                label="Détails"
                type="text"
                color="teal"
                v-model="selectedItem.description"
              ></v-textarea>
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
                    v-model="selectedItem.start_date"
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
                  v-model="selectedItem.start_date"
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
                    v-model="selectedItem.end_date"
                    label="Date de fin"
                    prepend-icon="mdi-clock-end"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="selectedItem.end_date"
                  @input="menu2 = false"
                ></v-date-picker>
              </v-menu>
              <v-text-field
                label="Couleur"
                type="color"
                color="teal"
                v-model="selectedItem.color"
              />
            </v-form>
            <v-btn 
              text
              @click.stop="dialog_update=false"
              @click="updateTimeline(selectedItem)"
            >
              Modifier
            </v-btn>
            <v-btn 
              text
              @click.stop="dialog_update=false"
              @click="deleteTimeline(selectedItem)"
            >
              Supprimer
            </v-btn>
            </v-container>
            </v-card>
        </v-dialog>
      </div>
    </div>
  </v-container>
</template>

<script>
// import { mapActions } from 'vuex'
import { getAPI } from '../axios-api'


  export default {
    name: 'Timeline',
    data: () => ({
      timelines:{},
      valid: false,
      dialog: false,
      dialog_update:false,
      menu1: false,
      menu2: false,
      send_form: {
        form: {
          name:"",
          description:"",
          start_date: "",
          end_date:"",
          color:"",
        },
        missionId: null,
      },
      selectedItem: {},    
    }),

  mounted() {
    // this.$store.dispatch('getTimelinesMission', this.$route.params.id)
    this.getTimelinesMission(this.$route.params.id)
  },

  methods:{
    async getTimelinesMission(missionId) {
      const data = await getAPI.get(`/api/missions/timelines/?missionid=${missionId}`)
      this.timelines = data.data
      console.log('GET TIMELINE',this.timelines)
    },

    async addTimeline(){
      this.send_form.missionId = this.$route.params.id
      console.log('FORM')
      if (this.$refs.form.validate()) {
        await getAPI.post('/api/missions/timelines/', 
          this.send_form, {
          headers: { 
            'Authorization': 'Token ' + this.$store.state.token,
            'Content-Type': 'application/json',   
          }
          })
        await this.getTimelinesMission(this.$route.params.id)
      }
    },

    async updateTimeline(selectedItem) {
        await getAPI.patch(`api/missions/timelines/${selectedItem.id}/`, {         
          name: selectedItem.name,
          description: selectedItem.description,
          start_date: selectedItem.start_date,
          end_date: selectedItem.end_date,
          color: selectedItem.color
        }, {
        headers: { 'Authorization': 'Token ' + this.$store.state.token }})
      },

    async deleteTimeline({id}){
      console.log('chou', id)
      await getAPI.delete(`/api/missions/timelines/${id}/`, {
        headers: { 'Authorization': 'Token ' + this.$store.state.token,}
      })
      
      await this.getTimelinesMission(this.$route.params.id)
    },

    selectItem(item){
      this.selectedItem = item
    },

  }

  }
</script>

<style lang="scss" scoped>

</style>