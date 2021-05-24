<template>
  <v-main>
    <v-container class="d-flex flex-column background-wrap" fluid>
      <h2>La vie à Bord !</h2>
      <v-divider />
      <Post Category="Onboard"></Post>
    </v-container>
  </v-main>
</template>

<script>
import Post from "../components/Post.vue";

export default {
  name: "OnBoard",
  components: {
    Post
  }
};
</script>

<style lang="scss" scoped>
.background-wrap {
  margin-top: 40px;
  background-color: #54658c;
  width: 95%;
}
</style>
