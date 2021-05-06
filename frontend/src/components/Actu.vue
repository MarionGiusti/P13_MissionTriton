<template>
  <v-container>
    <div class="mx-8">
    <v-btn
      color="#198F8F"
      class="mb-2 mt-0"
      @click="dialog = true "
    >
      Nouveau post
    </v-btn>
      <v-virtual-scroll
      :bench="benched"
      :items="Object.values(postActu)"
      :item-height="200"
      height="500"
      class="post-wrap"
      v-if="postActu.length!==0"
    >
      <template v-slot:default="{ item}" >
        <v-list-item :key="item.id" >
            <!-- <v-list-item-avatar> -->
              <!-- <v-img
                height="250"
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
              ></v-img> -->
              <!-- <v-img  :src=item.post_image ></v-img> -->
          <!-- </v-list-item-avatar> -->
          <v-list-item-content>
            <!-- <v-list-item-title>{{ item.created_at}} : {{ item.title }}</v-list-item-title> -->
            <v-card class="post-wrap" flat>    
              <v-row>
                <v-col cols="3" class="hidden-sm-and-down">
                  <v-hover>
                    <template v-slot:default="{ hover }">
                      <!-- <v-col cols="3"> -->
                        <v-avatar
                          tile
                          :class="{ 'on-hover': hover }"
                          size="150"
                        >
                          <v-img  v-if="item.post_image !==null" max-height="150" :src="`http://127.0.0.1:8000${item.post_image}`" ></v-img>
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
                                  @click="$refs.inputUpload.click()"
                                >
                                  <v-icon
                                  >
                                  mdi-camera
                                  </v-icon>
                                </v-btn>
                                <input type="file" v-show="false" ref="inputUpload" @change="onFileSelected($event, item.id)">
                              </v-overlay>
                            </v-fade-transition>
                          
                        </v-avatar>
                      <!-- </v-sheet> -->
                      <!-- </v-col> -->
                    </template>
                  </v-hover>
                </v-col>

                <v-col cols="12" md="9">
                  
                  <v-card-title >
                      {{ 
                        new Date(item.created_at).toLocaleDateString('fr-FR', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
                      }} <br/> {{ item.title }}
                    <v-spacer></v-spacer>
                    <v-btn
                      class="mb-4 mr-4" 
                      icon
                      outlined
                      @click="selectItem(item); dialog_update=true">
                        <v-icon
                        >
                          mdi-grease-pencil
                        </v-icon>
                    </v-btn>
                  </v-card-title>
                                       
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <!-- <v-btn
                      icon
                      @click="show = !show"
                    > -->
                    <v-btn
                      icon
                      @click="selectItem(item) ; dialog_content=true"
                    >
                      <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                    </v-btn>
                  </v-card-actions>

                  <!-- <v-expand-transition>
                    <div v-show="show">
                      <v-divider></v-divider>
                      <v-card-text>
                        {{ item.content }}
                      </v-card-text>
                    </div>
                  </v-expand-transition> -->
                </v-col>
              </v-row>
            </v-card>
          </v-list-item-content>     
          </v-list-item>
        <v-divider></v-divider>
      </template>
    </v-virtual-scroll>

    <!-- ASHOW post dialog -->
      <div class="text-center">
        <v-dialog
          v-model="dialog_content"
          max-width="800"
        >
          <v-card>
            <v-container>
              <v-card flat>
                <v-card-title>
                  {{ 
                    new Date(selectedItem.created_at).toLocaleDateString('fr-FR', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
                  }} : {{ selectedItem.title }}
                </v-card-title>
                <v-card-text>
              {{ this.selectedItem.content  }}
                </v-card-text>
                <v-card-actions>
              <v-btn
                class="mt-4"
                text
                @click.stop="dialog_content = false"
                outlined
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
      <v-dialog
        v-model="dialog"
        max-width="500"
      >
        <v-card>
          <v-container>
          <v-form ref="form"  v-model="valid" @submit.prevent="addPost">
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
            <!-- <input 
              type="file" 
              ref="inputUpload" 
              @change="onFileSelected($event, 0)"
            > -->
            <v-file-input
              accept="image/*"
              prepend-icon="mdi-camera"
              label="Image"
              @change="onFileSelected($event,0)"
            ></v-file-input>
          </v-form>
          <v-btn 
            text
            color="teal"
            outlined
            class="mx-4"
            @click.stop="dialog=false"
            @click="addPost"
          >
            Créer
          </v-btn>
          <v-btn 
            text
            color="teal"
            outlined
            class="mx-4"
            @click.stop="dialog=false"
          >
            Annuler
          </v-btn>
          </v-container>
          </v-card>
      </v-dialog>
    </div>

    <!-- Edit post dialog_update -->
    <div class="text-center">
      <v-dialog
        v-model="dialog_update"
        max-width="500"
      >
        <v-card>
          <v-container>
          <v-form ref="form_update" v-model="valid" @submit.prevent="updatePost">
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
            <!-- <v-file-input
              accept="image/*"
              prepend-icon="mdi-camera"
              label="Image"
              @change="onFileSelected($event)"
            ></v-file-input> -->
          </v-form>
          <v-btn 
            text
            @click.stop="dialog_update=false"
            @click="updatePost(selectedItem)"
          >
            Modifier
          </v-btn>
          <v-btn 
            text
            @click.stop="dialog_update=false"
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
import { mapState, mapActions } from 'vuex'
import { getAPI } from '../axios-api'

  export default {
    name: 'Actu',
    data: () => ({
      benched: 0,
      category: 'Actu',
      dialog: false,
      dialog_update: false,
      dialog_content: false,
      selectedItem: {},
      valid: false,
      selectedFile: null,
      show: false,


      send_form: {
        form: {
          title:"",
          content:"",
          video_url:""
        },
        missionId: null,
        category: 'Actu'
      },

    }),

    watch: {
      async '$route'(to, from) {
        if(to !== from) {
          let missionId = this.$route.params.id
          let params = {category:'Actu', missionId: missionId}
          this.loadPost(params)
        }
      }
    },

    
    
    async mounted(){
      let missionId = this.$route.params.id
      // this.params.missionId = this.$route.params.id
      // console.log('RRRRUN', missionId)
      // this.$store.dispatch('getPostActu', this.category, missionId)
      //   .then(() => console.log('postactu ok'))
      //   .catch(err => {console.log(err)})
      let params = {category:'Actu', missionId: missionId}
      await this.loadPost(params)


    },

    computed: {
      ...mapState(['postActu']),
    },

    methods: {
      async loadPost(params){
        await this.$store.dispatch('getPost', params)
        .then(() => console.log('postactu ok'))
        .catch(err => {console.log(err)})
      },

      onFileSelected(event, postId) {
        console.log('BABBYYY', event)
        this.selectedFile = event
        if (postId !== 0) {
          this.selectedFile = event.target.files[0]
          this.onUpload(postId)
          console.log("POSTID", postId, this.selectedFile)
        }
      },
      async onUpload(postId) {
        const fd = new FormData();
        fd.append('file', this.selectedFile, this.selectedFile.name)
        console.log('ON UPlOAD FILE', fd)
        if (postId !== 0) {
          // await getAPI.patch(`/api/posts/${postId}/`
          await getAPI.post(`/api/posts/update_post_picture/${postId}/`, 
          fd, {
          headers: { 
            'Authorization': 'Token ' + this.$store.state.token,
            'Content-Type': 'multipart/form-data',   
          }
          })

          let missionId = this.$route.params.id
          let params = {category:'Actu', missionId: missionId}
          this.loadPost(params)
        }
        else {
          await getAPI.post('/api/posts/post_picture/', 
            fd, {
            headers: { 
              'Authorization': 'Token ' + this.$store.state.token,
              'Content-Type': 'multipart/form-data',   
            }
          })
        }
      },

      ...mapActions(['postPost']),
      async addPost(){
        this.send_form.missionId = this.$route.params.id
        console.log('FORM', this.selectedFile)
        if (this.$refs.form.validate()) {
          await this.postPost(this.send_form)
          // await getAPI.post('/api/posts/', 
          //   this.send_form, {
          //   headers: { 
          //     'Authorization': 'Token ' + this.$store.state.token,
          //     'Content-Type': 'application/json',   
          //   }
          //   })
          if (this.selectedFile) {
            await this.onUpload(0)
          }         
          let missionId = this.$route.params.id
          let params = {category:'Actu', missionId: missionId}
          this.loadPost(params)
        }
      },

      ...mapActions(['patchPost']),
      async updatePost() {
        console.log(this.valid)
        if (this.$refs.form_update.validate()) {
          console.log(this.valid)
          await this.patchPost(this.selectedItem)
            .then(() => console.log('method patch mission user ok'))
            .catch(err => {console.log(err)});
        }
        console.log('UPDATE SELECTED ITEM', )
        
        let missionId = this.$route.params.id
        let params = {category:'Actu', missionId: missionId}
        this.loadPost(params)
      },

      ...mapActions(['removePost']),
      async deletePost(id){
        await this.removePost(id)
        // await getAPI.delete(`/api/posts/${id}/`, {
        //   headers: { 'Authorization': 'Token ' + this.$store.state.token,}
        // })
        
        let missionId = this.$route.params.id
        let params = {category:'Actu', missionId: missionId}
        this.loadPost(params)
      },

      selectItem(item){
        this.selectedItem = item
      },

    

    },
  }

</script>

<style lang="scss" scoped>
.post-wrap {
  background-color:#A3B3D5;
}
</style>