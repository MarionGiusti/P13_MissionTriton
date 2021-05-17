<template>
  <div class="heroBlock">
    <v-carousel hide-delimiters>
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
        reverse-transition="fade-transition"
        transition="fade-transition"
      >  
        <v-row class="title-wrap hidden-sm-and-down" align="center" justify="center" >
          <div class="title" > {{ item.title }} </div>
        </v-row>
      </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
  export default {
    name: 'HeroBlock',
    data() {
      return {
        items: [
          {
            src: require("../assets/buzz-andersen-unsplash.jpg"),
            title: "Emmenez nous à l'aventure !"
          },
          {
            src:require("../assets/thalassa.png"),
            title: "Partager vos campagnes en mer"
          },
          {
            src:require("../assets/hydrophone.png"),
            title: "Expliquer vos manoeuvres instrumentales"
          },
          {
            src:require("../assets/sebastian-pena-lambarri-unsplash.jpg"),
            title: "Vulgariser vos missions"
          },
          {
            src:require("../assets/sofia-zubiria-unsplash.jpg"),
            title: "Et faites nous rêver ..."
          },
        ]
      }
    } 
  }

</script>

<style lang="scss" scoped>

  .heroBlock {
    position: relative;
    .title-wrap {
      background-color:rgba(255, 255, 255, 0.3);
      position: relative;
      height: 20%;
      top: 50%;
      transform: translateY(-50%);

      .title {
      color: rgb(255, 255, 255);
      position: relative;
      z-index: 2;
      font: 500 50px  'Amatic SC' !important;
      }
    }
  }
</style>