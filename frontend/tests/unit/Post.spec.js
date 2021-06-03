import { shallowMount, createLocalVue  } from "@vue/test-utils";
import Post from "@/components/Post";
import Vuetify from'vuetify'
import Vuex from 'vuex'

const localVue = createLocalVue()
localVue.use(Vuex)

describe("Post component unit tests: ", () => {
  let vuetify
  let store
  let state
  let actions
  let wrapper

  beforeEach(() => {
    vuetify = new Vuetify()
    actions = {
      getPost: jest.fn()
    }
    state = {
      postMedBoard:[
        {
          category: "Med",
          content: "Le plancton ...",
          created_at: "2020-06-10T14:00:00:00Z",
          id: 9,
          mission: 1,
          mission_user: 5,
          post_image:"media/post_pics/sea.jpg",
          title:"Zoom sur le plancton",
          updated_at:"2020-06-10T14:30:00:00Z",
          video_url:"https://www.youtube.com/embed/EmvnIq7ZtVM"
        },
        {
          category: "Onboard",
          content: "Hey Lorem Ipsum",
          created_at: "2020-06-12T10:00:00:00Z",
          id: 10,
          mission: 1,
          mission_user: 5,
          post_image:"/media/post_pics/pizza.jpg",
          title:"Soirée pizza",
          updated_at:"2020-06-12T10:00:00:00Z",
          video_url:""
        },
      ]
    }

    store = new Vuex.Store({
      state,
      actions
    })

    wrapper = shallowMount(Post, {
      localVue,
      vuetify,
      store,
      mocks: {
        $route: {
          params: {
            id: 1
          }
        },
      },
      computed: {
        verifMember() { return false }
      }
    })
  })
  
  it("verify computed verifMember", () => {
    expect(wrapper.vm.verifMember).toBeFalse
  })

  it("renders state postMedBoard", () => {
    expect(wrapper.vm.postMedBoard).toEqual([
      {
        category: "Med",
        content: "Le plancton ...",
        created_at: "2020-06-10T14:00:00:00Z",
        id: 9,
        mission: 1,
        mission_user: 5,
        post_image:"media/post_pics/sea.jpg",
        title:"Zoom sur le plancton",
        updated_at:"2020-06-10T14:30:00:00Z",
        video_url:"https://www.youtube.com/embed/EmvnIq7ZtVM"
      },
      {
        category: "Onboard",
        content: "Hey Lorem Ipsum",
        created_at: "2020-06-12T10:00:00:00Z",
        id: 10,
        mission: 1,
        mission_user: 5,
        post_image:"/media/post_pics/pizza.jpg",
        title:"Soirée pizza",
        updated_at:"2020-06-12T10:00:00:00Z",
        video_url:""
      },
    ])
  });
});
