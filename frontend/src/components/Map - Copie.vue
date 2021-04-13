<template>
  <v-container>
    <v-row>
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
              :disabled="!valid"
              class="btn"
              outlined
              @click="validate"
            >
              Validate
            </v-btn>

            <v-btn
            class="btn"
            outlined
              @click="resetValidation"
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
              :icon="markerOptions"
              @click="center=m.position"
            />
            <gmap-polyline
              :path.sync="paths" 
              :options="polylineOptions"
              :icons="lineIcons"
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
// import {loadedGoogleMapsAPI} from '@/utils/gmaps'

// const home = { lat: 53.562, lng: -2.253};
// const work = { lat: 53.463, lng: -2.249}
// const mapMarker = require('../assets/logo.png');
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
        // markerOptions: {
        //   url: mapMarker,
        //   size: {width: 60, height: 90, f: 'px', b: 'px',},
        //   scaledSize: {width: 30, height: 45, f: 'px', b: 'px',},
        // },
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
      }
    },
  //   mounted: function() {
  //       console.log("map: ", google.maps)
  //           this.map = new google.maps.Map(document.getElementById('myMap'), {
  //           center: {lat:61.180059, lng: -149.822075},
  //           scrollwheel: false,
  //           zoom: 4
  //           })
  // },
  // mounted(){  
  //      loadedGoogleMapsAPI.then(()=>{
  //        this.initMap()
  //      });
  //    },
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
    //   initMap(){
    //     console.log(google.maps); //You can now access google maps object here
    //     new window.google.maps.Map(document.getElementById('map'), {
    //       // You configuration goes here
    //     })
    //  }

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
