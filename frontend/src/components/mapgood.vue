<template>
  <v-container>
    <v-row>
      <v-col cols="2">
        <v-form
            ref="form"
            v-model="valid"
            lazy-validation
          >
            <v-text-field
              label="Latitude"
              type="text"
              v-model="send_form.form.latitude"
              :counter="10"
              :rules="latitudeRules"
              required
            ></v-text-field>

            <v-text-field
              label="Longitude"
              type="number"
              v-model="send_form.form.longitude"
              :rules="longitudeRules"
              required
            ></v-text-field>

            <v-text-field
              v-model="send_form.form.date_time"
              label="Date"
              required
              :value="this.dateTimeExample"
            ></v-text-field>

            <v-btn
              elevation="2"
              :disabled="!valid"
              class="btn"
              outlined
              @click="AddShipPosition(send_form.form)"
              color="#09033E"
              small
            >
              Validate
            </v-btn>
          </v-form>
        </v-col>
        <v-col>
          <GmapMap v-if="mapCenter"
            :center="mapCenter"
            :zoom="3.5"
            map-type-id="satellite"
            style="width: 100%; height: 400px"
          >
            <GmapMarker
              :key="index"
              v-for="(m, index) in shippos"
              :position= "m.position"
              :clickable="true"
              :draggable="false"
              @click="center=m.position"
            />
            <gmap-polyline
              :path.sync="shippath" 
              :options="polylineOptions"
            >
            </gmap-polyline>
          </GmapMap>
          <div id="map" ref="map">
          </div>
      </v-col>
    </v-row>
    <!-- <v-row>
      <v-col>
        <h2>LALA</h2>
      </v-col>
    </v-row> -->

      <!-- <v-data-table
        :headers="headers"
        :items="desserts"
        :items-per-page="5"
        class="elevation-1"
      >
      </v-data-table> -->
  </v-container>
</template>

<script>
// import { mapGetters } from 'vuex'
import { mapState } from 'vuex'
import { getAPI } from '../axios-api'

const lineSymbol = {
    path: "M 0,-0.5 0,0.5",
    strokeOpacity: 1,
    strokeColor: "#8B1212",
    scale: 3,
  };

  export default {
    name: 'Map',
    data() {
      return {
      dateTimeExample:'2021-05-01T00:00:00Z',
      shippos: [],
      shippath: [],
        polylineOptions: {
          strokeOpacity: 0,
          icons: [{
            icon: lineSymbol,
            offset: "0",
            repeat: "10px",
          }]
        },

        valid: true,
        send_form: {
          form: {
            latitude:"",
            longitude:"",
            date_time:"",
          },
          mission: this.$route.params.id
        },
        
        latitudeRules: [
          v => !!v || 'Latitude is required',
          v => (v && v <= 90 && v>= -90) || 'Latitude comprise entre -90° et 90°',
        ],
        longitudeRules: [
          v => !!v || 'Longitude is required',
          v => (v && v <= 180 && v>= -180) || 'Latitude comprise entre -180° et 180°',
        ],
        // DateRules: [
        //   v => !!v || 'Date is required',
        //   v => /.+@.+\..+/.test(v) || 'Date must be valid',
        // ],



        headers: [
          {
            text: 'Dessert (100g serving)',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Calories', value: 'calories' },
          { text: 'Fat (g)', value: 'fat' },
          { text: 'Carbs (g)', value: 'carbs' },
          { text: 'Protein (g)', value: 'protein' },
          { text: 'Iron (%)', value: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: '1%',
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: '1%',
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: '7%',
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: '8%',
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: '16%',
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: '0%',
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: '2%',
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: '45%',
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: '22%',
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: '6%',
          },
        ],
      };
    },
       
  watch: {
      async '$route'(to, from) {
        if(to !== from ) {
          // console.log('POS',this.shippos, 'PATH',this.shippath)
          await this.$store.dispatch('getShipPositionsMission', this.$route.params.id)
          this.shippos=[]
          this.shippath=[]
          this.testspos()
          this.drawDirection()
        }
      }
    },
    
    async created() {
      await this.$store.dispatch('getShipPositionsMission', this.$route.params.id)
      this.testspos()
      this.drawDirection()
    },

    computed: {
      mapCenter() {
        if (this.shippos.length === 0) {
          return 
        }
        console.log(this.shippos)
        return {
          lat: this.shippos[0].position.lat,
          lng: this.shippos[0].position.lng,
        }
      },

      ...mapState([
        'shipPositionsDetails',
      ]),
    },

    methods: {
      testspos() {
        // console.log(this.shipPositionsDetails)
        this.shipPositionsDetails.forEach((pos) => {
          this.shippos.push({"id": Number(pos.id), "position": {"lat": Number(pos.latitude), "lng": Number(pos.longitude)}})
        })
      },
      drawDirection() {
        this.shippos.forEach((pos) => {
          this.shippath.push( {lat:pos.position.lat , lng:pos.position.lng} )
        })
      },

      validate () {
        this.$refs.form.validate()
      },
      
      async AddShipPosition () {
        // console.log('form shippos:',{latitude, longitude, date_time})
        if (this.$refs.form.validate()) {
          // console.log(this.valid)
          await getAPI.post('/api/missions/shippositions/', 
            this.send_form, {
            headers: { 
              'Authorization': 'Token ' + this.$store.state.token,
              'Content-Type': 'application/json',   
            }
            })
        // .then(() => console.log('addshippos ok', this.send_form))
        .then(() => this.$store.dispatch('getShipPositionsMission', this.$route.params.id))
        .then(() => this.testspos())
        .then(() => this.drawDirection())
        .catch(err => {console.log(err)}); 
        } 
      },
      
    },
  }
</script>

<style scoped>
#map {
  height:600px;
}

.btn {
  color: rgb(60, 173, 173); 
  margin-bottom: 6px;
}
</style>
