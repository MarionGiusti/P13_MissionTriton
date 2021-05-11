<template>
  <v-container>
    <div class="mx-8">

      <v-row>
        <v-col cols="12" md="3" v-if="verifMember && verifMember == true">
          <v-form
              ref="form"
              v-model="valid"
              lazy-validation
          >
            <v-text-field
              label="Latitude"
              type="text"
              v-model="send_form.form.latitude"
              color="teal"
              :rules="latitudeRules"
              required
            ></v-text-field>

            <v-text-field
              label="Longitude"
              type="number"
              color="teal"
              v-model="send_form.form.longitude"
              :rules="longitudeRules"
              required
            ></v-text-field>

            <v-text-field
              v-model="send_form.form.date_time"
              label="Date"
              required
              color="teal"
              type="datetime-local"
              :value="this.dateTimeExample"
            ></v-text-field>

            <v-btn
              elevation="2"
              :disabled="!valid"
              color="#198F8F"
              @click="AddShipPosition(send_form.form)"
            >
              Ajouter
            </v-btn>
          </v-form>
        </v-col>
        <v-col cols="12" md="9">
          
          <v-data-table v-if="shipPositionsDetails"
            :headers="headers"
            :items="Coordinates"
            :items-per-page="5"
            class="elevation-1"
          >
            <template v-slot:top>                  
              <v-dialog
                v-model="dialog"
                max-width="500px"
              >
                <v-card>
                  <v-card-title>
                    <span class="headline">Edit Item</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col
                          cols="12"
                          sm="6"
                          md="4"
                        >
                          <v-text-field
                            v-model="editedItem.date_time"
                            label="Date"
                          ></v-text-field>
                        </v-col>
                        <v-col
                          cols="12"
                          sm="6"
                          md="4"
                        >
                          <v-text-field
                            v-model="editedItem.latitude"
                            label="Latitude"
                          ></v-text-field>
                        </v-col>
                        <v-col
                          cols="12"
                          sm="6"
                          md="4"
                        >
                          <v-text-field
                            v-model="editedItem.longitude"
                            label="Longitude"
                          ></v-text-field>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-card-text>
                  <v-card-actions >
                    <v-spacer></v-spacer>
                    <v-btn
                      color="teal"
                      text
                      @click="close"
                      outlined
                    >
                      Annuler
                    </v-btn>
                    <v-btn
                      color="teal"
                      text
                      @click="save(editedItem)"
                      outlined
                    >
                      Modifier
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </template>
            <template v-slot:item.actions="{ item }" v-if="verifMember && verifMember == true">
              <v-icon
                small
                class="mr-2"
                @click="editItem(item)"
              >
                mdi-pencil
              </v-icon>
              <v-icon
                small
                @click="deleteItem(item)"
              >
                mdi-delete
              </v-icon>
            </template>
          </v-data-table>
        </v-col>
      </v-row>
      <v-row>
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
            <!-- <div id="map" ref="map">
            </div> -->
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
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

        dialog: false,
        dialogDelete: false,
        editedIndex: -1,
        editedItem: {
          latitude:"",
          longitude:"",
          date_time:"",
        },
        defaultItem: {
          latitude:"",
          longitude:"",
          date_time:"",
        },
        Coordinates: [],


        headers: [
          { text: 'Date', value: 'date_time'},
          { text: 'Latitude (°)', value: 'latitude' },
          { text: 'Longitude (°)', value: 'longitude' },
          { text: 'Actions', value: 'actions', sortable: false },
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
      },

      dialog (val) {
        val || this.close()
      },

      // currentMission(promise) {
      //   // save Promise result in local state
      //   promise.then(this.verifMember)
      // }
    },
    
    async created() {
      await this.initialise()
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
      ...mapGetters([ 'memberMission']),
      verifMember() {
        return this.memberMission(this.$route.params.id)
      }      
    },

    methods: {
      async initialise(){
        await this.$store.dispatch('getShipPositionsMission', this.$route.params.id)
        this.testspos()
        this.drawDirection()
        this.Coordinates = this.shipPositionsDetails
      },

      testspos() {
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
        if (this.$refs.form.validate()) {
          try {
            await getAPI.post('/api/missions/shippositions/', 
              this.send_form, {
              headers: { 
                'Authorization': 'Token ' + this.$store.state.token,
                'Content-Type': 'application/json',   
              }
            })
            this.shippos=[]
            this.shippath=[]
            await this.initialise()
          } catch(err) {
            console.log(`erreur: ${err}`) 
          }          
        } 
      },

      async UpdateShipPosition (item) {
          try {
            await getAPI.patch(`api/missions/shippositions/${item.id}/`, {         
              date_time: item.date_time,
              latitude: item.latitude,
              longitude: item.longitude,
              }, {
              headers: { 'Authorization': 'Token ' + this.$store.state.token,}
            })
            await this.$store.dispatch('getShipPositionsMission', this.$route.params.id)
              this.shippos=[]
              this.shippath=[]
              this.testspos()
              this.drawDirection()
          } catch(err) {
            console.log(`erreur: ${err}`) 
          }          
      },

      editItem (item) {
        this.editedIndex = this.Coordinates.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      async deleteItem (item) {
        this.editedIndex = this.Coordinates.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.Coordinates.splice(this.editedIndex, 1) 
        await getAPI.delete(`/api/missions/shippositions/${item.id}`, {
          headers: { 'Authorization': 'Token ' + this.$store.state.token,}
        })
        await this.$store.dispatch('getShipPositionsMission', this.$route.params.id)
          this.shippos=[]
          this.shippath=[]
          this.testspos()
          this.drawDirection()     
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem= Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      async save (item) {
        if (this.editedIndex > -1) {
          console.log("BEEEE!!!!!!!!!!!", this.Coordinates)
          Object.assign(this.Coordinates[this.editedIndex], this.editedItem)
        } else {
          this.Coordinates.push(this.editedItem)
        }
        await this.UpdateShipPosition(item)
        this.close()
      },  
    },
  }
</script>

<style lang="scss" scoped>
  #map {
    height:600px;
  }

  .btn {
    color: rgb(60, 173, 173); 
    margin-bottom: 6px;
  }
</style>
