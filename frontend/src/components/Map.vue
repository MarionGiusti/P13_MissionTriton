<template>
  <v-container>
    <v-row>
      <h4 v-if=" missionD.ship_positions">LALA: {{ missionD.ship_positions }}
      HHI: {{  missionD.ship_positions[0][2] }}
      </h4>
      <v-col cols="2">
    <!-- <v-btn @click="drawMarkers">Draw Marker</v-btn>
    <v-btn @click="drawDirection">Draw Direction</v-btn> -->
        <v-form
            ref="form"
            v-model="valid"
            lazy-validation
          >
            <v-text-field
              label="Latitude"
              type="text"
              v-model="form.latitude"
              :counter="10"
              :rules="latitudeRules"
              required
            ></v-text-field>

            <v-text-field
              label="Longitude"
              type="number"
              v-model="form.longitude"
              :rules="longitudeRules"
              required
            ></v-text-field>

            <!-- <v-text-field
              v-model="date"
              :rules="DateRules"
              label="Date"
              required
            ></v-text-field> -->

            <v-btn
              elevation="2"
              :disabled="!valid"
              class="btn"
              outlined
              @click="validate"
              color="#09033E"
              small
            >
              Validate
            </v-btn>

            <v-btn
            elevation="2"
            class="btn"
            outlined
            @click="resetValidation"
            color="#09033E"
            small
            >
              Reset Form
            </v-btn>
          </v-form>
        </v-col>
        <v-col>
          <GmapMap
            :center="mapCenter"
            :zoom="7"
            map-type-id="satellite"
            style="width: 100%; height: 400px"
          >
            <GmapMarker
              :key="index"
              v-for="(m, index) in markers"
              :position="m.position"
              :clickable="true"
              :draggable="false"
              @click="center=m.position"
            />
            <gmap-polyline
              :path.sync="paths" 
              :options="polylineOptions"
            >
            </gmap-polyline>
          </GmapMap>
          <div id="map" ref="map">
          </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'


// const home = { lat: 53.562, lng: -2.253};
// const work = { lat: 53.463, lng: -2.249}
const lineSymbol = {
    path: "M 0,-1 0,1",
    strokeOpacity: 1,
    strokeColor: "yellow",
    scale: 2.5,
  };

  export default {
    name: 'Map',
    data() {
      return {
        // map:null,
        markers: [
          // {id: 1, name:'Départ', lat: 53.562, lng: -2.253 },
          // {id: 2, name:'', lat: 53.463, lng: -2.250} ,
          {id: 3, name:'A', position: { lat: 38.227, lng: -32.225} },
          {id: 4, name:'Arrivée', position: { lat: 37.736, lng: -25.655} },

        ],
        // center: home,
        paths: [],
        polylineOptions: {
          strokeOpacity: 0,
          icons: [{
            icon: lineSymbol,
            offset: "0",
            repeat: "20px",
          }]
        },

        valid: true,
        form: {
          latitude:"",
          longitude:"",
        },
        latitudeRules: [
          v => !!v || 'Latitude is required',
          // v => (v && v.length <= 10) || 'Latitude must be less than 10 characters',
        ],
        longitudeRules: [
          v => !!v || 'Longitude is required',
          // v => /.+@.+\..+/.test(v) || 'Longitude must be valid',
        ],
        // DateRules: [
        //   v => !!v || 'Date is required',
          // v => /.+@.+\..+/.test(v) || 'Date must be valid',
        // ],
      };
    },
    computed: {
      mapCenter() {
        return {
          lat: this.markers[0].position.lat,
          lng: this.markers[0].position.lng,
        }
      },

      ...mapGetters([ 'currentMission' ]),
      missionD() {
        return this.currentMission(this.$route.params.id);
      },

    },

    // OLD
    // mounted(){
    //   this.map = new window.google.maps.Map(this.$ref["map"], {
    //     center: {lat: -25, lng:130},
    //     zoom:4
    //   })
    //   new window.google.maps.Marker({
    //     position: {lat:-25, lng: 131},
    //     map: this.map
    //   })
    // },
    
    //FONCTIONNE
    mounted() {
      this.drawDirection()
      this.drawMarkers()
    },

    methods: {
      drawMarkers() {
        // console.log(this.markers[0].position)
        this.markers = [
          {
            position: { lat:this.markers[0].position.lat, lng:this.markers[0].position.lng },
          },
          {
            position: { lat:this.markers[1].position.lat, lng:this.markers[1].position.lng },
          }
        ]; 
      },
      drawDirection() {
        this.paths = [ { lat:this.markers[0].position.lat, lng:this.markers[0].position.lng }, { lat:this.markers[1].position.lat, lng:this.markers[1].position.lng } ]
      },
      validate () {
        this.$refs.form.validate()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
      // async AddShipPosition ({latitude, longitude}) {
      //   console.log(this.valid)
      //   if (this.$refs.form.validate()) {
      //     console.log(this.valid)
      //     await this.$store
      //   }
      // }
    },
  }

</script>

<style scoped>
#map {
  height:600px;
  /* background: gray; */
  }
.btn {
  color: rgb(60, 173, 173); 
  margin-bottom: 6px;
}
</style>
