import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from '../axios-api'

import { getField, updateField } from 'vuex-map-fields';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    "token": localStorage.getItem('token') || null,
    "user_id": localStorage.getItem('user_id') || null,
    userDetails: {},
    allMissions: [],
    missionDetails: {},
    // "id_mission": null
  },

  getters: {
    getField
  },

  mutations: {
    updateField,

    SetTokenId(state, data) {
      state.token = data.token
      state.user_id = data.user_id
    },

    setUserDetails(state, userDetails) {
      state.userDetails = userDetails
    },

    updateUserDetails(state, values) {
      state.userDetails = Object.assign({}, state.userDetails, values);
    },
   
    setMissionList(state, allMissions) {
      state.allMissions = allMissions
      console.log('setmissionList mutation:', allMissions)
    },
    setMissionDetails(state, missionDetails){
      state.missionDetails = missionDetails
      console.log('setmissionDetails mutation:', missionDetails)
    },
    
    updateMissionList(data) {
      console.log('updatemissionlist:', data)
    },
  
  },

  actions: {
    async userLogin({ commit }, usercredentials) {
        const { data } = await getAPI.post('/api-token-auth/', {
            username: usercredentials.username,
            password: usercredentials.password
          })
        localStorage.setItem('token', data.token)
        localStorage.setItem('user_id', data.user_id)
        console.log("dataToken:", data)
        commit('SetTokenId', data)
    },

    async userRegister({ commit }, usercredentials) {
      const { data } = await getAPI.post('/api/users/', {
          username: usercredentials.username,
          first_name: usercredentials.firstname,
          last_name: usercredentials.lastname,
          password: usercredentials.password1,
          email: usercredentials.email,
        })
        commit('SetTokenId', data )
    },

    async missionRegister ({ commit }, missioncredentials) {
      const { data } = await getAPI.post('/api/missions/', {
          name: missioncredentials.name,
          ship_name: missioncredentials.ship,
          start_date: missioncredentials.start_date,
          end_date: missioncredentials.end_date,
        })
        console.log('missionRegister:', data)
        commit('updateMissionList', data)
    },

    
    // userLogout({ commit }, token ) {
    //   token = null
    //   commit('updateToken', token)
    // },

    userLogout({ commit }) {
      const data  =  {
        user_id: null,
        token: null
      }
      console.log("logoutData:", data)
      commit('SetTokenId', data)
    },

    async patchUserProfile({ commit, state }, usercredentials) {
      const { data } = await getAPI.patch('api/users/' + state.user_id + '/', {
          username: usercredentials.username,
          first_name: usercredentials.first_name,
          last_name: usercredentials.last_name,
          email: usercredentials.email,
          linkedin_link: usercredentials.linkedin_link,
          researchgate_link: usercredentials.researchgate_link,
        }, {
        headers: { 'Authorization': 'Token ' + state.token,}})
        console.log("dataUserProfile:", data)
        commit('updateUserDetails', data)
    },

    loadUserDetails({ commit, state }) {
      getAPI.get('api/users/' + state.user_id + '/')
      // .then(response => response.data)
      .then(data => {
        console.log('methods loadUserDetails:', data)
        let userDetails = data.data
        commit('setUserDetails', userDetails)
      })
      .catch(error => {
        console.log(error)
      })
    },
      
    async loadMissionList({ commit }) {
      await getAPI.get('/api/missions/')
      .then(data => {
        console.log('methods loadMissionList:', data)
        let allMissions = data.data
        commit('setMissionList', allMissions)
      })
      .catch(error => {
        console.log(error)
      })
    },

    // async loadMissionDetails({ commit, state }) {
    //   await getAPI.get('/api/missions/' + state.id_mission)
    //   .then(data => {
    //     console.log('methods loadmissionDetails:', data.data)
    //     let missionDetails = data.data
    //     commit('setMissionDetails', missionDetails)
    //   })
    async loadMissionDetails({ commit }, missionID) {
      console.log('CHALALA', missionID)
      await getAPI.get('/api/missions/' + missionID + '/')
      .then(data => {
        console.log('methods loadmissionDetails:', data.data)
        let missionDetails = data.data
        commit('setMissionDetails', missionDetails)
      })
      .catch(error => {
        console.log(error)
      })
    },

    // userAccount({ commit }) {
    //   getAPI.post('api/users/users/1').then(response => {
    //   commit('updateProfile', response.data)
    //   })
    // }
  },

  modules: {

  }
})
