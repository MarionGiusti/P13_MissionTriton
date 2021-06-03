import { shallowMount, createLocalVue  } from "@vue/test-utils";
import Actu from "@/components/Actu";
import Vuetify from'vuetify'
import Vuex from 'vuex'

const localVue = createLocalVue()
localVue.use(Vuex)

describe("Actu component unit tests: ", () => {
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
      postActu:[
        {
          category: "Actu",
          content: "Embarquement direction le Kamchatka",
          created_at: "2020-06-02T08:00:00:00Z",
          id: 9,
          mission: 1,
          mission_user: 5,
          post_image:"",
          title:"Départ",
          updated_at:"2020-06-02T08:00:00:00Z",
          video_url:""
        },
        {
          category: "Actu",
          content: "La vie du plancton",
          created_at: "2020-06-10T10:00:00:00Z",
          id: 10,
          mission: 1,
          mission_user: 5,
          post_image:"",
          title:"Conférence de J. Schmidt",
          updated_at:"2020-06-10T10:00:00:00Z",
          video_url:""
        },
      ]
    }
    store = new Vuex.Store({
      state,
      actions
    })

    wrapper = shallowMount(Actu, {
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
    });
  })

  it("verify computed verifMember", () => {
    expect(wrapper.vm.verifMember).toBeFalse
  })

  it("renders state postActu", () => {
    expect(wrapper.vm.postActu).toEqual([
      {
        category: "Actu",
        content: "Embarquement direction le Kamchatka",
        created_at: "2020-06-02T08:00:00:00Z",
        id: 9,
        mission: 1,
        mission_user: 5,
        post_image:"",
        title:"Départ",
        updated_at:"2020-06-02T08:00:00:00Z",
        video_url:""
      },
      {
        category: "Actu",
        content: "La vie du plancton",
        created_at: "2020-06-10T10:00:00:00Z",
        id: 10,
        mission: 1,
        mission_user: 5,
        post_image:"",
        title:"Conférence de J. Schmidt",
        updated_at:"2020-06-10T10:00:00:00Z",
        video_url:""
      }
    ])
  });
});
