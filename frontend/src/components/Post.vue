<template>
  <v-container>
    <div class="mx-8">
      <v-btn
        color="#198F8F"
        class="mb-2 mt-4"
        @click="dialog = true"
        v-if="verifMember == true"
      >
        Nouveau post {{ Category }}
      </v-btn>

      <v-row class="mt-4">
        <v-col
          v-for="item in postMedBoard"
          :key="item.id"
          cols="12"
          align="center"
          class="mb-4"
        >
          <v-card class="post-wrap" flat>
            <v-card-title>
              <h3>{{ item.title }}</h3>
              <v-spacer></v-spacer>
              <i>
                {{
                  new Date(item.created_at).toLocaleDateString("fr-FR", {
                    weekday: "long",
                    year: "numeric",
                    month: "long",
                    day: "numeric"
                  })
                }}
              </i>
              <v-btn
                class="ml-6 mr-4"
                icon
                outlined
                @click="
                  selectItem(item);
                  dialog_update = true;
                "
                v-if="verifMember == true"
              >
                <v-icon> mdi-grease-pencil </v-icon>
              </v-btn>
            </v-card-title>
            <v-divider class="mx-8"></v-divider>
            <v-card-text>
              <v-img
                v-if="item.post_image !== null"
                contain
                max-width="800px"
                :src="static_url(item.post_image)"
              ></v-img>
              <br />
              {{ item.content }}
              <br />
              <div class="resp-conteneur">
                <iframe
                  id="ytplayer"
                  type="text/html"
                  :src="`${item.video_url}`"
                  frameborder="0"
                  allowfullscreen="allowfullscreen"
                >
                </iframe>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <!-- Add post dialog -->
      <div class="text-center">
        <v-dialog v-model="dialog" max-width="800">
          <v-card>
            <v-container>
              <v-form ref="form" v-model="valid" @submit.prevent="addPost">
                <v-text-field
                  label="Titre"
                  type="text"
                  color="teal"
                  v-model="send_form.form.title"
                  :counter="100"
                  required
                  :rules="[v => !!v || 'Item is required']"
                />
                <v-textarea
                  label="Détails"
                  type="text"
                  color="teal"
                  v-model="send_form.form.content"
                  required
                  :rules="[v => !!v || 'Item is required']"
                ></v-textarea>
                <v-text-field
                  label="Embed Url vidéo youtube "
                  type="text"
                  color="teal"
                  v-model="send_form.form.video_url"
                />
              </v-form>
              <v-file-input
                accept="image/*"
                prepend-icon="mdi-camera"
                label="Image"
                @change="onFileSelected($event)"
              ></v-file-input>
              <v-btn
                type="submit"
                color="teal"
                class="mt-4"
                text
                @click.stop="dialog = false"
                @click="addPost"
              >
                Créer
              </v-btn>
              <v-btn
                text
                @click.stop="dialog = false"
                color="teal"
                class="mt-4"
              >
                Fermer
              </v-btn>
            </v-container>
          </v-card>
        </v-dialog>
      </div>

      <!-- Edit post dialog_update -->
      <div class="text-center">
        <v-dialog v-model="dialog_update" max-width="800">
          <v-card>
            <v-container>
              <v-form
                ref="form_update"
                v-model="valid"
                @submit.prevent="updatePost"
              >
                <v-text-field
                  label="Titre"
                  type="text"
                  color="teal"
                  v-model="selectedItem.title"
                  :value="selectedItem.title"
                  required
                  :rules="[v => !!v || 'Item is required']"
                  :counter="100"
                />
                <v-textarea
                  label="Détails"
                  type="text"
                  color="teal"
                  v-model="selectedItem.content"
                  :value="selectedItem.content"
                  required
                  :rules="[v => !!v || 'Item is required']"
                ></v-textarea>
                <v-text-field
                  label="Embed Url vidéo youtube "
                  type="text"
                  color="teal"
                  v-model="selectedItem.video_url"
                  :value="selectedItem.video_url"
                />
              </v-form>
              <v-file-input
                accept="image/*"
                prepend-icon="mdi-camera"
                label="Image"
                @change="onFileSelected($event)"
              ></v-file-input>
              <v-btn
                text
                @click.stop="dialog_update = false"
                @click="updatePost(selectedItem)"
              >
                Modifier
              </v-btn>
              <v-btn
                text
                @click.stop="dialog_update = false"
                @click="deletePost(selectedItem.id)"
              >
                Supprimer
              </v-btn>
              <v-btn text @click.stop="dialog_update = false">
                Fermer
              </v-btn>
            </v-container>
          </v-card>
        </v-dialog>
      </div>
    </div>
  </v-container>
</template>

<script>
import { mapState, mapActions, mapGetters } from "vuex";
import { getAPI, baseURL } from "../axios-api";

export default {
  name: "Post",
  props: ["Category"],

  data() {
    return {
      dialog: false,
      dialog_update: false,
      params: {
        missionId: this.$route.params.id,
        category: this.Category
      },
      selectedItem: {},
      send_form: {
        form: {
          title: "",
          content: "",
          video_url: ""
        },
        missionId: this.$route.params.id,
        category: this.Category
      },
      valid: false
    };
  },

  async mounted() {
    await this.loadPost(this.params);
  },

  computed: {
    ...mapState(["postMedBoard"]),
    ...mapGetters(["currentMission"]),
    missionD() {
      return this.currentMission(this.$route.params.id);
    },
    ...mapGetters(["memberMission"]),
    verifMember() {
      return this.memberMission(this.$route.params.id);
    },
    static_url() {
      return item => {
        return `${baseURL}${item}`;
      };
    }
  },

  methods: {
    async loadPost(params) {
      await this.$store.dispatch("getPost", params);
    },

    onFileSelected(event) {
      this.selectedFile = event;
    },
    async onUpload(postId) {
      const fd = new FormData();
      fd.append("file", this.selectedFile, this.selectedFile.name);
      if (postId !== 0) {
        await getAPI.post(`/api/posts/update_post_picture/${postId}/`, fd, {
          headers: {
            Authorization: "Token " + this.$store.state.token,
            "Content-Type": "multipart/form-data"
          }
        });
        this.loadPost(this.params);
      } else {
        await getAPI.post("/api/posts/post_picture/", fd, {
          headers: {
            Authorization: "Token " + this.$store.state.token,
            "Content-Type": "multipart/form-data"
          }
        });
      }
    },

    ...mapActions(["postPost"]),
    async addPost() {
      try {
        if (this.$refs.form.validate()) {
          await this.postPost(this.send_form);
          if (this.selectedFile) {
            await this.onUpload(0);
          }
          this.loadPost(this.params);
        }
      } catch (err) {
        console.log(`erreur: ${err}`);
      }
    },

    ...mapActions(["patchPost"]),
    async updatePost() {
      if (this.$refs.form_update.validate()) {
        try {
          await this.patchPost(this.selectedItem);
          if (this.selectedFile) {
            await this.onUpload(this.selectedItem.id);
          }
          this.loadPost(this.params);
        } catch (err) {
          console.log(`erreur: ${err}`);
        }
      }
    },

    ...mapActions(["removePost"]),
    async deletePost(id) {
      await this.removePost(id);
      this.loadPost(this.params);
    },

    selectItem(item) {
      this.selectedItem = item;
    }
  }
};
</script>

<style lang="scss" scoped>
.post-wrap {
  background-color: #a3b3d5;
}

.resp-conteneur {
  position: relative;
  overflow: hidden;
  padding-top: 56.25%;
}

.resp-conteneur iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}
</style>
