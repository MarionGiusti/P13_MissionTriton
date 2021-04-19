import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from '../axios-api'

import { getField, updateField } from 'vuex-map-fields';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('token') || null,
    user_id: localStorage.getItem('user_id') || null,
    userDetails: {},
    // missionList: [] ,
    missions: [],
    // allMissions: [],
    // missionDetails: {},
    // "id_mission": null
    missionUserDetails: {},
  },

  getters: {
    getField,
    currentMission: (state) => (id) => {
      return state.missions.find(missions => missions.id === id)
    }
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
   
    // setMissionList(state, missList) {
    //   state.missionList = missList
    //   console.log('setMissionList mutation:', missList)
    // },

    setMissions(state, allMissions) {
      state.missions = allMissions
      console.log('setMissions mutation:', allMissions)
    },

    // setMissionDetails(state, missionDetails){
    //   state.missionDetails = missionDetails
    //   console.log('setmissionDetails mutation:', missionDetails)
    // },
    
    updateMissionList(data) {
      console.log('updatemissionlist:', data)
    },

    setMissionuser(state, missionUserDetails) {
      state.missionUserDetails = missionUserDetails
      console.log('setMissionuser mutation:', missionUserDetails)
    },

    updateMissionUserDetails(state, values) {
      state.missionUserDetails = Object.assign({}, state.missionUserDetails, values);
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
        console.log("action userLogin, dataToken:", data)
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
        console.log('action missionRegister:', data)
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
      localStorage.removeItem('token')
      localStorage.removeItem('user_id')
      console.log("action userLogout, logoutData:", data)
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
        console.log("action patchUserProfile:", data)
        commit('updateUserDetails', data)
    },

    loadUserDetails({ commit, state }) {
      getAPI.get('api/users/' + state.user_id + '/')
      .then(data => {
        console.log('action loadUserDetails:', data)
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
        // // console.log('action loadMissionList:', data)
        // let allMissions = data.data;
        // let missList = [];
        // // console.log('allMissions:', allMissions)
        // allMissions.forEach((mission) => {
        //   missList.push({"id":mission.id, "name":mission.name})
        //   // console.log('miss', mission)
        // })
        // // console.log('missList:',missList)
        // commit('setMissionList', missList)
        commit('setMissions', data.data)
      })
      .catch(error => {
        console.log(error)
      })
    },

  
    async get_listmissionusers({commit, state}, missionId) {
      // await getAPI.get('/api/users/missionusers/?missionid=1',
      await getAPI.get('/api/users/missionusers/' + missionId + '/',
        {headers: { 'Authorization': 'Token ' + state.token }})
      .then(data => {
        console.log('get_listmissionusers action', data.data)
        commit('setMissionuser', data.data)})
      .catch(error => {
        console.log(error)
        commit('setMissionuser', {})
      })
    },

    async patchMissionUserProfile({ commit, state }, missionusercredentials) {
      const { data } = await getAPI.patch('api/users/missionusers/' + state.missionUserDetails.id + '/', {
          job: missionusercredentials.job,
          team_lab: missionusercredentials.team_lab,
          description: missionusercredentials.description,
        }, {
        headers: { 'Authorization': 'Token ' + state.token,}})
        console.log("action patchMissionUserProfile:", data)
        commit('updateMissionUserDetails', data)
    },

    // async loadMissionDetails({ commit }, missionID) {
    //   console.log('CHALALA', missionID)
    //   await getAPI.get('/api/missions/' + missionID + '/')
    //   .then(data => {
    //     console.log('action loadmissionDetails:', data.data)
    //     let missionDetails = data.data
    //     commit('setMissionDetails', missionDetails)
    //   })
    //   .catch(error => {
    //     console.log(error)
    //   })
    // },

  },

  modules: {

  }
})
