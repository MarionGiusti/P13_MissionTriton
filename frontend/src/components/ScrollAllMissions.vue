<template> 
    <v-container >
      <v-row>
        <v-col cols="12" md="4" v-for="(missionGroup, i) in missionGroups" :key="i">
          <div align="center">
            <h3 >{{ missionGroup.name }}</h3>
            <v-card class="mission-wrap" elevation="16" width="300">
              <!-- <v-card-title>
                {{ missionGroup.name }}
              </v-card-title> -->
              <v-virtual-scroll
                :bench="benched"
                :items="missionGroup.missions"
                height="200"
                item-height="60"
              >
                <template v-slot:default="{ item, i }">
                  <v-list-item :key="i" router :to="{name: 'HomeMission', params: {id: item.id}}" @click="loadShippos(item.id)">
                    <!-- <v-list-item-action>
                      <v-btn
                        fab
                        small
                        depressed
                        color="primary"
                      >
                        {{ item.name }}
                      </v-btn>
                    </v-list-item-action> -->
                    <v-list-item-content>
                      <v-list-item-title>
                        <strong> {{ item.name }} </strong> / Départ : {{ item.start_date }}
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-divider></v-divider>
                </template>
              </v-virtual-scroll>
            </v-card>
          </div>       
        </v-col>
      </v-row>
  </v-container>
</template>

<script>
import {mapGetters} from 'vuex'
// import { mapState} from 'vuex'

  export default {
    name: 'ScrollAllMissions',
    data: () => ({
      benched: 0,
      missionGroups: [
        {
          // id:1,
          name: 'Archivées',
          missions: null,
        },
        {
          // id:2,
          name: 'En cours',
          missions: null,
        },
        {
          // id:3,
          name: 'À venir',
          missions: null,
        }
      ],
    }),


    async created() {
      await this.initialise()    
    }, 
    computed: {
    // ...mapState([ 'missions']),
    ...mapGetters([ 'pastMissions', 'nowMissions', 'futureMissions' ]),

  


    // items () {
    //   var a = this.futureMissions.slice().sort((a, b) => new Date(a.start_date).getTime() - new Date(b.start_date).getTime())
    //   console.log('CHOUBIBI', a)
    //   return a
    // },
    },
    methods: {
      initialise() {
        let past = this.$store.getters.pastMissions;
        this.missionGroups[0].missions = past;

        let now = this.$store.getters.nowMissions;
        this.missionGroups[1].missions = now;

        let future = this.$store.getters.futureMissions;
        this.missionGroups[2].missions = future;
      }
      // callFunction: function () {
      //   var currentDate = new Date();
      //   console.log(currentDate, 'll', currentDate.getTime());
      //   var currentDateWithFormat = new Date().toJSON().slice(0,10).replace(/-/g,'/');
      //   console.log(currentDateWithFormat);
      // },
      // compDateMiss(){
      //   var currentDate = new Date();
      //   console.log(currentDate, 'll', currentDate.getTime());
      //   this.missions.forEach((date) => {
      //     let Sdate = date.start_date
      //     let SdateT = new Date(Sdate)
      //     let Edate = date.end_date
      //     let EdateT = new Date(Edate)

      //     if (EdateT.getTime() < currentDate.getTime()) {
      //       this.past_missions.push(date)
      //       // console.log('HAY', date);
      //     }
      //     else if (SdateT.getTime() > currentDate.getTime()) {
      //       this.future_missions.push(date)
      //       // console.log('HEY', date);
      //     }
      //     else {
      //       this.now_missions.push(date)
      //       // console.log('HOY', date);
      //     }
      //   })
      // },
    }
  } 
</script>

<style lang="scss" scoped>
.mission-wrap {
  background-color:#A3B3D5;
}

h3 {
  font: 400 20px 'Dosis' !important;
}
</style>