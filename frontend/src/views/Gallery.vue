<template>
  <v-main>
    <v-container class="d-flex flex-column background-wrap" fluid >
      <h2>Galerie photos</h2>
      <v-divider/>
     
      <div class="block galleryBlock mt-4 mx-8">
        <v-btn
          color="#198F8F"
          class="mb-2 mt-0"
          @click="$refs.inputUpload.click()"
          v-if="verifMember == true"
        >
          Nouvelle photo
        </v-btn>
        <input
          multiple
          type="file" 
          v-show="false" 
          ref="inputUpload"
          @change="onFileSelected($event)"
        />

        <v-row v-if="pictures.length !==0">
          <v-col
            v-for="(item, i) in pictures"
            :key="i"
            class="d-flex child-flex"
            cols="12"
            sm="6"
            md="4"
          >
          <v-hover>
        <template v-slot:default="{ hover }">
            <v-img
              :src= static_url(item.picture)
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

              <v-fade-transition>
                <v-overlay
                  v-if="hover"
                  absolute
                  color="#8c9297"
                >
                  <v-btn
                    icon
                    fab
                    outlined
                    @click="deletePicture(item.id)"
                  >
                    <v-icon
                    >
                    mdi-delete
                    </v-icon>
                  </v-btn>
                </v-overlay>
              </v-fade-transition>

            </v-img>
        </template>
          </v-hover>
          </v-col>
        </v-row>
      </div>
    </v-container>
  </v-main>
</template>

<script>
import { getAPI, baseURL } from '../axios-api'
import { mapGetters } from 'vuex'

// @ is an alias to /src
export default {
  name: 'Gallery',
  components: {
  },
  data() {
    return {
      dialog: false,
      files:[],
      form: {
      title:""
      },    
      pictures: {},
      selectedFile: null,
      valid: false,
    };
  },

  mounted(){
    this.getPicture();
  },

  computed: {
    ...mapGetters(['currentMission' ]),
    missionD() {
      return this.currentMission(this.$route.params.id);
    },
    ...mapGetters([ 'memberMission']),
    verifMember() {
      return this.memberMission(this.$route.params.id);
    },
    static_url() {
      return item => {
        return `${baseURL}${item}`
      }
    }
  },

  methods:{
    async getPicture() {
      const data = await getAPI.get(`/api/posts/gallery/?missionId=${this.$route.params.id}`)
      this.pictures = data.data;
    },


    onFileSelected(event) {
      const files = event.target.files
      this.files = [...this.files, ...files];
      this.onUpload();
    },

    async onUpload() {
      const fd = new FormData();
      this.files.forEach((file) => {
        if(this.validate(file) === "") {
          fd.append('file', file, file.name);
        }
      })
      try {
        await getAPI.post(`/api/posts/gallery/post_picture/${this.$route.params.id}/`, 
          fd, {
          headers: { 
            'Authorization': 'Token ' + this.$store.state.token,
            'Content-Type': 'multipart/form-data',   
          }
        });
        this.files = [];
        this.getPicture();
      } catch(err) {
        console.log(`erreur: ${err}`) 
      }
    },

    validate(file) {
      const allowedTypes = ["image/png", "image/jpeg", "image/gif"];
      if (!allowedTypes.includes(file.type)) {
        return "Not an image";
      }
      return "";
    },

    async deletePicture(id){
      await getAPI.delete(`/api/posts/gallery/${id}/`, {
        headers: { 'Authorization': 'Token ' + this.$store.state.token,}
      })
      this.getPicture();
    },

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