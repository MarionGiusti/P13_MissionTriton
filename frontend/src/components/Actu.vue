<template>
  <v-container>
    <div class="mx-8">
      <v-btn
        color="#198F8F"
        class="mb-2 mt-0"
        @click="dialog = true"
        v-if="verifMember && verifMember == true"
      >
        Nouveau post
      </v-btn>
      <v-virtual-scroll
        :bench="benched"
        :items="Object.values(postActu)"
        :item-height="200"
        height="500"
        class="post-wrap"
        v-if="postActu.length !== 0"
      >
        <template v-slot:default="{ item }">
          <v-list-item :key="item.id">
            <v-list-item-content>
              <v-card class="post-wrap" flat>
                <v-row>
                  <v-col cols="3" class="hidden-sm-and-down">
                    <v-hover>
                      <template v-slot:default="{ hover }">
                        <v-avatar
                          tile
                          :class="{ 'on-hover': hover }"
                          size="150"
                        >
                          <v-img
                            v-if="item.post_image !== null"
                            max-height="150"
                            :src="static_url(item.post_image)"
                          ></v-img>
                          <v-fade-transition>
                            <v-overlay v-if="hover" absolute color="#8c9297">
                              <v-btn
                                icon
                                fab
                                outlined
                                @click="$refs.inputUpload.click()"
                                v-if="verifMember && verifMember == true"
                              >
                                <v-icon>
                                  mdi-camera
                                </v-icon>
                              </v-btn>
                              <input
                                type="file"
                                v-show="false"
                                ref="inputUpload"
                                @change="onFileSelected($event, item.id)"
                              />
                            </v-overlay>
                          </v-fade-transition>
                        </v-avatar>
                      </template>
                    </v-hover>
                  </v-col>
                  <v-col cols="12" md="9">
                    <v-card-title>
                      {{
                        new Date(item.created_at).toLocaleDateString("fr-FR", {
                          weekday: "long",
                          year: "numeric",
                          month: "long",
                          day: "numeric"
                        })
                      }}
                      <br />
                      {{ item.title }}
                      <v-spacer></v-spacer>
                      <v-btn
                        class="mb-4 mr-4"
                        icon
                        outlined
                        @click="
                          selectItem(item);
                          dialog_update = true;
                        "
                        v-if="verifMember && verifMember == true"
                      >
                        <v-icon>
                          mdi-grease-pencil
                        </v-icon>
                      </v-btn>
                    </v-card-title>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        icon
                        @click="
                          selectItem(item);
                          dialog_content = true;
                        "
                      >
                        <v-icon>{{
                          show ? "mdi-chevron-up" : "mdi-chevron-down"
                        }}</v-icon>
                      </v-btn>
                    </v-card-actions>
                  </v-col>
                </v-row>
              </v-card>
            </v-list-item-content>
          </v-list-item>
          <v-divider></v-divider>
        </template>
      </v-virtual-scroll>

      <!-- Show post dialog -->
      <div class="text-center">
        <v-dialog v-model="dialog_content" max-width="800">
          <v-card>
            <v-container>
              <v-card flat>
                <v-card-title>
                  {{
                    new Date(selectedItem.created_at).toLocaleDateString(
                      "fr-FR",
                      {
                        weekday: "long",
                        year: "numeric",
                        month: "long",
                        day: "numeric"
                      }
                    )
                  }}
                  : {{ selectedItem.title }}
                </v-card-title>
                <v-card-text>
                  {{ this.selectedItem.content }}
                </v-card-text>
                <v-card-actions>
                  <v-btn
                    class="mt-4"
                    text
                    @click.stop="dialog_content = false"
                    color="teal"
                  >
                    Fermer
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-container>
          </v-card>
        </v-dialog>
      </div>

      <!-- Add post dialog -->
      <div class="text-center">
        <v-dialog v-model="dialog" max-width="500">
          <v-card>
            <v-container>
              <v-form ref="form" v-model="valid" @submit.prevent="addPost">
                <v-text-field
                  label="Titre"
                  type="text"
                  color="teal"
                  v-model="send_form.form.title"
                  required
                  :rules="[v => !!v || 'Item is required']"
                  :counter="100"
                />
                <v-textarea
                  label="Détails"
                  type="text"
                  color="teal"
                  v-model="send_form.form.content"
                  required
                  :rules="[v => !!v || 'Item is required']"
                ></v-textarea>
                <v-file-input
                  accept="image/*"
                  prepend-icon="mdi-camera"
                  label="Image"
                  @change="onFileSelected($event, 0)"
                ></v-file-input>
              </v-form>
              <v-btn
                text
                color="teal"
                class="mb-4"
                @click.stop="dialog = false"
                @click="addPost"
              >
                Créer
              </v-btn>
              <v-btn
                text
                color="teal"
                class="mb-4"
                @click.stop="dialog = false"
              >
                Fermer
              </v-btn>
            </v-container>
          </v-card>
        </v-dialog>
      </div>

      <!-- Edit post dialog_update -->
      <div class="text-center">
        <v-dialog v-model="dialog_update" max-width="500">
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
                  required
                  :rules="[v => !!v || 'Item is required']"
                  v-model="selectedItem.title"
                  :value="selectedItem.title"
                  :counter="100"
                />
                <v-textarea
                  label="Détails"
                  type="text"
                  color="teal"
                  required
                  :rules="[v => !!v || 'Item is required']"
                  v-model="selectedItem.content"
                  :value="selectedItem.content"
                ></v-textarea>
              </v-form>
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
            </v-container>
          </v-card>
        </v-dialog>
      </div>
    </div>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import { mapState, mapActions } from "vuex";
import { getAPI, baseURL } from "../axios-api";

export default {
  name: "Actu",
  data: () => ({
    benched: 0,
    category: "Actu",
    dialog: false,
    dialog_update: false,
    dialog_content: false,
    selectedItem: {},
    valid: false,
    selectedFile: null,
    show: false,
    send_form: {
      form: {
        title: "",
        content: "",
        video_url: ""
      },
      missionId: null,
      category: "Actu"
    }
  }),

  watch: {
    async $route(to, from) {
      if (to !== from) {
        let missionId = this.$route.params.id;
        let params = { category: "Actu", missionId: missionId };
        this.loadPost(params);
      }
    }
    // memberMission(promise) {
    // // save Promise result in local state
    // promise.then(this.verifMember)
    // },
  },

  async mounted() {
    let missionId = this.$route.params.id;
    let params = { category: "Actu", missionId: missionId };
    await this.loadPost(params);
  },

  computed: {
    ...mapState(["postActu"]),
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
      try {
        await this.$store.dispatch("getPost", params);
      } catch (err) {
        console.log(`erreur: ${err}`);
      }
    },

    onFileSelected(event, postId) {
      this.selectedFile = event;
      if (postId !== 0) {
        this.selectedFile = event.target.files[0];
        this.onUpload(postId);
      }
    },
    async onUpload(postId) {
      const fd = new FormData();
      fd.append("file", this.selectedFile, this.selectedFile.name);
      if (postId !== 0) {
        try {
          await getAPI.post(`/api/posts/update_post_picture/${postId}/`, fd, {
            headers: {
              Authorization: "Token " + this.$store.state.token,
              "Content-Type": "multipart/form-data"
            }
          });
        } catch (err) {
          console.log(`erreur: ${err}`);
        }
        let missionId = this.$route.params.id;
        let params = { category: "Actu", missionId: missionId };
        this.loadPost(params);
      } else {
        try {
          await getAPI.post("/api/posts/post_picture/", fd, {
            headers: {
              Authorization: "Token " + this.$store.state.token,
              "Content-Type": "multipart/form-data"
            }
          });
        } catch (err) {
          console.log(`erreur: ${err}`);
        }
      }
    },

    ...mapActions(["postPost"]),
    async addPost() {
      this.send_form.missionId = this.$route.params.id;
      if (this.$refs.form.validate()) {
        try {
          await this.postPost(this.send_form);
          if (this.selectedFile) {
            await this.onUpload(0);
          }
          let missionId = this.$route.params.id;
          let params = { category: "Actu", missionId: missionId };
          this.loadPost(params);
        } catch (err) {
          console.log(`erreur: ${err}`);
        }
      }
    },

    ...mapActions(["patchPost"]),
    async updatePost() {
      if (this.$refs.form_update.validate()) {
        try {
          await this.patchPost(this.selectedItem);
        } catch (err) {
          console.log(`erreur: ${err}`);
        }
      }
      let missionId = this.$route.params.id;
      let params = { category: "Actu", missionId: missionId };
      this.loadPost(params);
    },

    ...mapActions(["removePost"]),
    async deletePost(id) {
      await this.removePost(id);
      let missionId = this.$route.params.id;
      let params = { category: "Actu", missionId: missionId };
      this.loadPost(params);
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
</style>
