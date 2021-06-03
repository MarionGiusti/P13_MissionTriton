import { shallowMount, createLocalVue  } from "@vue/test-utils";
import ScrollAllMissions from "@/components/ScrollAllMissions";
import Vuetify from'vuetify'
import Vuex from 'vuex'

const localVue = createLocalVue()
localVue.use(Vuex)

describe("ScrollAllMissions component unit tests: ", () => {

  let vuetify
  let getters
  let store

 
  beforeEach(() => {
    vuetify = new Vuetify()
    getters = {
      pastMissions: () => [
        {
          id: 1,
          name: "NEMO21",
          ship_name: "Bubble",
          start_date: "2020-06-02",
          end_date: "2020-06-17",
          description: "Direction le Kamchatka"
        }
      ],
      nowMissions: () => [],
      futureMissions: () => [
        {
          id: 2,
          name: "SEAWE",
          ship_name: "Endeavour",
          start_date: "2021-10-16",
          end_date: "2021-11-28",
          description: "Direction l'Alaska'"
        }
      ]
    }

    store = new Vuex.Store({
      getters
    })
  })

  it("renders store.getters.pastMissions/nowMissions/futureMissions", () => {
    const wrapper = shallowMount(ScrollAllMissions, {
      localVue,
      vuetify,
      store,
    });
    expect(wrapper.html()).toContain('<h3>Archivées</h3>')
    expect(wrapper.vm.missionGroups).toEqual(
      [
        {
          "missions": [
            {
              "description": "Direction le Kamchatka",
              "end_date": "2020-06-17",
              "id": 1,
              "name": "NEMO21",
              "ship_name": "Bubble",
              "start_date": "2020-06-02"
            }
          ],
          "name": "Archivées"
        },
        {
          "missions": [],
          "name": "En cours"
        },
        {
          "missions": [
            {
              "description": "Direction l'Alaska'",
              "end_date": "2021-11-28",
              "id": 2,
              "name": "SEAWE",
              "ship_name": "Endeavour",
              "start_date": "2021-10-16"
            }
          ],
          "name": "À venir"
        }
      ]
    )
  });
});
