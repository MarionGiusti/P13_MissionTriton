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
    shipPositionsDetails: {},
    scheduleUserDetails: {},
    postActu: {},
    postMedBoard: {},
  },

  getters: {
    // getField,
    currentMission: (state) => (id) => {
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

    // memberMission:(state)=> (missionName) => {
    //   var missionNameUser = []
    //   for (const mission in state.userDetails.missions) {
    //     var miss = state.userDetails.missions[mission].name
    //     console.log('mission', miss)
    //     missionNameUser.push(miss)
    //   }
    //   // var miss = state.missions.find(missions => missions.id === parseInt(id))
    //   // console.log("MISS",miss.name)
    //   // // for (const item  in miss) {
    //   // //   var missi = miss[item].name
    //   // //   console.log('missi', missi)
    //   // // }     
    //   return missionNameUser.includes(missionName)
    // }
    memberMission:(state, getters)=> (id) => {
      var missionNameUser = []
      for (const mission in state.userDetails.missions) {
        var miss = state.userDetails.missions[mission].name
        console.log('mission', miss)
        missionNameUser.push(miss)
      }  
      return missionNameUser.includes(getters.currentMission(id)["name"])
    }
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
    },
    
    updateMissionList(data) {
      console.log('updatemissionlist:', data)
    },

    setMissionuser(state, missionUserDetails) {
      state.missionUserDetails = missionUserDetails
    },

    updateMissionUserDetails(state, data) {
      state.missionUserDetails = Object.assign({}, state.missionUserDetails, data);
    },

    setShipPositions(state, shipPositionsDetails) {
      state.shipPositionsDetails = shipPositionsDetails
    },

    setScheduleUser(state, data) {
      state.scheduleUserDetails = data
    },

    setPostActu(state, data) {
      state.postActu = data
    },

    setPostMedBoard(state, data) {
      state.postMedBoard = data
    },

    updatePostActu(state, data) {
      state.postActu = Object.assign({}, state.postActu, data);
    },
  
  },

  actions: {
    async userLogin({ commit }, usercredentials) {
      const { data } = await getAPI.post('api/api-token-auth/', {
          username: usercredentials.username,
          password: usercredentials.password
        })
      localStorage.setItem('token', data.token)
      localStorage.setItem('userId', data.user_id)
      commit('setTokenId', data)
    },

    async userRegister({ commit }, usercredentials) {
      const { data } = await getAPI.post('api/dj-rest-auth/registration/', {
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
        commit('updateMissionList', data)
    },

    async userLogout({ commit }) {
      // await getAPI.post("api/dj-rest-auth/logout/", {
      // })
      localStorage.removeItem('userId')
      localStorage.removeItem('token')
      const { data }  = {
        userId: null,
        token: null
      }
      console.log(data, 'local', localStorage)
      commit('setTokenId', data)
      console.log("action userLogout, logoutData:", data)
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
        commit('updateUserDetails', data)
    },

    async getUserDetails({ commit, state }) {
      await getAPI.get(`api/users/${state.userId}`)
      .then(data => {
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
        commit('updateMissionUserDetails', data)
    },

    async getShipPositionsMission({commit}, missionId) {
      await getAPI.get(`/api/missions/shippositions/?missionid=${missionId}`)
      .then(data => {
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
        } else {
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
      commit('updatePostActu', data)
    },

    async removePost({state}, postId) {
      await getAPI.delete(`/api/posts/${postId}/`, {
        headers: { 'Authorization': 'Token ' + state.token,}
      })
    },

  },
})
