import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from '../axios-api'

// import { getField, updateField } from 'vuex-map-fields';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('token') || null,
    userId: localStorage.getItem('userId') || null,
    userDetails: {},
    missions: [],
    missionUserDetails: {},
    // currentMissionDetails: {},
    shipPositionsDetails: {},
    scheduleUserDetails: {},
    postActu: {},
    postMedBoard: {},
    // postBoard: {},
  },

  getters: {
    // getField,
    currentMission: (state) => (id) => {
      // console.log(JSON.stringify(state.missions))
      return state.missions.find(missions => missions.id === parseInt(id))
    },
    futureMissions: (state)=> {
      return state.missions.filter(
        missions => new Date(missions.start_date).getTime() > new Date().getTime()
        ).slice().sort((a, b) => new Date(a.start_date).getTime() - new Date(b.start_date).getTime())
    },
    nowMissions: (state)=> {
      return state.missions.filter(
        missions => new Date(missions.start_date).getTime() <= new Date().getTime() &&
      new Date(missions.end_date).getTime() >= new Date().getTime()
      ).slice().sort((a, b) => new Date(a.start_date).getTime() - new Date(b.start_date).getTime())
    },
    pastMissions: (state)=> {
      return state.missions.filter(
        missions => new Date(missions.end_date).getTime() < new Date().getTime()
      ).slice().sort((a, b) => new Date(a.start_date).getTime() - new Date(b.start_date).getTime())
    },
  },

  mutations: {
    // updateField,

    setTokenId(state, data) {
      state.token = data.token
      state.userId = data.user_id
    },

    setUserDetails(state, userDetails) {
      state.userDetails = userDetails
    },

    updateUserDetails(state, data) {
      state.userDetails = Object.assign({}, state.userDetails, data);
    },

    setMissions(state, allMissions) {
      state.missions = allMissions
      // console.log('setMissions mutation:', allMissions)
    },

    // setCurrentMissionDetails(state, data) {
    //   state.currentMissionDetails = data
    //   console.log('setcurrentMissionDetails mutation:', data)
    // },
    
    updateMissionList(data) {
      console.log('updatemissionlist:', data)
    },

    setMissionuser(state, missionUserDetails) {
      state.missionUserDetails = missionUserDetails
      // console.log('setMissionuser mutation:', missionUserDetails)
    },

    updateMissionUserDetails(state, data) {
      state.missionUserDetails = Object.assign({}, state.missionUserDetails, data);
    },

    // setTimelines(timelinesDetails) {
    //   console.log('setTimelines mutation:', timelinesDetails)
    // },

    setShipPositions(state, shipPositionsDetails) {
      state.shipPositionsDetails = shipPositionsDetails
      // console.log('setShipPositions mutation:', shipPositionsDetails)
    },

    setScheduleUser(state, data) {
      state.scheduleUserDetails = data
      // console.log('setScheduleUser mutation:', data)
    },

    setPostActu(state, data) {
      state.postActu = data
      // console.log('setPostActu mutation:', data)
    },

    // setPostMed(state, data) {
    //   state.postMed = data
    // },

    setPostMedBoard(state, data) {
      state.postMedBoard = data
    },

    updatePostActu(state, data) {
      state.postActu = Object.assign({}, state.postActu, data);
    },
  
  },

  actions: {
    async userLogin({ commit }, usercredentials) {
        const { data } = await getAPI.post('/api-token-auth/', {
            username: usercredentials.username,
            password: usercredentials.password
          })
        localStorage.setItem('token', data.token)
        localStorage.setItem('userId', data.user_id)
        // console.log("action userLogin, dataToken:", data)
        commit('setTokenId', data)
    },

    async userRegister({ commit }, usercredentials) {
      // const { data } = await getAPI.post('/api/users/', {
      //     username: usercredentials.username,
      //     first_name: usercredentials.firstname,
      //     last_name: usercredentials.lastname,
      //     password: usercredentials.password1,
      //     email: usercredentials.email,
      //   })
      //   commit('setTokenId', data )
      const { data } = await getAPI.post('/dj-rest-auth/registration/', {
            username: usercredentials.username,
            password1: usercredentials.password1,
            password2: usercredentials.password2,
            email: usercredentials.email,
          })
          commit('setTokenId', data )

    },

    async missionRegister ({ commit, state }, missioncredentials) {
      const { data } = await getAPI.post('/api/missions/', {
          name: missioncredentials.name,
          ship_name: missioncredentials.ship,
          start_date: missioncredentials.start_date,
          end_date: missioncredentials.end_date,
        }, {
          headers: { 'Authorization': 'Token ' + state.token,}})
        // console.log('action missionRegister:', data)
        commit('updateMissionList', data)
    },

    userLogout({ commit }) {
      const data  =  {
        userId: null,
        token: null
      }
      localStorage.removeItem('token')
      localStorage.removeItem('userId')
      // console.log("action userLogout, logoutData:", data)
      commit('setTokenId', data)
    },

    async patchUserProfile({ commit, state }, usercredentials) {
        const { data } = await getAPI.patch(`api/users/${state.userId}/`, {
          username: usercredentials.username,
          first_name: usercredentials.first_name,
          last_name: usercredentials.last_name,
          email: usercredentials.email,
          linkedin_link: usercredentials.linkedin_link,
          researchgate_link: usercredentials.researchgate_link,
        }, {
        headers: { 'Authorization': 'Token ' + state.token,}})
        // console.log("action patchUserProfile:", data)
        commit('updateUserDetails', data)
    },

    async getUserDetails({ commit, state }) {
      await getAPI.get(`api/users/${state.userId}`)
      .then(data => {
        // console.log('action getUserDetails:', data)
        let userDetails = data.data
        commit('setUserDetails', userDetails)
      })
      .catch(error => {
        console.log(error)
      })
    },

    // Beginning to get list in the search icon
    async loadMissionList({ commit }) {
      await getAPI.get('/api/missions/')
      .then(data => {
        commit('setMissions', data.data)
      })
      .catch(error => {
        console.log(error)
      })
    },

    // Account page to get mission user of one user and one mission
    async getListMissionUsers({commit, state}, missionId) {
      await getAPI.get(`/api/users/missionusers/?missionid=${missionId}`,
        {headers: { 'Authorization': 'Token ' + state.token }})
      .then(data => {
        // console.log('getListMissionUsers action', data.data)
        commit('setMissionuser', data.data[0])})
      .catch(error => {
        console.log(error)
        commit('setMissionuser', {})
      })
    },

    async patchMissionUserProfile({ commit, state }, missionusercredentials) {
        const { data } = await getAPI.patch(`api/users/missionusers/${state.missionUserDetails.id}/`, {         
          job: missionusercredentials.job,
          team_lab: missionusercredentials.team_lab,
          description: missionusercredentials.description,
        }, {
        headers: { 'Authorization': 'Token ' + state.token,}})
        // console.log("action patchMissionUserProfile:", data)
        commit('updateMissionUserDetails', data)
    },

    // async getTimelinesMission({commit}, missionId) {
    //   await getAPI.get(`/api/missions/timelines/?missionid=${missionId}`)
    //   .then(data => {
    //     // console.log('getTimelinesMission action', data.data)
    //     commit('setTimelines', data.data)})
    //   .catch(error => {
    //     console.log(error)
    //   })
    // },

    async getShipPositionsMission({commit}, missionId) {
      await getAPI.get(`/api/missions/shippositions/?missionid=${missionId}`)
      .then(data => {
        // console.log('getShipPositionsMission action', data.data)
        commit('setShipPositions', data.data)})
      .catch(error => {
        console.log(error)
      })
    },

    async getScheduleUser({commit, state}) {
      await getAPI.get(`/api/schedules/`, {
        headers: { 'Authorization': 'Token ' + state.token,
      }})
      .then(data => {
        // console.log('getScheduleUser', data.data)
        commit('setScheduleUser', data.data)})
      .catch(error => {
        console.log(error)
      })
    },

    async getPost({commit}, params) {
      await getAPI.get(`/api/posts/`, {params:params})
      .then(data => {
        console.log('getPost', data.data)
        if (params["category"] == 'Actu') {
          commit('setPostActu', data.data)
          console.log('ACTU', params["category"])

        }
        // else if (params["category"] == 'Med') {
        //   commit('setPostMed', data.data)
        //   console.log('MED', params["category"])

        // }
        // else if (params["category"] == 'Onboard') {
        //   commit('setPostBoard', data.data)
        //   console.log('BOARD', params["category"])
        // }
        else {
          commit('setPostMedBoard', data.data)
        }
      })
      .catch(error => {
        console.log(error)
      })
    },

    async postPost({ commit, state }, postcredentials) {
      const { data } = await getAPI.post('/api/posts/', 
      postcredentials,
      {
        headers: { 
          'Authorization': 'Token ' + state.token,
          'Content-Type': 'application/json',   
        }
      })
      commit('updatePostActu', data)
    },

    async patchPost({ commit, state }, postcredentials) {
      const { data } = await getAPI.patch(`api/posts/${postcredentials.id}/`, {         
        title: postcredentials.title,
        content: postcredentials.content,
        video_url: postcredentials.video_url,
      }, {
      headers: { 'Authorization': 'Token ' + state.token,}})
      // console.log("action patchMissionUserProfile:", data)
      commit('updatePostActu', data)
    },

    async removePost({state}, postId) {
      await getAPI.delete(`/api/posts/${postId}/`, {
        headers: { 'Authorization': 'Token ' + state.token,}
      })
    },

  },

  modules: {

  }
})
