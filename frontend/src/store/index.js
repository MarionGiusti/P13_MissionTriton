import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from '../axios-api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    "token": null,
  },

  mutations: {
    updateStorage(state, token) {
        state.token = token
    },
  },

  actions: {
    async userLogin({commit}, usercredentials) {
          const { data } = await getAPI.post('/api-token-auth/', {
              username: usercredentials.username,
              password: usercredentials.password
            })
            commit('updateStorage', data )
            // commit('updateStorage', resp.data.token)
    }
  },

  modules: {

  }
})
