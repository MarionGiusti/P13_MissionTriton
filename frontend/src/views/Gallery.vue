<template>
  <v-main>
    <v-container class="d-flex flex-column background-wrap" fluid >
      Galerie photos
      <div class="block galleryBlock">
        <v-row>
          <v-col
            v-for="n in 9"
            :key="n"
            class="d-flex child-flex"
            cols="4"
          >
            <v-img
              :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
              :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
              aspect-ratio="1"
              class="grey lighten-2"
            >
              <template v-slot:placeholder>
                <v-row
                  class="fill-height ma-0"
                  align="center"
                  justify="center"
                >
                  <v-progress-circular
                    indeterminate
                    color="grey lighten-5"
                  ></v-progress-circular>
                </v-row>
              </template>
            </v-img>
          </v-col>
        </v-row>
      </div>
    </v-container>
  </v-main>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Gallery',
  components: {
  }
}
</script>

<style lang="scss" scoped>

.background-wrap {
  margin-top: 40px;
  background-color:#54658C;
  width: 95%;
}
</style>