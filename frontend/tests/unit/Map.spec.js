import { shallowMount, createLocalVue  } from "@vue/test-utils";
import Map from "@/components/Map";
import Vuetify from'vuetify'
import Vuex from 'vuex'

const localVue = createLocalVue()
localVue.use(Vuex)

describe("Map component unit tests: ", () => {
  let vuetify
  let store
  let state
  let actions
  let wrapper

  beforeEach(() => {
    vuetify = new Vuetify()
    actions = {
      getShipPositionsMission: jest.fn()
    }

    state = {
      shipPositionsDetails:[
        {
          date_time: "2020-06-04T10:30:00Z",
          id: 1,
          latitude: "45",
          longitude: "147",
          mission: 1
        },
        {
          date_time: "2020-06-05T09:00:00Z",
          id: 2,
          latitude: "41",
          longitude: "146",
          mission: 1
        },
      ]
    }

    store = new Vuex.Store({
      state,
      actions
    })

    wrapper = shallowMount(Map, {
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

  it("renders store.getters.pastMissions/nowMissions/futureMissions", () => {
    expect(wrapper.vm.shipPositionsDetails).toEqual([
      {
        date_time: "2020-06-04T10:30:00Z",
        id: 1,
        latitude: "45",
        longitude: "147",
        mission: 1
      },
      {
        date_time: "2020-06-05T09:00:00Z",
        id: 2,
        latitude: "41",
        longitude: "146",
        mission: 1
      },
    ])
  });
});
