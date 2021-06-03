import { shallowMount, createLocalVue  } from "@vue/test-utils";
import Team from "@/components/Team";
import Vuetify from'vuetify'
import Vuex from 'vuex'

const localVue = createLocalVue()
localVue.use(Vuex)

describe("Team component unit tests: ", () => {
  let vuetify
  let store

  beforeEach(() => {
    vuetify = new Vuetify()   
  })

  it("renders data team", () => {
    const wrapper = shallowMount(Team, {
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
      data() {
        return {
          team: [
            {
              first_name: "Jo",
              last_name:"Pellen",
              email:"jo.pellent@test.com",
              job:"acousticien",
              description:""
            },
            {
              first_name: "Jane",
              last_name:"Dupalis",
              email:"jane.dupalis@test.com",
              job:"chercheuse en géochimie",
              description:""
            }
          ]
        }
      },
      computed: {
        verifMember() { return false },
      }
    });
    expect(wrapper.vm.verifMember).toBeFalse
    expect(wrapper.vm.team).toEqual([
      {
        first_name: "Jo",
        last_name:"Pellen",
        email:"jo.pellent@test.com",
        job:"acousticien",
        description:""
      },
      {
        first_name: "Jane",
        last_name:"Dupalis",
        email:"jane.dupalis@test.com",
        job:"chercheuse en géochimie",
        description:""
      }
    ])
    expect(wrapper.html()).toContain("Jo Pellen", "Jane Dupalis", "chercheuse en géochimie")
  });
});
