<template>
  <v-row class="fill-height">
      <v-col>
        <v-sheet height="64">
          <v-toolbar
            flat
          >
            <v-btn
              color="#198F8F"
              class="mr-4"
              @click="dialog = true ; selectMissionForm()"
            >
              Nouvelle tâche
            </v-btn>
            <v-btn
              outlined
              class="mr-4 hidden-sm-and-down"
              color="grey darken-2"
              @click="setToday"
              
            >
              Today
            </v-btn>
            <v-btn
              fab
              text
              small
              color="grey darken-2"
              @click="prev"
            >
              <v-icon small>
                mdi-chevron-left
              </v-icon>
            </v-btn>
            <v-btn
              fab
              text
              small
              color="grey darken-2"
              @click="next"
            >
              <v-icon small>
                mdi-chevron-right
              </v-icon>
            </v-btn>
            <v-toolbar-title v-if="$refs.calendar" class="hidden-sm-and-down">
              {{ $refs.calendar.title }}
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-menu
              bottom
              right
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  outlined
                  color="grey darken-2"
                  v-bind="attrs"
                  v-on="on"
                  class="hidden-sm-and-down"
                >
                  <span>{{ typeToLabel[type] }}</span>
                  <v-icon right>
                    mdi-menu-down
                  </v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item @click="type = 'day'">
                  <v-list-item-title>Day</v-list-item-title>
                </v-list-item>
                <v-list-item @click="type = 'week'">
                  <v-list-item-title>Week</v-list-item-title>
                </v-list-item>
                <v-list-item @click="type = 'month'">
                  <v-list-item-title>Month</v-list-item-title>
                </v-list-item>
                <v-list-item @click="type = '4day'">
                  <v-list-item-title>4 days</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </v-toolbar>
        </v-sheet>
        <v-sheet height="600">
          <v-calendar
            ref="calendar"
            v-model="focus"
            color="teal"
            :events="events"
            :type="type"
            @click:event="showEvent"
            @click:more="viewDay"
            @click:date="viewDay"
            @change="updateRange"
          ></v-calendar>
          <v-menu
            v-model="selectedOpen"
            :close-on-content-click="false"
            :activator="selectedElement"
            offset-x
          >
            <v-card
              color="grey lighten-4"
              min-width="350px"
              flat
            >
              <v-toolbar
                :color="selectedEvent.color"
                dark
              >
                <v-btn @click="deleteEvent(selectedEvent.id)" icon>
                  <v-icon>mdi-delete</v-icon>
                </v-btn>
                <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
              </v-toolbar>
              <v-card-text>

                <!-- <span v-html="selectedEvent.details"></span> -->
                <v-form v-if="currentlyEditing !== selectedEvent.id">
                  {{ selectedEvent.details }}
                </v-form>
                <v-form v-else>
                  <v-textarea
                    v-model="selectedEvent.details"
                    type="text" 
                    placeholder="ajouter détails">
                  </v-textarea>
                </v-form>

              </v-card-text>
              <v-card-actions>
                <v-btn
                  text
                  @click="selectedOpen = false"
                >
                  Fermer
                </v-btn>
                <v-btn
                  text
                  v-if="currentlyEditing !== selectedEvent.id"
                  @click.prevent="editEvent(selectedEvent)"
                >
                  Modifier
                </v-btn>
                <v-btn
                  text
                  v-else
                  @click.prevent="updateEvent(selectedEvent)"
                >
                  Enregistrer
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-menu>
        </v-sheet>
        <!-- Add event dialog -->
        <div class="text-center">
          <v-dialog
            v-model="dialog"
            max-width="500"
          >
            <v-card>
              <v-container>
              <v-form @submit.prevent="addEvent">
                <v-text-field
                  label="Nom"
                  type="text"
                  color="teal"
                  v-model="name"
                  required
                  :rules="[v => !!v || 'Item is required']"
                  :counter="100"
                />
                <v-text-field
                  label="Détails"
                  type="text"
                  color="teal"
                  v-model="details"
                />
                <v-text-field
                  label="Début"
                  type="date"
                  color="teal"
                  v-model="start"
                  required
                  :rules="[v => !!v || 'Item is required']"
                />
                <v-text-field
                  label="Fin"
                  type="date"
                  color="teal"
                  v-model="end"
                  required
                  :rules="[v => !!v || 'Item is required']"
                />
                <!-- <v-text-field
                  label="Mission"
                  type="text"
                  color="teal"
                  v-model="mission"
                /> -->
                <v-select
                  :items="selectMission"
                  label="Mission"
                  v-model="mission"
                  dense
                ></v-select>
                <v-text-field
                  label="Couleur"
                  type="color"
                  color="teal"
                  v-model="color"
                />
              </v-form>
              <v-btn 
                color="teal"
                text
                outlined
                class="mx-4"
                @click.stop="dialog=false"
                @click="addEvent"
              >
                Créer
              </v-btn>
              <v-btn 
                text
                color="teal"
                outlined
                class="mx-4"
                @click.stop="dialog=false"
              >
                Annuler
              </v-btn>
              </v-container>
             </v-card>
          </v-dialog>
        </div>
  


      </v-col>
    </v-row>
</template>

<script>
import {mapState} from 'vuex'
import { getAPI } from '../axios-api'

export default {
  name: 'Calendar',
  components: {
  },

  data: () => ({
    focus: '',
    type: 'month',
    typeToLabel: {
      month: 'Month',
      week: 'Week',
      day: 'Day',
      '4day': '4 Days',
    },
    selectedEvent: {},
    selectedElement: null,
    selectedOpen: false,
    // colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
    // names: ['Meeting', 'Holiday', 'PTO', 'Travel', 'Event', 'Birthday', 'Conference', 'Party'],
    
    name: null,
    details: "",
    start: null,
    end: null,
    mission: null,
    color: "",
    currentlyEditing: null,
    events: [],
    dialog: false,
    selectMission: [],
  }),


  async mounted () {
    this.$refs.calendar.checkChange()
    this.getEvents();
  },

  computed:{
    ...mapState([
      'scheduleUserserDetails', 'userDetails'
    ]),
  },

  methods: {
    selectMissionForm(){
      this.userDetails.missions.forEach(mission => {
      let miss = mission.name;
      this.selectMission.push(miss)
      })
    },

    async getEvents(){
      let events= [];
      await this.$store.dispatch('getScheduleUser')
      .then(() =>
        this.$store.state.scheduleUserDetails.forEach(task => {
          let dataTask = task;
          events.push(dataTask);
      }))
      this.events = events;
    },
    async addEvent(){
      if(this.name && this.start && this.end){
        console.log('ooooo', this.color)
        await getAPI.post(`/api/schedules/`, {
          name: this.name ,
          details: this.details,
          start: this.start,
          end: this.end,
          mission: this.mission,
          color: this.color
        }, {
        headers: { 'Authorization': 'Token ' + this.$store.state.token,}
        });
        this.getEvents();
        this.name = "";
        this.details = "";
        this.start = "";
        this.end = "";
        this.mission = "";
        this.color = "";
      } else {
        alert('Name, start and date are required');
      }
    },
    async updateEvent(ev){
      await getAPI.patch(`/api/schedules/${ev.id}/`, {
        details: ev.details
      }, {
        headers: { 'Authorization': 'Token ' + this.$store.state.token,}
      })
      this.selectedOpen = false;
      this.currentlyEditing = null;
    },
    async deleteEvent(ev){
      console.log('chou', ev)
      await getAPI.delete(`/api/schedules/${ev}/`, {
        headers: { 'Authorization': 'Token ' + this.$store.state.token,}
      })
      this.selectedOpen = false;
      this.getEvents();
    },
    viewDay ({ date }) {
      this.focus = date
      this.type = 'day'
    },
    getEventColor (event) {
      return event.color
    },
    setToday () {
      this.focus = ''
    },
    prev () {
      this.$refs.calendar.prev()
    },
    next () {
      this.$refs.calendar.next()
    },
    editEvent(ev) {
      this.currentlyEditing = ev.id;
    },
    showEvent ({ nativeEvent, event }) {
      const open = () => {
        this.selectedEvent = event
        this.selectedElement = nativeEvent.target
        setTimeout(() => {
          this.selectedOpen = true
        }, 10)
      }

      if (this.selectedOpen) {
        this.selectedOpen = false
        setTimeout(open, 10)
      } else {
        open()
      }

      nativeEvent.stopPropagation()
    },
    updateRange ({ start, end }) {
      const events = []

      const min = new Date(`${start.date}T00:00:00`)
      const max = new Date(`${end.date}T23:59:59`)
      const days = (max.getTime() - min.getTime()) / 86400000
      const eventCount = this.rnd(days, days + 20)

      for (let i = 0; i < eventCount; i++) {
        const allDay = this.rnd(0, 3) === 0
        const firstTimestamp = this.rnd(min.getTime(), max.getTime())
        const first = new Date(firstTimestamp - (firstTimestamp % 900000))
        const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000
        const second = new Date(first.getTime() + secondTimestamp)

        events.push({
          name: this.names[this.rnd(0, this.names.length - 1)],
          start: first,
          end: second,
          color: this.colors[this.rnd(0, this.colors.length - 1)],
          timed: !allDay,
        })
      }

      this.events = events
    },
    rnd (a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a
    },
  },
 
}
</script>

<style lang="scss" scoped>

</style>
